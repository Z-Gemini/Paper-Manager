from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import os
import sys


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 450)
        Form.setStyleSheet("")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(200, 320, 200, 50))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.open_file)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Paper Organizor"))
        self.pushButton.setText(_translate("Form", "Browse"))

    def open_file(self):
        file_name = QFileDialog.getOpenFileName(self, 'open file', '.')
        f_name = file_name[0]
        print(f_name)


app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()
sys.exit(app.exec_())
