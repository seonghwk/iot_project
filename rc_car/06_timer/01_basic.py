import mysql.connector
from threading import Timer
from time import sleep
import signal
import sys

def closeDB(signal, frame):
    print("BYE")
    timer.cancel()
    sys.exit(0)

def polling():
    print("HI")   
    global timer
    timer = Timer(2, polling)
    timer.start()

timer = None
signal.signal(signal.SIGINT, closeDB)
polling()

while True: 
    print("KFC MAIN")
    sleep(0.5)
    pass
