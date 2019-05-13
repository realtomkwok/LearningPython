from PyQt5 import QtWidgets
import Ui_textEditor

class mainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_textEditor.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Text Editor')
        self.resize(500,400)
        
        newButton = self.ui.actionNew
        newButton.setShortcut("Ctrl+N")
        newButton.triggered.connect(self.newFile)

        openButton = self.ui.actionOpen
        openButton.setShortcut('Ctrl+O')
        openButton.triggered.connect(self.openFile)

        saveButton = self.ui.actionSave
        saveButton.setShortcut('Ctrl+S')
        saveButton.triggered.connect(self.saveFile)
        
        exitButton = self.ui.actionExit
        exitButton.setShortcut("Ctrl+W")
        exitButton.triggered.connect(self.close)

        self.show()

    def newFile(self):
        self.w = mainWindow()
        self.w.show()
    
    # will crush the program and idk
    def openFile(self):
        self.filename = QtWidgets.QFileDialog.getOpenFileName(self)
    
        if self.filename:
            with open(self.filename,"rt") as file:
                self.ui.textEdit.toPlainText(file.read())

    def saveFile(self):
        if not self.filename:
            self.filename = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File')
        if not self.filename.endswith(".writer"):
            self.filename += ".writer"
        with open(self.filename,"wt") as file:
            file.write(self.text.toHtml())

app = QtWidgets.QApplication([])
win = mainWindow()
win.show

app.exec()