# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Mar 27 2023, 01:51:45) 
# [GCC 12.2.1 20220924]
# Embedded file name: passwordGenerator.py
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
import pyperclip

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName('MainWindow')
        MainWindow.resize(560, 408)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName('centralwidget')
        self.title = QTextBrowser(self.centralwidget)
        self.title.setObjectName('title')
        self.title.setGeometry(QRect(80, 10, 411, 51))
        self.textBrowser_2 = QTextBrowser(self.centralwidget)
        self.textBrowser_2.setObjectName('textBrowser_2')
        self.textBrowser_2.setGeometry(QRect(10, 80, 161, 41))
        self.generate = QPushButton(self.centralwidget)
        self.generate.setObjectName('generate')
        self.generate.setGeometry(QRect(140, 330, 261, 51))
        self.PasswordLength = QSpinBox(self.centralwidget)
        self.PasswordLength.setObjectName('PasswordLength')
        self.PasswordLength.setGeometry(QRect(30, 130, 101, 21))
        self.PasswordLength.setMinimum(10)
        self.PasswordLength.setMaximum(40)
        self.copyButton = QPushButton(self.centralwidget)
        self.copyButton.setObjectName('copyButton')
        self.copyButton.setGeometry(QRect(460, 260, 71, 61))
        self.textBrowser_4 = QTextBrowser(self.centralwidget)
        self.textBrowser_4.setObjectName('textBrowser_4')
        self.textBrowser_4.setGeometry(QRect(190, 170, 141, 41))
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName('checkBox')
        self.checkBox.setGeometry(QRect(250, 220, 16, 17))
        self.checkBox.setCheckable(True)
        self.checkBox.setChecked(False)
        self.checkBox.setTristate(False)
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem('')
        self.comboBox.addItem('')
        self.comboBox.addItem('')
        self.comboBox.setObjectName('comboBox')
        self.comboBox.setGeometry(QRect(350, 130, 161, 21))
        self.textBrowser_5 = QTextBrowser(self.centralwidget)
        self.textBrowser_5.setObjectName('textBrowser_5')
        self.textBrowser_5.setGeometry(QRect(360, 80, 131, 41))
        self.password_field = QLineEdit(self.centralwidget)
        self.password_field.setObjectName('password_field')
        self.password_field.setGeometry(QRect(100, 260, 351, 61))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName('statusbar')
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate('MainWindow', 'MainWindow', None))
        self.title.setDocumentTitle('')
        self.title.setHtml(QCoreApplication.translate('MainWindow', '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n<html><head><meta name="qrichtext" content="1" /><style type="text/css">\np, li { white-space: pre-wrap; }\n</style></head><body style=" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;">\n<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:20pt;">Secure Password Generator</span></p></body></html>', None))
        self.textBrowser_2.setDocumentTitle('')
        self.textBrowser_2.setHtml(QCoreApplication.translate('MainWindow', '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n<html><head><meta name="qrichtext" content="1" /><style type="text/css">\np, li { white-space: pre-wrap; }\n</style></head><body style=" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;">\n<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt;">Password Length</span></p></body></html>', None))
        self.generate.setText(QCoreApplication.translate('MainWindow', 'Generate!', None))
        self.copyButton.setText(QCoreApplication.translate('MainWindow', 'Copy', None))
        self.textBrowser_4.setDocumentTitle('')
        self.textBrowser_4.setHtml(QCoreApplication.translate('MainWindow', '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n<html><head><meta name="qrichtext" content="1" /><style type="text/css">\np, li { white-space: pre-wrap; }\n</style></head><body style=" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;">\n<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt;">Hide Password</span></p></body></html>', None))
        self.checkBox.setText('')
        self.comboBox.setItemText(0, QCoreApplication.translate('MainWindow', 'All Characters', None))
        self.comboBox.setItemText(1, QCoreApplication.translate('MainWindow', 'Alphabetic', None))
        self.comboBox.setItemText(2, QCoreApplication.translate('MainWindow', 'Alphanumeric', None))
        self.textBrowser_5.setDocumentTitle('')
        self.textBrowser_5.setHtml(QCoreApplication.translate('MainWindow', '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n<html><head><meta name="qrichtext" content="1" /><style type="text/css">\np, li { white-space: pre-wrap; }\n</style></head><body style=" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;">\n<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:16pt;">characters</span></p></body></html>', None))
        self.password_field.setText('')


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setFixedSize(QSize(550, 400))
        self.setWindowTitle('Secure Password Generator')
        self.password_field.setReadOnly(True)
        self.passlen()
        self.chars()
        self.hide()
        self.gen()

    def passlen(self):
        self.PasswordLength.valueChanged.connect(self.lenpass)

    def lenpass(self, l):
        global value
        value = l

    def chars(self):
        self.comboBox.currentIndexChanged.connect(self.charss)

    def charss(self, i):
        global index
        index = i

    def hide(self):
        self.checkBox.stateChanged.connect(self.status)

    def status(self, s):
        global status
        status = s == Qt.Checked

    def copy(self):
        self.copyButton.clicked.connect(self.copied)

    def copied(self):
        pyperclip.copy(self.password_field.text())

    def gen(self):
        self.generate.clicked.connect(self.genButton)

    def genButton(self):
        try:
            hide = status
            if hide:
                self.password_field.setEchoMode(QLineEdit.Password)
            else:
                self.password_field.setEchoMode(QLineEdit.Normal)
            password = self.genPassword()
            self.password_field.setText(password)
        except:
            msg = QMessageBox()
            msg.setWindowTitle('Warning')
            msg.setText('Change the default values before generating passwords!')
            x = msg.exec_()

        self.copy()

    def genPassword(self):
        length = value
        char = index
        if char == 0:
            charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890~!@#$%^&*()_-+={}[]|:;<>,.?'
        else:
            if char == 1:
                charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
            else:
                if char == 2:
                    charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
                else:
                    try:
                        qsrand(QTime.currentTime().msec())
                        password = ''
                        for i in range(length):
                            idx = qrand() % len(charset)
                            nchar = charset[idx]
                            password += str(nchar)

                    except:
                        msg = QMessageBox()
                        msg.setWindowTitle('Error')
                        msg.setText('Error while generating password!, Send a message to the Author!')
                        x = msg.exec_()

                return password


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    mainwindow = MainWindow()
    mainwindow.show()
    app.exec_()
# okay decompiling passwordGenerator.pyc
