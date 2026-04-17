import pyautogui
import time

print("Starting mouse movement. Press Ctrl+C to stop.")

try:
    while True:
        x, y = pyautogui.position()
        pyautogui.moveTo(x + 1, y + 1, duration=0.1)
        pyautogui.moveTo(x, y, duration=0.1)
        time.sleep(5)

except KeyboardInterrupt:
    print("\nMouse movement stopped.")
