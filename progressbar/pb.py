
#chp1_2_QTimer_and_ProgressBar.py
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import *

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("pb.ui",self)
        self.main()

    def main(self):
        self.pb.setValue(0)
        self.timer = QTimer()
        self.timer.setInterval(30)
        self.timer.timeout.connect(self.run)

    def run(self):
        print(self.pb.value())
        if self.pb.value() == 100:
            self.timer.stop()
        self.pb.setValue(self.pb.value() + 1)

    def go(self):
        if self.timer.isActive() == False:
            self.timer.start()

    def pause(self):
        if self.timer.isActive() == True:
            self.timer.stop()

    def stop(self):
        self.timer.stop()
        self.pb.setValue(0)

app = QApplication([]) 
win = MyApp()
win.show()
app.exec()
