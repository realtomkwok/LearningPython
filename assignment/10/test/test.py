from PyQt5 import QtWidgets 
# PyQt5 uses QtWidgets instead of QtGui
import Ui_test

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_test.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.buttonClicked)
        self.show()

    def buttonClicked(self):
        height = float(self.ui.lineEdit.text())
        weight = float(self.ui.lineEdit_2.text())
        bmi = weight / (height ** 2)
        self.ui.label_3.setText(str(bmi))

app = QtWidgets.QApplication([])
win = MyWindow()
win.show()
app.exec()