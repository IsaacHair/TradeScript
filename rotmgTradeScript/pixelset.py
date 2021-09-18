import pyautogui
import time
import winsound

storage = open("pixels.txt", "w")
time.sleep(2)
realx, realy = pyautogui.position()
winsound.Beep(750, 250)
storage.write(str(realx)+"\n"+str(realy)+"\n")
time.sleep(2)
botx, boty = pyautogui.position()
winsound.Beep(750, 250)
storage.write(str(botx)+"\n"+str(boty)+"\n")
time.sleep(2)
msgrealx,msgrealy = pyautogui.position()
winsound.Beep(750, 250)
storage.write(str(msgrealx)+"\n"+str(msgrealy)+"\n")
time.sleep(2)
msgbotx,msgboty = pyautogui.position()
winsound.Beep(750, 250)
storage.write(str(msgbotx)+"\n"+str(msgboty)+"\n")
storage.close()