import os
import pygame
from gtts import gTTS
import tkinter as tk
from tkinter import messagebox

class TextToSpeechApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text to Speech")
        self.create_widgets()
        pygame.mixer.init()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Enter text to convert to speech:")
        self.label.pack(pady=10)

        self.text_entry = tk.Entry(self.root, width=50)
        self.text_entry.pack(pady=10)

        self.speak_button = tk.Button(self.root, text="Speak", command=self.speak)
        self.speak_button.pack(pady=10)

    def speak(self):
        text = self.text_entry.get()
        if not text:
            messagebox.showwarning("Input Error", "Please enter some text")
            return

        tts = gTTS(text=text, lang='en')
        tts.save("speech.mp3")
        self.play_audio("speech.mp3")

    def play_audio(self, file_path):
        if os.path.exists(file_path):
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
        else:
            messagebox.showerror("File Error", "Audio file not found")

if __name__ == "__main__":
    root = tk.Tk()
    app = TextToSpeechApp(root)
    root.mainloop()
