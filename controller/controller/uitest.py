from PySide2.QtWidgets import *
from PySide2.QtCore import *
from mainUI import Ui_MainWindow
import mysql.connector

class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init()

    def init(self):
        pass
        # self.db = mysql.connector.connect(host='52.78.179.144', user='seonghwk', password='1234', database='minDB', auth_plugin='mysql_native_password')
        # self.cur = self.db.cursor()

        # #timer setting
        # self.timer = QTimer()
        # self.timer.setInterval(500) #500ms
        # self.timer.timeout.connect(self.pollingQuery)

    def start(self):
        pass
        #self.timer.start()

    def pollingQuery(self):
        pass
        # #query
        # self.cur.execute("select * from command order by time desc limit 15")
        # self.ui.logText.clear()

        # #print
        # for (id, time, cmd_string, arg_string, is_finish) in self.cur:
        #     str = "%3d | %s | %6s | %6s | %4d" % (id, time.strftime("%Y%m%d %H:%M:%S"), cmd_string, arg_string, is_finish)
        #     self.ui.logText.appendPlainText(str)

        # self.cur.execute("select * from sensing order by time desc limit 15")
        # self.ui.sensingText.clear()
        # for (id, time, num1, num2, num3, meta_string, is_finish) in self.cur:
        #     str = "%3d | %s | %6s | %6s | %6s | %10s | %4d" % (id, time.strftime("%Y%m%d %H:%M:%S"), num1, num2, num3, meta_string, is_finish)
        #     self.ui.sensingText.appendPlainText(str)
        # self.db.commit()

    def closeEvent(self, event):
        pass
        # self.cur.close()
        # self.db.close()

    def insertCommand(self, cmd_string, arg_string):
        pass
        # time = QDateTime().currentDateTime().toPython()
        # is_finish = 0

        # query = "insert into command(time, cmd_string, arg_string, is_finish) values (%s, %s, %s, %s)"
        # value = (time, cmd_string, arg_string, is_finish)

        # self.cur.execute(query, value)
        # self.db.commit()

    def go(self):
        pass
        #self.insertCommand("go", "0")

    def stop(self):
        pass
        #self.insertCommand("stop", "0")

    def back(self):
        pass
        #self.insertCommand("back", "0")

    def left(self):
        pass
        #self.insertCommand("left", "0")

    def mid(self):
        pass
        #self.insertCommand("mid", "0")

    def right(self):
        pass
        #self.insertCommand("right", "0")

app = QApplication()
win = MyApp()
win.show()
app.exec_()
