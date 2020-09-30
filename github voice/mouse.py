import pyautogui

print (pyautogui.position())
#Point(x=684, y=413)
#Point(x=695, y=507)
#Point(x=1547, y=58)
'''
x =684
y=413
pyautogui.moveTo(x,y)
pyautogui.click(button='left',clicks=1,interval =0.1)
x1 =695
y1 =507
pyautogui.moveTo(x1,y1)
pyautogui.click(button='left',clicks=1,interval =0.1)

    >>> screenWidth, screenHeight = pyautogui.size() # Returns two integers, the width and height of the screen. (The primary monitor, in multi-monitor setups.)
    >>> currentMouseX, currentMouseY = pyautogui.position() # Returns two integers, the x and y of the mouse cursor's current position.
    >>> pyautogui.moveTo(100, 150) # Move the mouse to the x, y coordinates 100, 150.
    >>> pyautogui.click() # Click the mouse at its current location.
    >>> pyautogui.click(200, 220) # Click the mouse at the x, y coordinates 200, 220.
    >>> pyautogui.move(None, 10)  # Move mouse 10 pixels down, that is, move the mouse relative to its current position.
    >>> pyautogui.doubleClick() # Double click the mouse at the
    >>> pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad) # Use tweening/easing function to move mouse over 2 seconds.
    >>> pyautogui.write('Hello world!', interval=0.25)  # Type with quarter-second pause in between each key.
    >>> pyautogui.press('esc') # Simulate pressing the Escape key.
    >>> pyautogui.keyDown('shift')
    >>> pyautogui.write(['left', 'left', 'left', 'left', 'left', 'left'])
    >>> pyautogui.keyUp('shift')
    >>> pyautogui.hotkey('ctrl', 'c')
'''