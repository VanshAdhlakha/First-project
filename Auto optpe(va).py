import pyautogui
import subprocess
import time

subprocess.Popen('notepad.exe')
time.sleep(1)
message = "Hello!"
repeat = 2
wait = 0.001

for i in range(repeat):
    pyautogui.write(message, interval = wait)
    pyautogui.press('enter')