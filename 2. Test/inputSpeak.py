import pyautogui
import pyperclip
import time
import speech_recognition as sr
import keyboard

def paste_string_in_any_field(message):
    pyperclip.copy(message)
    pyautogui.hotkey('ctrl', 'v')

def listen_and_send(recognizer, mic):
    print("Vui lòng nói tin nhắn bạn muốn gửi...")
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio_data = recognizer.listen(source)

    try:
        print("Đang nhận dạng giọng nói...")
        message = recognizer.recognize_google(audio_data, language="vi")
        print("Tin nhắn của bạn: " + message)
        paste_string_in_any_field(message)
    except sr.UnknownValueError:
        print("Không thể nhận dạng giọng nói")
    except sr.RequestError as e:
        print("Lỗi kết nối; {0}".format(e))

def main():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("Khởi động... Bạn có 1 giây để chuẩn bị.")
    time.sleep(1)  

    keyboard.add_hotkey('ctrl+q', lambda: listen_and_send(recognizer, mic))
    keyboard.wait('esc')

if __name__ == "__main__":
    main()
