#Copyright (c) 2025 SeoliWorks
#This software is released under the MIT License, see LICENSE.

import pyautogui as pau
import pyperclip
import time
import os

def autoGUI(Pic_URL, Pic_name):

    #cmddef    
    DownloadCmd = f'powershell Invoke-WebRequest -Uri {Pic_URL} -OutFile Downloads/{Pic_name}'
    OpenCmd = f'C:/Users/%username%/Downloads/{Pic_name}'

    #download a pic on DL-dir
    pyperclip.copy(DownloadCmd)
    pau.hotkey('win','r')
    time.sleep(1)
    pau.hotkey('ctrl','v')
    pau.press('enter')
    time.sleep(10)

    #open the pic
    pyperclip.copy(OpenCmd)
    pau.hotkey('win','r')
    time.sleep(1)
    pau.hotkey('ctrl','v')
    pau.press('enter')
    time.sleep(2.5)

    #set it as wallpaper
    pau.hotkey('ctrl','b')
    time.sleep(2)

    #close the pic
    pau.hotkey('alt','f4')

    return 0
