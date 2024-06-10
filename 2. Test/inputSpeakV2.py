import pyautogui
import pyperclip
import time
import speech_recognition as sr
import keyboard
import tkinter as tk
from tkinter import scrolledtext
from threading import Thread

def paste_string_in_any_field(message):
    pyperclip.copy(message)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')

def listen_and_send():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        status_label.config(text="Vui lòng nói tin nhắn bạn muốn gửi...")
        root.update()
        recognizer.adjust_for_ambient_noise(source)
        audio_data = recognizer.listen(source)
        
        try:
            status_label.config(text="Đang nhận dạng giọng nói...")
            root.update()
            message = recognizer.recognize_google(audio_data, language="vi")
            status_label.config(text="Tin nhắn của bạn: " + message)
            display_text.insert(tk.END, message + '\n')
            root.update()
            paste_string_in_any_field(message)
        except sr.UnknownValueError:
            status_label.config(text="Không thể nhận dạng giọng nói")
            root.update()
        except sr.RequestError as e:
            status_label.config(text="Lỗi kết nối; {0}".format(e))
            root.update()

def start_listening():
    listening_thread = Thread(target=listen_and_send)
    listening_thread.start()

# Tạo giao diện Tkinter
root = tk.Tk()
root.title("Voice Typing App")
root.geometry("500x400")

# Thêm các thành phần vào giao diện
status_label = tk.Label(root, text="Nhấn nút để bắt đầu nhận diện giọng nói")
status_label.pack(pady=10)

start_button = tk.Button(root, text="Bắt đầu", command=start_listening)
start_button.pack(pady=10)

display_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10)
display_text.pack(pady=10)

# Khởi động giao diện
root.mainloop()
