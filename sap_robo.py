# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 10:51:00 2019

@author: shadab
"""

import pyautogui, time

class saplogon(object): 
    def __init__(self,user,passwrd,inst,tcode):
        self.userid=user
        self.pswrd = passwrd
        self.instance=inst
        self.tcode=tcode
        pyautogui.FAILSAFE=True
        pyautogui.PAUSE=2
        
    def activate_preinvoke(self):
        
        pyautogui.hotkey('win','d')
    
    def activate_saplogon(self):
        try:
            pyautogui.hotkey('win','r')
            pyautogui.typewrite('C:\Program Files (x86)\SAP\FrontEnd\SAPgui\saplogon.exe')
            pyautogui.press('enter')
            return True
        except:
            return False
    
    def activate_postinvoke(self):
        pyautogui.hotkey('win','up')
        
    def open_instance(self):
        try:
            pyautogui.hotkey('ctrl','f')
            pyautogui.typewrite(self.instance)
            pyautogui.press('enter')
            return True
        except:
            return False
        
        
    def SapLogin(self):
        pyautogui.typewrite(self.userid)
        pyautogui.press('tab')
        #time.sleep(1)
        pyautogui.typewrite(self.pswrd)
    
    def tcodeVal(self):
        pyautogui.typewrite('ME2L')
        #pyautogui.hotkey('ctrl', 'n')
        #pyautogui.doubleClick(109, 61)
        #pyautogui.typewrite('me2l')

if __name__ == '__main__':
    sap = saplogon('xxxxxxxx','xxxxxxxxx','xxxxxx','xxxxx')
    sap.activate_preinvoke()
    #time.sleep(5)
    sap.activate_saplogon()
    
    #time.sleep(7)
    sap.activate_postinvoke()
    #time.sleep(5)
    sap.open_instance()
    #time.sleep(5)
    
    sap.SapLogin()
    #time.sleep(3)
  
    #time.sleep(5)
    
    #pyautogui.alert('Phase 1 Completed')
    
    pyautogui.press('enter')
    
    pyautogui.PAUSE=15
    #pyautogui.press('tab')
    
    #pyautogui.hotkey('shift','tab')
    
    pyautogui.typewrite('ME2L')
    pyautogui.PAUSE=15
    #time.sleep(5)
    pyautogui.press('enter')
    
    