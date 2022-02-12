#Install Library
>>> import pyautogui

#Display position mouse / RGB color
>>> pyautogui.displayMousePosition()
X: 1464 Y:  673 RGB: ( 30,  30,  30)
>>> pyautogui.position()  # current mouse x and y

>>> pyautogui.moveTo(100, 150) # Move the mouse to XY coordinates.
>>> pyautogui.click()          # Click the mouse.
>>> pyautogui.doubleClick()     # Double click the mouse.
>>> pyautogui.click(100, 200)  # Move the mouse to XY coordinates and click it.
>>> pyautogui.click('button.png') # Find where button.png appears on the screen and click it.
>>> pyautogui.move(400, 0)      # Move the mouse 400 pixels to the right of its current position.
>>> pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)  # Use tweening/easing function to move mouse over 2 seconds.
>>> pyautogui.write('Hello world!', interval=0.25)  # type with quarter-second pause in between each key
>>> pyautogui.press('esc')     # Press the Esc key. All key names are in pyautogui.KEY_NAMES

>>> with pyautogui.hold('shift'):  # Press the Shift key down and hold it.
        pyautogui.press(['left', 'left', 'left', 'left'])  # Press the left arrow key 4 times.
>>> # Shift key is released automatically.

>>> pyautogui.hotkey('ctrl', 'c') # Press the Ctrl-C hotkey combination.
>>> pyautogui.alert('This is the message to display.') # Make an alert box appear and pause the program until OK is clicked.

>>> screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
>>> screenWidth, screenHeight
(2560, 1440)
>>> pyautogui.size()  # current screen resolution width and height

>>> currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
>>> currentMouseX, currentMouseY
(1314, 345)

>>> pyautogui.onScreen(x, y)  # True if x & y are within the screen.
True

>>> pyautogui.PAUSE = 2.5 #Set up a 2.5 second pause after each PyAutoGUI call

##Click
>>> pyautogui.rightClick(x=moveToX, y=moveToY)
>>> pyautogui.middleClick(x=moveToX, y=moveToY)
>>> pyautogui.doubleClick(x=moveToX, y=moveToY)
>>> pyautogui.tripleClick(x=moveToX, y=moveToY)



