import time
import pyautogui
import winsound

time.sleep(2)
pos = pyautogui.position()
winsound.Beep(750, 250)

while 1:
	if pyautogui.position() != pos:
		exit()
	time.sleep(0.01)
	pyautogui.click()
	time.sleep(0.01)
	pyautogui.typewrite("you are a cutie")
	time.sleep(0.01)
	pyautogui.typewrite("\n")