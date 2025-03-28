from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from helium import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import keyboard
import time
import json



# options = Options()
# options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(ChromeDriverManager().install())



choice = int(input('1: Class Swap Bot\n2: Enrollment Bot\n3: Test\nYour Choice: '))
options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(executable_path=r'G:\ANIMO SYS ENROLLMENT BOT\geckodriver-v0.33.0-win32\geckodriver.exe', options=options)
actions = ActionChains(driver)


# Information
username = "12112512"
password = "D=JhnX^=$z9EZS8"
class_codes = ["4766", "4767"]
url = "http://animo.sys.dlsu.edu.ph/psp/ps/?cmd=login"
url2 = "http://animo.sys.dlsu.edu.ph/psp/ps/?cmd=login"

print("No cloudlfare?")

def is_cloudflare_error_present():
    try:
        error_message = driver.find_element(By.XPATH, "//p[contains(text(), 'Error code 524')]")
        return True
    except:
        return False

def refresh_page():
    driver.refresh()

def wait_for_real_page(driver):
    while True:  # This creates an infinite loop
        try:
            WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.NAME, "userid")))
            print("No Cloudflare :D")
            break  # Exit the loop once the element is found
        except Exception:
            print("Yes Cloudflare :(")

driver.get(url)


if choice == 1:
    wait_for_real_page(driver)
    print("Option 1 selected")
    driver.get(url)
    driver.implicitly_wait(6)
    driver.find_element(By.NAME, "userid").send_keys(username)
    driver.find_element(By.NAME, "pwd").send_keys(password)
    print("login done")
    driver.find_element(By.NAME,"Submit").click()
    # driver.find_element(By.CLASS_NAME,"ptnav2toggle").click()
    actions.move_to_element(driver.find_element(By.CLASS_NAME,"ptnav2toggle")).click().perform()
    driver.find_element(By.ID,"fldra_HCCC_ENROLLMENT").click()
    driver.find_element(By.XPATH,"//a[contains(text(),'Enrollment: Swap Classes')]").click()
    # TODO: kete
    driver.switch_to.frame('ptifrmtgtframe')
    print("switched to iframe")



    last_executed_line = 0
    loop = 0
    while True:
        for class_code in class_codes:
            try:
                print(f'class code: {class_code}')
                element_dropdown = driver.find_element(By.ID,"DERIVED_REGFRM1_DESCR50$38$")
                select = Select(element_dropdown)
                select.select_by_index(7)
                driver.find_element(By.NAME, "DERIVED_REGFRM1_CLASS_NBR").send_keys(class_code)
                driver.find_element(By.LINK_TEXT,"enter").click()
                # driver.implicitly_wait(20)
                driver.find_element(By.LINK_TEXT,"Next").click()
                # driver.implicitly_wait(20)
                driver.find_element(By.LINK_TEXT,"Finish Swapping").click()
                time.sleep(2)
                print("Class swap process complete")
                # Increment the loop counter and wait for 3 seconds before proceeding to the next loop iteration
                loop += 1
                print("Loop " + str(loop))

                # time.sleep(2)
                # driver.implicitly_wait(20)
                driver.find_element(By.LINK_TEXT,"swap").click()
            except Exception as e:
                print(f"Error occurred: Some dumb long error")
                while True:
                    if is_cloudflare_error_present():
                        print("Cloudflare error detected. Refreshing after 50 seconds...")
                        time.sleep(5)  # Wait for 50 seconds
                        refresh_page()
                    else:
                        print("Page is accessible.")
                        break
                driver.get('https://animo.sys.dlsu.edu.ph/psp/ps/EMPLOYEE/HRMS/c/SA_LEARNER_SERVICES.SSR_SSENRL_SWAP.GBL?PORTALPARAM_PTCNAV=HC_SSR_SSENRL_SWAP&EOPP.SCNode=HRMS&EOPP.SCPortal=EMPLOYEE&EOPP.SCName=HCCC_ENROLLMENT&EOPP.SCLabel=Enrollment&EOPP.SCPTfname=HCCC_ENROLLMENT&FolderPath=PORTAL_ROOT_OBJECT.CO_EMPLOYEE_SELF_SERVICE.HCCC_ENROLLMENT.HC_SSR_SSENRL_SWAP&IsFolder=false')
                while True:
                    if is_cloudflare_error_present():
                        print("Cloudflare error detected. Refreshing after 50 seconds...")
                        time.sleep(5)  # Wait for 50 seconds
                        refresh_page()
                    else:
                        print("Page is accessible.")
                        break
                driver.switch_to.frame('ptifrmtgtframe')
                # driver.implicitly_wait(20)
                continue
elif choice == 2:
    wait_for_real_page(driver)
    print("Option 2 selected")
    time.sleep(1)
    driver.find_element(By.NAME, "userid").send_keys(username)
    driver.find_element(By.NAME, "pwd").send_keys(password)
    print("login done")
    driver.find_element(By.NAME, "Submit").click()
    driver.implicitly_wait(5)
    driver.get("https://animo.sys.dlsu.edu.ph/psp/ps/EMPLOYEE/HRMS/s/WEBLIB_PTPP_SC.HOMEPAGE.FieldFormula.IScript_AppHP?pt_fname=CO_EMPLOYEE_SELF_SERVICE&FolderPath=PORTAL_ROOT_OBJECT.CO_EMPLOYEE_SELF_SERVICE&IsFolder=true")
    driver.find_element(By.ID, "fldra_HCCC_ENROLLMENT").click()
    driver.find_element(By.XPATH, "//a[contains(text(),'Enrollment: Add Classes')]").click()
    time.sleep(2)
    driver.switch_to.frame('ptifrmtgtframe')
    print("switched to iframe")
    loop = 0
    while True:
        try:
            loop += 1
            print("Loop " + str(loop))
            # driver.implicitly_wait(15)
            driver.find_element(By.NAME, "DERIVED_REGFRM1_LINK_ADD_ENRL$114$").click()
            driver.find_element(By.LINK_TEXT, "Finish Enrolling").click()
            driver.find_element(By.LINK_TEXT, "Add Another Class").click()
            print("Enrollment complete")
            time.sleep(1)
        except Exception as e:
            print(f"Error occurred: Some dumb long error")
            driver.get('https://animo.sys.dlsu.edu.ph/psp/ps/EMPLOYEE/HRMS/c/SA_LEARNER_SERVICES.SSR_SSENRL_CART.GBL?FolderPath=PORTAL_ROOT_OBJECT.CO_EMPLOYEE_SELF_SERVICE.HCCC_ENROLLMENT.HC_SSR_SSENRL_CART_GBL&IsFolder=false&IgnoreParamTempl=FolderPath%2cIsFolder')
            driver.switch_to.frame('ptifrmtgtframe')
            # driver.implicitly_wait(20)
            continue
elif choice == 3:
    wait_for_real_page(driver)
    print("Option 2 selected")
    time.sleep(1)
    driver.find_element(By.NAME, "userid").send_keys(username)
    driver.find_element(By.NAME, "pwd").send_keys(password)
    print("login done")
    driver.find_element(By.NAME, "Submit").click()
    driver.implicitly_wait(5)
    driver.get(
        "https://animo.sys.dlsu.edu.ph/psp/ps/EMPLOYEE/HRMS/s/WEBLIB_PTPP_SC.HOMEPAGE.FieldFormula.IScript_AppHP?pt_fname=CO_EMPLOYEE_SELF_SERVICE&FolderPath=PORTAL_ROOT_OBJECT.CO_EMPLOYEE_SELF_SERVICE&IsFolder=true")
    driver.find_element(By.ID, "fldra_HCCC_ENROLLMENT").click()
    driver.find_element(By.XPATH, "//a[contains(text(),'Enrollment: Add Classes')]").click()
    time.sleep(2)
    driver.switch_to.frame('ptifrmtgtframe')
    print("switched to iframe")

    loop = 0
    running = True

    def toggle_running():
        global running
        running = not running
        print(f"{'Stopping' if not running else 'Resuming'} loop...")


    # Assign a key combo to stop/resume the loop
    keyboard.add_hotkey('ctrl+shift+s', toggle_running)

    while True:
        while running:
            try:
                loop += 1
                print("Loop " + str(loop))
                driver.find_element(By.NAME, "DERIVED_REGFRM1_LINK_ADD_ENRL$114$").click()
                driver.find_element(By.LINK_TEXT, "Finish Enrolling").click()
                driver.find_element(By.LINK_TEXT, "Add Another Class").click()
                print("Enrollment complete")
                time.sleep(0.4)
            except Exception as e:
                print(f"Error occurred: Some dumb long error: {str(e)}")
                driver.get(
                    'https://animo.sys.dlsu.edu.ph/psp/ps/EMPLOYEE/HRMS/c/SA_LEARNER_SERVICES.SSR_SSENRL_CART.GBL?FolderPath=PORTAL_ROOT_OBJECT.CO_EMPLOYEE_SELF_SERVICE.HCCC_ENROLLMENT.HC_SSR_SSENRL_CART_GBL&IsFolder=false&IgnoreParamTempl=FolderPath%2cIsFolder')
                driver.switch_to.frame('ptifrmtgtframe')
                continue

        time.sleep(0.1)  # Sleep briefly to avoid maxing out CPU usage

    # To exit the entire script, you can use another hotkey:
    keyboard.add_hotkey('ctrl+shift+q', lambda: exit())
elif choice == 4:
    wait_for_real_page(driver)
    print("Option 4 selected")
    time.sleep(1)
    while True:  # Start an infinite loop
        try:
            time.sleep(1)
            driver.find_element(By.NAME, "userid").send_keys(username)
            driver.find_element(By.NAME, "pwd").send_keys(password)
            print("Login attempt...")
            driver.find_element(By.XPATH, "//input[@value='Sign In' and @name='Submit']").click()
            driver.implicitly_wait(5)
            driver.get(
                "https://animo.sys.dlsu.edu.ph/psp/ps/EMPLOYEE/HRMS/s/WEBLIB_PTPP_SC.HOMEPAGE.FieldFormula.IScript_AppHP?pt_fname=CO_EMPLOYEE_SELF_SERVICE&FolderPath=PORTAL_ROOT_OBJECT.CO_EMPLOYEE_SELF_SERVICE&IsFolder=true")

            # Attempt to find the HCCC_ENROLLMENT element
            driver.find_element(By.ID, "fldra_HCCC_ENROLLMENT").click()
            print("HCCC_ENROLLMENT found and clicked.")
            break  # Exit the loop if successful
        except Exception as e:
            print("Failed to find HCCC_ENROLLMENT, retrying login...")
            driver.get(url)  # Reset to the login page and try again
    driver.find_element(By.XPATH, "//a[contains(text(),'Enrollment: Add Classes')]").click()
    time.sleep(2)
    driver.switch_to.frame('ptifrmtgtframe')
    print("switched to iframe")

    loop = 0
    running = True


    def toggle_running():
        global running
        running = not running
        print(f"{'Stopping' if not running else 'Resuming'} loop...")


    # Assign a key combo to stop/resume the loop
    keyboard.add_hotkey('ctrl+shift+s', toggle_running)

    while True:
        while running:
            try:
                loop += 1
                print("Loop " + str(loop))
                driver.find_element(By.NAME, "DERIVED_REGFRM1_LINK_ADD_ENRL$114$").click()
                driver.find_element(By.LINK_TEXT, "Finish Enrolling").click()
                driver.find_element(By.LINK_TEXT, "Add Another Class").click()
                print("Enrollment complete")
                time.sleep(0.4)
            except Exception as e:
                print(f"Error occurred: Some dumb long error: {str(e)}")
                if is_cloudflare_error_present():
                    print("Cloudflare error detected. Pausing loop...")
                    running = False  # Pause the loop
                    while is_cloudflare_error_present():
                        time.sleep(2)  # Wait for 5 seconds before checking again
                        refresh_page()
                    print("Page is accessible. Resuming loop...")
                    running = True  # Resume the loop
                    driver.get(
                        'https://animo.sys.dlsu.edu.ph/psp/ps/EMPLOYEE/HRMS/c/SA_LEARNER_SERVICES.SSR_SSENRL_CART.GBL?FolderPath=PORTAL_ROOT_OBJECT.CO_EMPLOYEE_SELF_SERVICE.HCCC_ENROLLMENT.HC_SSR_SSENRL_CART_GBL&IsFolder=false&IgnoreParamTempl=FolderPath%2cIsFolder')
                    driver.switch_to.frame('ptifrmtgtframe')
                continue

        time.sleep(0.1)  # Sleep briefly to avoid maxing out CPU usage

    # To exit the entire script, you can use another hotkey:
    keyboard.add_hotkey('ctrl+shift+q', lambda: exit())
