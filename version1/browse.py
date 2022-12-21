
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog,QWidget
from QCandyUi import CandyWindow

class Main_window(QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 450)
        Form.setStyleSheet("")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(200, 320, 200, 50))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.filedialog)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Paper Organizor"))
        self.pushButton.setText(_translate("Form", "Browse"))

    def filedialog(self):
        selected_file = QFileDialog.getOpenFileName(self,
                                                          "选取文件",
                                                          "./",
                                                          "All Files (*);;PDF Files (*.pdf)")  # 设置文件扩展名过滤,注意用双分号间隔
        return selected_file

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    Form = CandyWindow.createWindow(Form, 'blueDeep')
    ui = Main_window()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
