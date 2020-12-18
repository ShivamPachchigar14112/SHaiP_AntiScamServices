import pyautogui, time
usr_input = input()
time.sleep(10)
while(0 == 0): #This runs infinitely to print usr_input infintely
    pyautogui.typewrite(usr_input)
    pyautogui.press("enter")
