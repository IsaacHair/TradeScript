import time
import pyautogui
import winsound

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
	pyautogui.moveTo(msgrealpos)
	put(msgreal)
	pixel = pyautogui.screenshot(region=(realx, realy, 1, 1))
	color = pixel.getcolors()
	x,y,z = color[0][1]
	if (x < 50 or x > 60):
		winsound.Beep(750, 1000)
	time.sleep(4)
	if pyautogui.position() != msgrealpos:
		condition = input("continue? (y/n):")
		if (condition[0] == 'n'):
			exit()
	pyautogui.moveTo(msgbotpos)
	put(msgbot)
	pixel = pyautogui.screenshot(region=(botx, boty, 1, 1))
	color = pixel.getcolors()
	x,y,z = color[0][1]
	if (x < 50 or x > 60):
		winsound.Beep(750, 1000)
	time.sleep(4)
	if pyautogui.position() != msgbotpos:
		condition = input("continue? (y/n):")
		if (condition[0] == 'n'):
			exit()