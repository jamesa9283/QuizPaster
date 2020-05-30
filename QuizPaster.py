# -*- coding: utf-8 -*-
"""
Created on Sat May 30 16:13:55 2020

I created this in 15 minutes, its crap and pretty cursed.

** IT MAY BREAK YOUR COMPUTER. BIG WARNING HERE. **

@author: james
"""

import pyperclip
import threading
from pynput.keyboard import Key, Controller

keyboard = Controller()


inp = input()

pyperclip.copy(inp)
spam = pyperclip.paste()
      
        
def printit():
  threading.Timer(10.0, printit).start()
  with keyboard.pressed(Key.ctrl):
    keyboard.press('v')
    keyboard.release('v')
    
printit()