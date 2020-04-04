# Using Keyboard module in Python 
import keyboard 
  

keyboard.add_hotkey('a', lambda: keyboard.press_and_release('tab,tab,a')) 
#^ Creates a hotkey and assigns a function...in this case it tabs twice and presses 'a'
  
keyboard.wait('esc') #Deactivates hotkey

