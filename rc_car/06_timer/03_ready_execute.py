import mysql.connector
from threading import Timer
from time import sleep
import signal
import sys

def closeDB(signal, frame):
    print("BYE")
    cur.close()
    db.close()
    timer.cancel()
    sys.exit(0)

def polling():
    global cur, db, ready
    
    cur.execute("select * from command order by time desc limit 1")
    for (id, time, cmd_string, arg_string, is_finish) in cur:
        if is_finish == 1 : break
        ready = (cmd_string, arg_string)
        cur.execute("update command set is_finish=1 where is_finish=0")

    db.commit()
     
    global timer
    timer = Timer(0.1, polling)
    timer.start()

def go():
    print("go")

def back():
    print("back")

def stop():
    print("stop")

def left():
    print("left")

def mid():
    print("mid")

def right():
    print("right")

#init
db = mysql.connector.connect(host='52.78.179.144', user='seonghwk', password='1234', database='minDB', auth_plugin='mysql_native_password')
cur = db.cursor()
ready = None
timer = None
signal.signal(signal.SIGINT, closeDB)
polling()

#main thread
while True:
    sleep(0.1)
    if ready == None : continue

    cmd, arg = ready
    ready = None

    if cmd == "go" : go()
    if cmd == "back" : back()
    if cmd == "stop" : stop()
    if cmd == "left" : left()
    if cmd == "mid" : mid()
    if cmd == "right" : right()
