#chp3_8
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import *
from gpiozero import *

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("QDial.ui",self)
        self.main()
        self.led1 = PWMLED(15)
        self.led2 = PWMLED(18)
        self.ledOff()
        
        self.btn = Button(24)
        self.btn.when_pressed = self.pressed

    def main(self):
        pass

    def ledOn(self):
        print("ON")
        self.led1.value = 1
        self.led2.value = 1

    def ledOff(self):
        print("OFF")
        self.led1.value = 0
        self.led2.value = 0

    def closeEvent(self,e):
        self.led1.close()
        self.led2.close()

    def setDial(self,value):
        print(value)
        self.led1.value = value/100
        self.led2.value = (100 - value)/100
        self.lcdNumber.display(value)

    def pressed(self):
        num = self.led1.value *100
        self.setDial(100-num)

app = QApplication([])
win = MyApp()
win.show()
app.exec()