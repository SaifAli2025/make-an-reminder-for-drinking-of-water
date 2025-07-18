import os 
import time
import pyttsx3
import threading
def background_os_task():
    os.system("echo os Task Executed")
    threading.Timer(10,background_os_task).start()
    background_os_task()
    input("press Enter to stop..........n")

def repeat_task():
    while True:
        engine=pyttsx3.init()
        engine.setProperty("rate",150)
        engine.say(" syef Ali it's time to drink water go now")
        engine.runAndWait()
        time.sleep(7200)
repeat_task()
