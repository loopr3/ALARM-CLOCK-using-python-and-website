# ⏰ Alarm Timer with Snooze

A dual-version **Alarm Timer App** — available in both **Web** and **Python CLI** versions.  
You can set a countdown timer, enable alarm sound, and use built-in snooze options (5, 10, 15 minutes or custom time).

---

## 🚀 Features

### 🖥️ Web Version (`index.html`)
- Modern, responsive interface with dark mode design.  
- Input custom minutes and seconds for countdown.  
- Supports any online or local MP3 alarm sound.  
- One-click **Enable Sound** button (to bypass browser autoplay restrictions).  
- Multiple **Snooze options**: 5, 10, 15 minutes, or custom snooze.  
- Works **offline** if you download and link `alarm.mp3`.

### 🐍 Python Version (`main.py`)
- Command-line based timer that plays an alarm sound after countdown.  
- Uses the `playsound` library to play audio.  
- Built-in snooze menu (5m / 10m / 15m / custom snooze).  
- Automatically downloads `alarm.mp3` if not found.  
- Clean and minimal terminal UI.

---

## 🧩 How to Use

### 🔹 Web Version
1. Open `index.html` in your browser.  
2. Enter the **Minutes** and **Seconds**.  
3. Click **Enable Sound 🔊** once (required for browsers).  
4. Press **Start** to begin countdown.  
5. Use **Snooze** buttons when alarm rings.

> 💡 Tip: To use it offline, download the `alarm.mp3` and paste its local path in the “Alarm Sound URL” input.

---

### 🔹 Python Version
1. Install required dependencies:
   ```bash
   pip install playsound requests
Run the script:
python main.py
Enter the countdown time when prompted.
When the alarm rings, choose an option from the snooze menu.
📦 Files in This Repository
File	Description
index.html	Web-based alarm timer with snooze and audio controls
main.py	Python command-line alarm timer with snooze options
alarm.mp3	Default alarm sound (can be replaced with your own)
⚙️ Tech Stack

Frontend: HTML, CSS, JavaScript

Backend (CLI): Python 3

Audio: MP3 format (plays locally or via URL)

🧠 Author

Developed by Priyansu Pati
🎓 C.V. Raman Global University
💻 Aspiring coder & web developer
