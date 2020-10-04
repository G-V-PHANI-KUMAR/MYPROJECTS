import pyautogui as p
import time as t
#THE FOOBAR CODE...
p.hotkey("winleft")
t.sleep(2)
p.typewrite("chrome\n",0.1)
p.typewrite("https://www.google.com/search?q=list+comprehension+python&rlz=1C1CHBF_enIN912IN912&oq=list+comprehension+&aqs=chrome.1.69i57j0l7.3737j0j7&sourceid=chrome&ie=UTF-8\n",)
t.sleep(3)
i=0
while i<30:
    p.hotkey('ctrl', 't')
    p.typewrite("https://www.google.com/search?q=list+comprehension+python&rlz=1C1CHBF_enIN912IN912&oq=list+comprehension+&aqs=chrome.1.69i57j0l7.3737j0j7&sourceid=chrome&ie=UTF-8\n",)
    t.sleep(0.5)
    i+=1
