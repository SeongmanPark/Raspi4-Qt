from PyQt5.QtWidgets import *
from PyQt5.QtGui import QKeySequence

class MainWindow(QMainWindow):
    def closeEvent(self, e):
        if not text.document().isModified():
            return
        answer = QMessageBox.question(window, None, "SAVE or NOT",
                                      QMessageBox.Save |
                                      QMessageBox.Discard |
                                      QMessageBox.Cancel
                                      )
        if answer & QMessage.Save:
            save()
        elif answer & QMessageBox.Cancel:
            e.ignore()

app = QApplication([])
app.setApplicationName("MINCODING")
text = QPlainTextEdit()

window = MainWindow()
window.setCentralWidget(text)
menu = window.menuBar().addMenu("&File")

open_action = QAction("&Open")
def open_file():
    path = QFileDialog.getOpenFileName(window, "Open File")[0]
    if path:
        text.setPlainText(open(path).read())
open_action.triggered.connect(open_file)
open_action.setShortcut(QKeySequence("Ctrl+O"))
menu.addAction(open_action)


file_path = None
save_action = QAction("&Save")
def save():
    if file_path is None:
        save_as()
    else:
        with open(file_path, "w") as f:
            f.write(text.toPlainText())
        text.document().setModified(False)
            
save_action.triggered.connect(save)
save_action.setShortcut(QKeySequence("Ctrl+S"))
menu.addAction(save_action)

save_as_action = QAction("Save &As...")
def save_as():
    global file_path
    path = QFileDialog.getSaveFileName(window, "Save As")[0]
    if path:
        file_path = path
        save()
            
save_as_action.triggered.connect(save_as)
menu.addAction(save_as_action)

close = QAction("&Close")
close.triggered.connect(window.close)
menu.addAction(close)

help_menu = window.menuBar().addMenu("&Help")
about_action = QAction("&About")
help_menu.addAction(about_action)

def show_about_dialog():
    text = "<center>" \
           "<h1>Text Editor</h1>" \
           "</center>" \
           "<p>Version 1.2.3<br>" \
           "Copyright Mincoding</p>"
    QMessageBox.about(window, "About", text)
    
about_action.triggered.connect(show_about_dialog)


window.show()
text.show()
app.exec()
