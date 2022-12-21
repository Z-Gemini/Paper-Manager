import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog,QWidget


widgets = {
            "mainWindow":[],
            "logo": [],
            "btn_browse": []
          }

def clear_widgets():
    ''' hide all existing widgets and erase
        them from the global dictionary'''
    for widget in widgets:
        if widgets[widget] != []:
            widgets[widget][-1].hide()
        for i in range(0, len(widgets[widget])):
            widgets[widget].pop()

class Ui_mainWindow(QWidget):

    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        widgets["mainWindow"].append(mainWindow)

        mainWindow.resize(395, 431)
        mainWindow.setStyleSheet("QWidget{\n"
"background-color:\"#ead9ff\"\n"
"}\n"
"QPushButton{\n"
"background-color:\"#ff52ae\"\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(mainWindow)
        self.verticalLayout.setObjectName("verticalLayout")

        spacerItem = QtWidgets.QSpacerItem(20, 118, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.logo = QtWidgets.QLabel(mainWindow)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.logo.setFont(font)
        self.logo.setObjectName("logo")
        widgets["logo"].append(self.logo)

        self.horizontalLayout.addWidget(self.logo)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 117, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.btn_browse = QtWidgets.QPushButton(mainWindow)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_browse.setFont(font)
        self.btn_browse.setObjectName("btn_browse")
        widgets["btn_browse"].append(self.btn_browse)

        self.btn_browse.clicked.connect(self.filedialog)

        self.horizontalLayout_2.addWidget(self.btn_browse)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Paper Manager"))
        self.logo.setText(_translate("mainWindow", "logo"))
        self.btn_browse.setText(_translate("mainWindow", "Broese"))


    def filedialog(self):
        selected_file = QFileDialog.getOpenFileName(self,
                                                          "Select a PDF File",
                                                          "./",
                                                          "All Files (*);;PDF Files (*.pdf)")  # 设置文件扩展名过滤,注意用双分号间隔

        return selected_file



