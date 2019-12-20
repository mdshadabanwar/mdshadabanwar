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
        pyautogui.typewrite(self.tcode)

    def vendorDetails(self):
        pyautogui.press(['tab','tab'])
        pyautogui.press('enter')
        pyautogui.press('f6')
        pyautogui.press(['tab','tab','tab'])
        pyautogui.typewrite('wipro')        
        pyautogui.press(['tab','tab'])
        pyautogui.press('enter')
                        

if __name__ == '__main__':
    sap = saplogon('xxxxxxxxx','xxxxxxxxxx','xxxxxx','xxxxxxx')
    pyautogui.PAUSE=5
    sap.activate_preinvoke()
    pyautogui.PAUSE=5
    sap.activate_saplogon()
    pyautogui.PAUSE=5
    sap.activate_postinvoke()
    pyautogui.PAUSE=5
    sap.open_instance()
    pyautogui.PAUSE=5
    sap.SapLogin()
    pyautogui.PAUSE=5
    pyautogui.press('enter')
    pyautogui.press('enter')       
    sap.tcodeVal()
    pyautogui.PAUSE=5
    pyautogui.press('enter')
    sap.vendorDetails()
    