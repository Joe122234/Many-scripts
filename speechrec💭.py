import speech_recognition as sr
import time
import os
import webbrowser

# Ensure the FLAC_CONVERTER environment variable is set
os.environ['FLAC_CONVERTER'] = "/opt/homebrew/bin/flac"

def perform_search(query):
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)
    print(f"Searching for: {query}")

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
                perform_search(text)
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
