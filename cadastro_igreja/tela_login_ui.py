# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_login.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)
import xcz_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(395, 495)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 85, 127);\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(140, 360, 111, 41))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.pushButton.setFont(font1)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: rgb(130, 129, 131);")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 60, 81, 41))
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color: rgb(0, 170, 0);")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 460, 161, 31))
        font3 = QFont()
        font3.setPointSize(9)
        font3.setBold(True)
        self.label_4.setFont(font3)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(260, 470, 131, 28))
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(130, 129, 131);")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(70, 320, 241, 31))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(60, 130, 261, 181))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"")
        self.label_2.setPixmap(QPixmap(u"../../../Downloads/usuario.png"))
        self.label_2.setScaledContents(True)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setPixmap(QPixmap(u"../../../Downloads/cadeado.png"))
        self.label_3.setScaledContents(True)

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(-10, 0, 91, 71))
        self.label_6.setPixmap(QPixmap(u"../../../Downloads/icon.png"))
        self.label_6.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(qtTrId(u""))
        self.pushButton.setText(qtTrId(u""))
        self.label.setText(qtTrId(u""))
        self.label_4.setText(qtTrId(u""))
        self.pushButton_2.setText(qtTrId(u""))
        self.label_5.setText("")
        self.label_2.setText("")
        self.lineEdit.setText("")
        self.label_3.setText("")
        self.label_6.setText("")
    # retranslateUi

