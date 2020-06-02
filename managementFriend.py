from PyQt5.QtWidgets import *

app = QApplication([])
win = QMainWindow()

app.setApplicationName("My Frineds")
win.resize(400, 400)
bar = win.statusBar()
bar.showMessage("make Friends !!!")

mb = win.menuBar()
menu = mb.addMenu("menu")

menuAdd = QAction("append", win)
menuRemove = QAction("remove", win)
bye = QAction("exit", win)

menu.addAction(menuAdd)
menu.addAction(menuRemove)
mb.addAction(bye)

main = QWidget()
win.setCentralWidget(main)

addBtn = QPushButton("append")
removeBtn = QPushButton("remove")
btnLayout = QHBoxLayout()
btnLayout.addWidget(addBtn)
btnLayout.addWidget(removeBtn)

form = QFormLayout()
name = QLineEdit()
form.addWidget(QLabel("make Friend !!!"))
form.addRow("name", name)
form.addRow(btnLayout)

main.setLayout(form)

def add():
    str = name.text()
    if len(str) == 0 : return
    
    global names
    if names.count(str) == 1:
        bar.showMessage("already friend")
    else:
        bar.showMessage("welcome my new friend")
        names.append(str)
        print(names)

def remove():
    str = name.text()
    if len(str) == 0 : return
    
    global names
    if names.count(str) == 0:
        bar.showMessage(str + ", not my friend")
    else:
        bar.showMessage(str + ", not my friend more")
        names.remove(str)
        print(names)
    
def byebye():
    quit()

names = ["inho", "donghun", "carrot", "seongman"]

addBtn.clicked.connect(add)
removeBtn.clicked.connect(remove)

menuAdd.triggered.connect(add)
menuRemove.triggered.connect(remove)
bye.triggered.connect(byebye)

win.show()
app.exec()



