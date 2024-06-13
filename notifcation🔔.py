import time
import subprocess
import pygame

def type_print(message):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.025)
    print()  

def notify(title, message):
    # Initialize pygame mixer
    pygame.mixer.init()
    
    # Load and play the notification sound
    pygame.mixer.music.load('noti.mp3')
    pygame.mixer.music.play()

    # Send the notification
    subprocess.run([
        'osascript', '-e',
        f'display notification "{message}" with title "{title}"'
    ])

    # Allow time for the sound to play
    time.sleep(3)

def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"Notification in {i} seconds...", end='\r', flush=True)
        time.sleep(1)
    type_print("\nTime's up! Sending notification...")

def main():
    type_print("Welcome to alarm and notifications! ⏰")
    
    type_print("What title do you want your notification to be: ")
    title = input()
    
    type_print("What should your message be: ")
    message = input()
    
    type_print("How many seconds until the notification? ")
    countdown_seconds = int(input())
    
    type_print(f"\nYour Title: {title}\nYour Message: {message}\nYour Countdown: {countdown_seconds} seconds\n")
    
    type_print("Starting countdown...")
    countdown(countdown_seconds)
    
    type_print("Sending notification now...")
    notify(title, message)

if __name__ == "__main__":
    main()
