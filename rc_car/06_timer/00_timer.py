import mysql.connector
from threading import Timer
from time import sleep


def polling():
    print("HI")

    timer = Timer(2, polling)
    timer.start()


polling()

while True:
    pass
