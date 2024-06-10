import tkinter as tk
import threading
import time
import speech_recognition as sr
import keyboard
import pyperclip
import pyautogui
import pygame.mixer
import requests

def paste_string_in_any_field(message):
    pyperclip.copy(message)
    pyautogui.hotkey('ctrl', 'v')
    print("Đã dán tin nhắn: ", message)

def sendData(pin, value, i):
    url = f"https://sgp1.blynk.cloud/external/api/update?token=s4IEZXPS6DFlYAACZC_6z-rNmdU1erLH&{pin}={value}"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Dữ liệu đã được gửi thành công. Đèn {i} đã được {value}")
        status_label.config(text=f"Đèn {i} đã được {value}")
    else:
        print("Có lỗi xảy ra:", response.status_code, response.text)
        status_label.config(text=f"Có lỗi xảy ra khi thay đổi đèn {i}: {response.status_code} {response.text}")

def listen_and_send():
    status_label.config(text="Vui lòng nhập văn bản...")
    pygame.mixer.music.load("beep.wav")
    pygame.mixer.music.play()
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio_data = recognizer.listen(source)

    try:
        status_label.config(text="Đang nhận dạng giọng nói...")
        message = recognizer.recognize_google(audio_data, language="vi")
        status_label.config(text="Văn bản của bạn: " + message)
        paste_string_in_any_field(message)
    except sr.UnknownValueError:
        status_label.config(text="Không thể nhận dạng giọng nói")
    except sr.RequestError as e:
        status_label.config(text="Lỗi kết nối; {0}".format(e))

def listen_and_control():
    status_label.config(text="Vui lòng nói điều gì đó...")
    pygame.mixer.music.load("beep.wav")
    pygame.mixer.music.play()
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio_data = recognizer.listen(source)

    try:
        status_label.config(text="Đang nhận dạng giọng nói...")
        text = recognizer.recognize_google(audio_data, language="vi")
        status_label.config(text="Bạn: " + text)

        if "mở đèn 1" in text or "Mở Đèn 1" in text:
            sendData("v0", "On1", 1)
        elif "tắt đèn 1" in text or "Tắt Đèn 1" in text:
            sendData("v0", "Off1", 1)
        elif "mở đèn 2" in text or "Mở Đèn 2" in text:
            sendData("v0", "On2", 2)
        elif "tắt đèn 2" in text or "Tắt Đèn 2" in text:
            sendData("v0", "Off2", 2)
        elif "mở đèn 3" in text or "Mở Đèn 3" in text:
            sendData("v0", "On3", 3)
        elif "tắt đèn 3" in text or "Tắt Đèn 3" in text:
            sendData("v0", "Off3", 3)
        elif "mở đèn 4" in text or "Mở Đèn 4" in text:
            sendData("v0", "On4", 4)
        elif "tắt đèn 4" in text or "Tắt Đèn 4" in text:
            sendData("v0", "Off4", 4)
        elif "mở đèn 5" in text or "Mở Đèn 5" in text:
            sendData("v0", "On5", 5)
        elif "tắt đèn 5" in text or "Tắt Đèn 5" in text:
            sendData("v0", "Off5", 5)
        elif "mở đèn 6" in text or "Mở Đèn 6" in text:
            sendData("v0", "On6", 6)
        elif "tắt đèn 6" in text or "Tắt Đèn 6" in text:
            sendData("v0", "Off6", 6)
        elif "mở đèn 7" in text or "Mở Đèn 7" in text:
            sendData("v0", "On7", 7)
        elif "tắt đèn 7" in text or "Tắt Đèn 7" in text:
            sendData("v0", "Off7", 7)
        elif "mở đèn 8" in text or "Mở Đèn 8" in text:
            sendData("v0", "On8", 8)
        elif "tắt đèn 8" in text or "Tắt Đèn 8" in text:
            sendData("v0", "Off8", 8)
        else:
            status_label.config(text="Không hiểu lệnh điều khiển")
    except sr.UnknownValueError:
        status_label.config(text="Không thể nhận dạng giọng nói")
    except sr.RequestError as e:
        status_label.config(text=f"Lỗi kết nối; {e}")

def start_listening_thread():
    if mode.get() == "text":
        thread = threading.Thread(target=listen_and_send)
    else:
        thread = threading.Thread(target=listen_and_control)
    thread.start()

def start_listening(event=None):
    status_label.config(text="Khởi động... Bạn có 1 giây để chuẩn bị.")
    time.sleep(1)
    start_listening_thread()

def toggle_mode():
    if mode.get() == "text":
        mode.set("control")
        mode_button.config(text="Chuyển sang chế độ Soạn Văn Bản")
        status_label.config(text="Chế độ hiện tại: Điều Khiển Thiết Bị")
    else:
        mode.set("text")
        mode_button.config(text="Chuyển sang chế độ Điều Khiển Thiết Bị")
        status_label.config(text="Chế độ hiện tại: Soạn Văn Bản")

root = tk.Tk()
root.title("Voice Typing and Control App")

status_label = tk.Label(root, text="Chưa sẵn sàng")
status_label.pack(pady=10)

mode_button = tk.Button(root, text="Chuyển sang chế độ Điều Khiển Thiết Bị", command=toggle_mode)
mode_button.pack(pady=5)

recognizer = sr.Recognizer()
mic = sr.Microphone()

pygame.mixer.init()

mode = tk.StringVar(value="text")
keyboard.add_hotkey('ctrl+shift+l', start_listening)
root.mainloop()
