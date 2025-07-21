import pyautogui

print(pyautogui.size())

x,y = pyautogui.position()

pyautogui.moveTo(100,500,1)

pyautogui.moveRel(300,200,1)

pyautogui.dragTo(200,300,button='left')

pyautogui.dragTo(200, 300, duration=1)

pyautogui.dragRel(500,200,duration=1)


pyautogui.click()

pyautogui.doubleClick()

pyautogui.click(clicks=2)

pyautogui.click(100,10, duration=2)

pyautogui.scroll(300)

pyautogui.write("Hi! User")
