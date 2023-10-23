# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(375, 500)
        MainWindow.setMinimumSize(QSize(375, 500))
        MainWindow.setMaximumSize(QSize(375, 500))
        MainWindow.setSizeIncrement(QSize(375, 500))
        MainWindow.setBaseSize(QSize(375, 500))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lblFondoLogin = QLabel(self.centralwidget)
        self.lblFondoLogin.setObjectName(u"lblFondoLogin")
        self.lblFondoLogin.setGeometry(QRect(0, 0, 381, 481))
        self.lblFondoLogin.setPixmap(QPixmap(u"../../../../../Downloads/Recursos/Fondos/f3.jpg"))
        self.lblFondoLogin.setScaledContents(True)
        self.lblFondoLogin.setMargin(0)
        self.lblTituloDeLogin = QLabel(self.centralwidget)
        self.lblTituloDeLogin.setObjectName(u"lblTituloDeLogin")
        self.lblTituloDeLogin.setGeometry(QRect(60, 60, 271, 41))
        self.lblTituloDeLogin.setStyleSheet(u"font: 900 20pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")
        self.lblLogoUsuario = QLabel(self.centralwidget)
        self.lblLogoUsuario.setObjectName(u"lblLogoUsuario")
        self.lblLogoUsuario.setGeometry(QRect(130, 120, 111, 101))
        self.lblLogoUsuario.setPixmap(QPixmap(u"../../../../../Downloads/usuario.png"))
        self.lblLogoUsuario.setScaledContents(True)
        self.txtLoginUsuario = QTextEdit(self.centralwidget)
        self.txtLoginUsuario.setObjectName(u"txtLoginUsuario")
        self.txtLoginUsuario.setGeometry(QRect(60, 260, 271, 31))
        self.txtLoginUsuario.setStyleSheet(u"border: 520px;\n"
"\n"
"")
        self.txtLoginContrasenia = QTextEdit(self.centralwidget)
        self.txtLoginContrasenia.setObjectName(u"txtLoginContrasenia")
        self.txtLoginContrasenia.setGeometry(QRect(60, 330, 271, 31))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 230, 91, 16))
        self.label.setStyleSheet(u"font: 900 15pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 300, 131, 16))
        self.label_2.setStyleSheet(u"font: 900 15pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(150, 390, 80, 24))
        self.pushButton.setStyleSheet(u"font: 900 10pt \"Arial Black\";\n"
"color: rgb(0, 0, 0);")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(150, 450, 91, 20))
        self.label_3.setStyleSheet(u"font: 8pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 375, 21))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lblFondoLogin.setText("")
        self.lblTituloDeLogin.setText(QCoreApplication.translate("MainWindow", u"INICIO DE SESI\u00d3N", None))
        self.lblLogoUsuario.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Chambo-Ecuador", None))
    # retranslateUi

