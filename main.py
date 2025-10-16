import requests
from playsound import playsound
import time
import os

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

# Download alarm sound (only if not already downloaded)
def download_mp3(url, filename="alarm.mp3"):
    if not os.path.exists(filename):  # download only once
        response = requests.get(url)
        with open(filename, "wb") as f:
            f.write(response.content)
    return filename

def countdown(seconds):
    print(CLEAR)
    while seconds > 0:
        minutes_left = seconds // 60
        seconds_left = seconds % 60
        print(f"{CLEAR_AND_RETURN}⏳ Alarm in: {minutes_left:02d}:{seconds_left:02d}")
        time.sleep(1)
        seconds -= 1

def play_alarm():
    mp3_file = download_mp3("https://www.fesliyanstudios.com/play-mp3/4383", "alarm.mp3")
    print(f"{CLEAR_AND_RETURN}🔔 Time’s up! Playing alarm...")
    playsound(mp3_file)

def alarm(seconds):
    countdown(seconds)
    while True:  # keep ringing until user stops
        play_alarm()

        print("\n--- Snooze Menu ---")
        print("1. Snooze 5 minutes")
        print("2. Snooze 10 minutes")
        print("3. Snooze 15 minutes")
        print("4. Custom snooze time")
        print("5. Stop alarm")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            countdown(5 * 60)
        elif choice == "2":
            countdown(10 * 60)
        elif choice == "3":
            countdown(15 * 60)
        elif choice == "4":
            minutes = int(input("Enter snooze minutes: "))
            countdown(minutes * 60)
        elif choice == "5":
            print("✅ Alarm stopped.")
            break
        else:
            print("❌ Invalid choice, please try again.")

# Main program
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))
total_seconds = minutes * 60 + seconds
alarm(total_seconds)
