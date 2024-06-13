import speech_recognition as sr
import time
import os
import pyttsx3

# Ensure the FLAC_CONVERTER environment variable is set
os.environ['FLAC_CONVERTER'] = "/opt/homebrew/bin/flac"

def append_reminder(reminder):
    with open("reminders.txt", "a") as file:
        file.write(f"{reminder}\n")
    print(f"Reminder set: {reminder}")

def show_reminders():
    if os.path.exists("reminders.txt"):
        with open("reminders.txt", "r") as file:
            reminders = file.readlines()
            if reminders:
                print("Your reminders:")
                for index, reminder in enumerate(reminders):
                    print(f"{index + 1}. {reminder.strip()}")
                read_aloud_reminders(reminders)
            else:
                print("You have no reminders.")
    else:
        print("You have no reminders.")

def clear_reminders():
    if os.path.exists("reminders.txt"):
        os.remove("reminders.txt")
        print("Reminders cleared.")
    else:
        print("No reminders to clear.")

def read_aloud_reminders(reminders):
    engine = pyttsx3.init(driverName='nsss')  # Use 'nsss' driver on macOS
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)
    
    engine.say("Here are your current reminders:")
    for reminder in reminders:
        engine.say(reminder.strip())
    
    engine.runAndWait()

def listen_for_response(recognizer):
    try:
        with sr.Microphone() as source:
            print("Please respond (you have 5 seconds)")
            
            recognizer.adjust_for_ambient_noise(source)
            
            # Countdown for 5 seconds
            for i in range(5, 0, -1):
                print(f"Listening in {i}...")
                time.sleep(1)
                
            try:
                audio = recognizer.listen(source, timeout=5)
                response = recognizer.recognize_google(audio)
                print("You said:", response)
                return response.lower()
            except sr.WaitTimeoutError:
                print("You need to speak within 5 seconds.")
            except sr.UnknownValueError:
                print("Sorry, I could not understand the audio.")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return None

def speech_to_text():
    recognizer = sr.Recognizer()
    
    try:
        with sr.Microphone() as source:
            print("Please Speak (You have 5 seconds)")
            
            recognizer.adjust_for_ambient_noise(source)
            
            # Countdown for 5 seconds
            for i in range(5, 0, -1):
                print(f"Speak in {i}...")
                time.sleep(1)
                
            try:
                audio = recognizer.listen(source, timeout=5)
                text = recognizer.recognize_google(audio)
                print("You said:", text)
                
                if "set a reminder for" in text.lower():
                    reminder_text = text.lower().split("set a reminder for", 1)[1].strip()
                    append_reminder(reminder_text)
                
                elif "show reminders" in text.lower():
                    show_reminders()
                
                elif "clear reminders" in text.lower():
                    clear_reminders()
                
                else:
                    print("Command not recognized.")
                
                # Ask for input to show reminders or clear them
                if "show reminders" not in text.lower() and "clear reminders" not in text.lower():
                    print("Do you want to see your current reminders? Please say 'yes' or 'no'.")
                    response = listen_for_response(recognizer)
                    if response and "yes" in response:
                        show_reminders()
                    else:
                        print("Okay, no reminders will be shown.")
                    
                    print("Do you want to clear the reminders? Please say 'yes' or 'no'.")
                    response = listen_for_response(recognizer)
                    if response and "yes" in response:
                        clear_reminders()
                    else:
                        print("Okay, reminders will not be cleared.")
            
            except sr.WaitTimeoutError:
                print("You need to speak within 5 seconds.")
            except sr.UnknownValueError:
                print("Sorry, I could not understand the audio.")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    speech_to_text()
