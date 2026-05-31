import keyboard
import pyautogui
import time
import threading

# Place any ranged weapon on slot 8 then press f4 to start and esc to end macro
#If you want to choose any other slot then just press f2 on the weapon and f3 on the unload button

position1 = pyautogui.Point(x=1267, y=1003)
position2 = pyautogui.Point(x=1349, y=944)
running = False

##
def save_position1():
     global position1
     position1 = pyautogui.position()
     print(f"Position 1 saved: {position1}")

def save_position2():
     global position2
     position2 = pyautogui.position()
     print(f"Position 2 saved: {position2}")

def macro_loop():
    global running
    while running:
        if position1 is None or position2 is None:
            print("First save possitions")
            running = False
            break

        # TAB
        pyautogui.press('tab')
        time.sleep(0.1)

        # Pozycja 1 + PPM
        pyautogui.moveTo(position1.x, position1.y, duration=0.1)
        pyautogui.click(button='right')
        time.sleep(0.1)

        # Pozycja 2 + LPM
        pyautogui.moveTo(position2.x, position2.y, duration=0.1)
        pyautogui.click(button='left')
        time.sleep(0.1)

        # TAB
        pyautogui.press('tab')
        time.sleep(0.1)

        # R
        pyautogui.press('r')

        # Czekanie
        time.sleep(4)

def toggle_macro():
    global running
    running = not running

    if running:
        print("Macro turned on")
        thread = threading.Thread(target=macro_loop)
        thread.daemon = True
        thread.start()
    else:
        print("Macro Turned off")

# Hotkeye
keyboard.add_hotkey('f4', toggle_macro)
keyboard.add_hotkey('f2', save_position1)
keyboard.add_hotkey('f3', save_position2)

print("F2 = save weapon position 1")
print("F3 = save weapon position 2")
print("F4 = start / stop macro")
print("ESC = exit")

keyboard.wait('esc')