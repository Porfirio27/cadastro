# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'primeira_tela.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)
import xcz_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(395, 509)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(157, 149, 155);\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(130, 360, 111, 41))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(100, 169, 181, 24))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(100, 242, 181, 24))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 50, 241, 41))
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        self.label.setFont(font2)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 170, 24, 24))
        self.label_2.setStyleSheet(u"")
        self.label_2.setPixmap(QPixmap(u"usuario.png"))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 230, 32, 32))
        self.label_3.setPixmap(QPixmap(u"cadeado.png"))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 470, 161, 31))
        font3 = QFont()
        font3.setPointSize(9)
        font3.setBold(True)
        self.label_4.setFont(font3)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(260, 470, 131, 28))
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"background-color: rgb(0, 0, 127);")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(110, 280, 141, 31))
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color: rgb(170, 0, 0);")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.lineEdit.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"TELA DE LOGIN", None))
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o \u00e8 cadastrado?", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR", None))
        self.label_5.setText("")
    # retranslateUi

