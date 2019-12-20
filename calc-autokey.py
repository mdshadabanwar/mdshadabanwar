import pyautogui, time

pyautogui.click((pyautogui.locateCenterOnScreen('1key.png')))
time.sleep(0.25)
pyautogui.click((pyautogui.locateCenterOnScreen('pluskey_new.png')))
time.sleep(0.25)
pyautogui.click((pyautogui.locateCenterOnScreen('1key.png')))
time.sleep(0.25)
pyautogui.press('enter')