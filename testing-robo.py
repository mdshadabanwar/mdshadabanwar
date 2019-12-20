# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 12:40:50 2019

@author: shadab
"""

import pyautogui,time

pyautogui.hotkey('win','d')

time.sleep(.25)

pyautogui.hotkey('win','r')

time.sleep(.25)

pyautogui.typewrite("C:\Program Files (x86)\SAP\FrontEnd\SAPgui\saplogon.exe")

time.sleep(.25)

pyautogui.press('enter')

time.sleep(7) 
pyautogui.hotkey('win','up') 