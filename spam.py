import pyautogui, time
time.sleep(10)
f = open("spm")
for words in f:
    pyautogui.typewrite(words)
    pyautogui.press("enter")
    #time.sleep(10)
