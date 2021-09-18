import time
import pyautogui
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

def put(message):
	time.sleep(0.1)
	pyautogui.click()
	pyautogui.typewrite("\n")
	time.sleep(0.1)
	pyautogui.typewrite(message)
	time.sleep(0.1)
	pyautogui.typewrite("\n")
	time.sleep(0.1)

messages = open("msg.txt", "r")
msgreal = messages.readline()
msgreal = msgreal.rstrip('\n')
msgbot = messages.readline()
msgbot = msgbot.rstrip('\n')
messages.close()

storage = open("pixels.txt", "r")
realx = int(storage.readline())
realy = int(storage.readline())
botx = int(storage.readline())
boty = int(storage.readline())
msgrealpos = int(storage.readline()),int(storage.readline())
msgbotpos = int(storage.readline()),int(storage.readline())
storage.close()

while 1:
	pyautogui.scroll(1000)
	time.sleep(0.1)
	pyautogui.scroll(-100)
	time.sleep(0.1)
	if pyautogui.position() != msgbotpos:
		condition = input("continue? (y/n):")
		if (condition[0] == 'n'):
			exit()