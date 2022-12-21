import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog,QWidget

import fuc
from fuc import *

widgets = {
    "mainWindow": [],
    "logo": [],
    "btn_browse": [],
    "fucWindow": [],
    "logo2": [],
    "generate": [],
    "images": [],
    "bookmarks": [],
    "keywords": [],
    "back": [],
    "textWindow":[],
    "btn_saveas":[]
}

def clear_widgets():
    ''' hide all existing widgets and erase
        them from the global dictionary'''
    for widget in widgets:
        if widgets[widget] != []:
            widgets[widget][-1].hide()
        for i in range(0, len(widgets[widget])):
            widgets[widget].pop()

def show_funWindow():
    clear_widgets()
    fucWindow = QtWidgets.QWidget()
    ui = Ui_fucWindow()
    ui.setupUi(fucWindow)
    fucWindow.show()



def show_textWindow():
    printKeywords, printAbstract = fuc.pdfKeywords('D:/nj/paper/03.pdf')
    clear_widgets()
    textWindow = QtWidgets.QWidget()
    ui = Ui_textWindow()
    ui.setupUi(textWindow)
    ui.text_keywords.appendPlainText(printKeywords)
    ui.text_abstract.appendPlainText(printAbstract)
    textWindow.show()


class Ui_mainWindow(QWidget):

    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
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
        self.btn_browse.setText(_translate("mainWindow", "Browse"))
        self.btn_browse.clicked.connect(self.filedialog)
        widgets["mainWindow"].append(mainWindow)
        widgets["logo"].append(self.logo)
        widgets["btn_browse"].append(self.btn_browse)

    def filedialog(self):
        selected_file = QFileDialog.getOpenFileName(self, "Select a PDF File",
                                                    "./",
                                                    "All Files (*);;PDF Files (*.pdf)")  # 设置文件扩展名过滤,注意用双分号间隔
        print(selected_file[0])
        show_funWindow()
        return selected_file[0]


class Ui_fucWindow(QWidget):
    def setupUi(self, fucWindow):
        fucWindow.setObjectName("fucWindow")
        fucWindow.resize(482, 471)
        fucWindow.setStyleSheet("QWidget{\n"
"background-color:\"#ead9ff\"\n"
"\n"
"}\n"
"QPushButton{\n"
"background-color:\"#ff52ae\"\n"
"\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(fucWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 94, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.logo2 = QtWidgets.QLabel(fucWindow)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.logo2.setFont(font)
        self.logo2.setObjectName("logo2")
        self.horizontalLayout_2.addWidget(self.logo2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 94, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.generate = QtWidgets.QPushButton(fucWindow)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.generate.setFont(font)
        self.generate.setObjectName("generate")
        self.gridLayout.addWidget(self.generate, 1, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 0, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 1, 4, 1, 1)
        self.images = QtWidgets.QPushButton(fucWindow)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.images.setFont(font)
        self.images.setObjectName("images")
        self.gridLayout.addWidget(self.images, 0, 3, 1, 1)
        self.bookmarks = QtWidgets.QPushButton(fucWindow)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.bookmarks.setFont(font)
        self.bookmarks.setObjectName("bookmarks")
        self.gridLayout.addWidget(self.bookmarks, 1, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 1, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 0, 4, 1, 1)
        self.keywords = QtWidgets.QPushButton(fucWindow)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.keywords.setFont(font)
        self.keywords.setObjectName("keywords")
        self.gridLayout.addWidget(self.keywords, 0, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem10 = QtWidgets.QSpacerItem(461, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem10)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.back = QtWidgets.QPushButton(fucWindow)
        self.back.setObjectName("back")
        self.horizontalLayout.addWidget(self.back)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem11)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(fucWindow)
        QtCore.QMetaObject.connectSlotsByName(fucWindow)

    def retranslateUi(self, fucWindow):
        _translate = QtCore.QCoreApplication.translate
        fucWindow.setWindowTitle(_translate("fucWindow", "Paper Manager"))
        self.logo2.setText(_translate("fucWindow", "logo2"))
        self.generate.setText(_translate("fucWindow", "Generate"))
        self.images.setText(_translate("fucWindow", "Images"))
        self.bookmarks.setText(_translate("fucWindow", "Bookmark"))
        self.keywords.setText(_translate("fucWindow", "Keywords"))
        self.keywords.clicked.connect(show_textWindow)
        self.back.setText(_translate("fucWindow", "back"))
        widgets["fucWindow"].append(fucWindow)
        widgets["logo2"].append(self.logo2)
        widgets["generate"].append(self.generate)
        widgets["images"].append(self.images)
        widgets["bookmarks"].append(self.bookmarks)
        widgets["keywords"].append(self.keywords)
        widgets["back"].append(self.back)

class Ui_textWindow(QWidget):
    def setupUi(self, textWindow):
        textWindow.setObjectName("textWindow")
        textWindow.resize(745, 557)
        self.verticalLayout = QtWidgets.QVBoxLayout(textWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 96, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.text_abstract = QtWidgets.QPlainTextEdit(textWindow)
        self.text_abstract.setObjectName("text_abstract")
        self.horizontalLayout_2.addWidget(self.text_abstract)
        self.text_keywords = QtWidgets.QPlainTextEdit(textWindow)
        self.text_keywords.setObjectName("text_keywords")
        self.horizontalLayout_2.addWidget(self.text_keywords)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 95, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(448, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.btn_saveas = QtWidgets.QPushButton(textWindow)
        self.btn_saveas.setObjectName("btn_saveas")
        self.horizontalLayout.addWidget(self.btn_saveas)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 96, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)

        self.retranslateUi(textWindow)
        QtCore.QMetaObject.connectSlotsByName(textWindow)

    def retranslateUi(self, textWindow):
        _translate = QtCore.QCoreApplication.translate
        textWindow.setWindowTitle(_translate("textWindow", "Paper Manager: abstract"))
        self.btn_saveas.setText(_translate("textWindow", "Save PDF as"))
        widgets["textWindow"].append(textWindow)
        widgets["btn_saveas"].append(self.btn_saveas)
