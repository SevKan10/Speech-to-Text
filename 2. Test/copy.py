import pyautogui
import pyperclip
import time

global_string = "Xin chào các bạn"

def paste_string_in_any_field():
    pyperclip.copy(global_string)
    time.sleep(5)

    pyautogui.hotkey('ctrl', 'v')

paste_string_in_any_field()