
import keyboard

#It writes the content to output 
keyboard.write("GEEKS FOR GEEKS\n") 
 
#It writes the keys r, k and end of line  
keyboard.press_and_release('shift + r, shift + k, \n') 
keyboard.press_and_release('R, K') 
 
#It blocks until ctrl is pressed 
keyboard.wait('Ctrl') 

#Output

GEEKS FOR GEEKS 
RK
rk
