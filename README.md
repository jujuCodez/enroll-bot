# DLSU Enrollment Bot 🧠📚

An automation script built with **Selenium** to assist DLSU students in automating course **enrollment**, **class swapping**, and **retry-based registration** on the [Animo.sys Portal](http://animo.sys.dlsu.edu.ph/). Designed to reduce the hassle of manual enrollment by looping through tasks, detecting Cloudflare issues, and retrying failed attempts.

> ⚠️ For educational use only. This project is not affiliated with or endorsed by De La Salle University.

---

## 🚀 Features

- 🔁 **Auto-looping class enrollment** and **class swapping**
- 🌐 **Cloudflare bypass handling**
- 🧪 Robust retry mechanisms for failed page interactions
- ⌨️ **Hotkey-controlled execution**
  - `Ctrl+Shift+S` → Pause/Resume loop
  - `Ctrl+Shift+Q` → Exit script
- 🧩 Compatible with Firefox and Geckodriver
- 🧪 Tested on DLSU Animo.sys portal (PeopleSoft system)

---

## 📁 File Structure

| File | Description |
|------|-------------|
| `main-bot.py` | Main automation script for logging in, enrolling, or swapping classes |
| `course_enrollment_monitor.js` | (Optional) JS-based extension/helper logic (not integrated in `main-bot.py`) |
| `clicker` | Unknown binary/tool (possibly part of extended features) |
| `README.md` | Project documentation |

---

## 🖥️ Requirements

- Python 3.8+
- Firefox browser
- [Geckodriver](https://github.com/mozilla/geckodriver/releases)
- Installed Python packages:
  ```bash
  pip install selenium helium keyboard
  ```

---

## 🔧 Setup & Usage

1. **Update your credentials** and class codes in `main-bot.py`:
   ```python
   username = "YOUR_DLSU_ID"
   password = "YOUR_PASSWORD"
   class_codes = ["1234", "5678"]
   ```

2. **Check/Update Firefox & Geckodriver paths**:
   ```python
   options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
   driver = webdriver.Firefox(executable_path=r'G:\Path\to\geckodriver.exe', options=options)
   ```

3. **Run the script**:
   ```bash
   python main-bot.py
   ```

4. **Choose an option when prompted**:
   ```
   1: Class Swap Bot
   2: Enrollment Bot
   3: Enrollment Bot with Pause/Resume
   4: Retry Login & Enrollment with Cloudflare Recovery
   ```

---

## ❗ Notes

- Keep your **class codes updated** before the enrollment period begins.
- Monitor Cloudflare blocks; the bot will detect and retry automatically.
- Ensure your **internet connection** is stable to avoid session drops.

---

## 🛡️ Disclaimer

This tool is intended for **personal use only**. Use responsibly and avoid abusing the DLSU systems. This bot mimics human behavior but is still subject to CAPTCHA, rate limits, and university IT policies.

---

## 📜 License

MIT License. Feel free to fork and adapt, but don’t sell or redistribute without proper credit.

---

## 💡 Author

Developed by a Computer Engineering student from De La Salle University.  
Questions or feedback? Feel free to open an issue or fork a pull request.

```
