const fs = require('fs');
const notifier = require('node-notifier');
const { CourierClient } = require('@trycourier/courier');

// Initialize Courier client with your API token
const client = new CourierClient({
  authorizationToken: 'pk_prod_FP80475E5HMEG8KRPA2R7HKT1DMX' // Replace with your Courier API key
});

let previousData = null;

function sendNotification(title, message) {
  notifier.notify({
    title: title,
    message: message,
    sound: true,
    wait: true
  });
}

async function sendMessage(title, body) {
  try {
    const response = await client.send({
      message: {
        to: {
          email: 'michael_aringo@dlsu.edu.ph',
          data: {
            name: title
          }
        },
        content: {
          title: title,
          body: body
        },
        routing: {
          method: 'all',
          channels: ['email']
        }
      }
    });

    console.log('Message sent successfully:', response);
  } catch (error) {
    console.error('Error sending message:', error);
  }
}

async function scanTable(page) {
  if (!page.url().includes('view_course_offerings')) {
    await page.goto('https://enroll.dlsu.edu.ph/dlsu/view_course_offerings', {
      waitUntil: 'domcontentloaded'
    });
    await new Promise(resolve => setTimeout(resolve, 8000));
    await page.type('input[name="p_id_no"]', '12112512');
    await page.click('input[name="p_button"]');
    await new Promise(resolve => setTimeout(resolve, 1000));
  }

  await page.$eval('input[name="p_course_code"]', el => el.value = '');
  await page.type('input[name="p_course_code"]', 'GEWORLD');
  await new Promise(resolve => setTimeout(resolve, 500));
  await page.click('input[name="p_button"]');
  await new Promise(resolve => setTimeout(resolve, 500));

  const tableData = await page.evaluate(() => {
    const rows = Array.from(document.querySelectorAll('table tr'));
    return rows.map(row => {
      const cells = Array.from(row.querySelectorAll('td, th'));
      return cells.map(cell => cell.innerText.trim());
    }).filter(row => row.length > 0);
  });

  return tableData;
}

function compareData(previous, current) {
  if (!previous || !current) return null;

  const changes = [];
  for (let i = 1; i < Math.min(current.length, previous.length); i++) {
    if (current[i][6] !== previous[i][6] || current[i][7] !== previous[i][7]) {
      changes.push({
        course: current[i][1],
        section: current[i][2],
        prevEnrlCap: previous[i][6],
        newEnrlCap: current[i][6],
        prevEnrolled: previous[i][7],
        newEnrolled: current[i][7]
      });
    }
  }
  return changes.length > 0 ? changes : null;
}

function logChanges(changes) {
  const logMessage = `[${new Date().toISOString()}] Changes detected:\n${JSON.stringify(changes, null, 2)}\n\n`;

  console.log(logMessage);
  fs.appendFileSync('enrollment_changes_LBYCPF3.log', logMessage, 'utf8');
}

async function runScan(page) {
  try {
    const currentData = await scanTable(page);
    const changes = compareData(previousData, currentData);

    if (changes) {
      const changeMessage = `Changes detected:\n${changes.map(change => `Course: ${change.course} \nSection: ${change.section}, \nprevEnrolled: ${change.prevEnrolled}, \nnewEnrolled: ${change.newEnrolled}`).join('\n')}`;
      logChanges(changes);
      sendNotification('Course Enrollment Changes', changeMessage);
      await sendMessage('Course Enrollment Changes GEWORLD', changeMessage);
    } else {
      console.log(`[${new Date().toISOString()}] No changes detected`);
    }

    previousData = currentData;

  } catch (error) {
    console.error(`[${new Date().toISOString()}] Error during scan:`, error);

    // Handle errors more gracefully
    try {
      await page.reload({ waitUntil: 'domcontentloaded' });
      console.log(`[${new Date().toISOString()}] Page refreshed due to error.`);
      // Retry scan after refresh
      const currentData = await scanTable(page);
      const changes = compareData(previousData, currentData);

      if (changes) {
        const changeMessage = `Changes detected:\n${changes.map(change => `Course: ${change.course} \nSection: ${change.section}, \nprevEnrolled: ${change.prevEnrolled}, \nnewEnrolled: ${change.newEnrolled}`).join('\n')}`;
        logChanges(changes);
        sendNotification('Course Enrollment Changes', changeMessage);
        await sendMessage('Course Enrollment Changes', changeMessage);
      } else {
        console.log(`[${new Date().toISOString()}] No changes detected after refresh`);
      }

      previousData = currentData;

    } catch (refreshError) {
      console.error(`[${new Date().toISOString()}] Error during page refresh:`, refreshError);
    }
  }
}

async function main() {
  const { connect } = await import('puppeteer-real-browser');
  const { page, browser } = await connect({
    headless: false,
    turnstile: true,
    fingerprint: false,
    skipTarget: [],
    args: [],
    customConfig: {},
    connectOption: {},
    fpconfig: {},
  });

  console.log('Course Enrollment Monitoring service has started');

  async function scanLoop() {
    await runScan(page);
    // Repeat scan after a delay
    setTimeout(scanLoop, 5000); // Adjust as needed
  }

  scanLoop();

  console.log('Automatic scanning started. Press Ctrl+C to exit.');
}

main().catch(console.error);
