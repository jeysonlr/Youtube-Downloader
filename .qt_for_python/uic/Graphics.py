# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Windows\Documents\GitHub\Youtube-Downloader\Graphics.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(592, 321)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_top = QtWidgets.QLabel(self.centralwidget)
        self.label_top.setGeometry(QtCore.QRect(130, 10, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_top.setFont(font)
        self.label_top.setAlignment(QtCore.Qt.AlignCenter)
        self.label_top.setObjectName("label_top")
        self.button_download = QtWidgets.QPushButton(self.centralwidget)
        self.button_download.setGeometry(QtCore.QRect(240, 170, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.button_download.setFont(font)
        self.button_download.setObjectName("button_download")
        self.check_video = QtWidgets.QCheckBox(self.centralwidget)
        self.check_video.setGeometry(QtCore.QRect(390, 190, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.check_video.setFont(font)
        self.check_video.setObjectName("check_video")
        self.input_url = QtWidgets.QLineEdit(self.centralwidget)
        self.input_url.setGeometry(QtCore.QRect(20, 60, 551, 41))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(10)
        self.input_url.setFont(font)
        self.input_url.setInputMask("")
        self.input_url.setText("")
        self.input_url.setAlignment(QtCore.Qt.AlignCenter)
        self.input_url.setObjectName("input_url")
        self.button_set = QtWidgets.QPushButton(self.centralwidget)
        self.button_set.setGeometry(QtCore.QRect(500, 110, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.button_set.setFont(font)
        self.button_set.setObjectName("button_set")
        self.input_path = QtWidgets.QLineEdit(self.centralwidget)
        self.input_path.setGeometry(QtCore.QRect(20, 110, 471, 41))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(10)
        self.input_path.setFont(font)
        self.input_path.setText("")
        self.input_path.setAlignment(QtCore.Qt.AlignCenter)
        self.input_path.setObjectName("input_path")
        self.radio_single = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_single.setGeometry(QtCore.QRect(390, 160, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.radio_single.setFont(font)
        self.radio_single.setObjectName("radio_single")
        self.radio_playlist = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_playlist.setGeometry(QtCore.QRect(470, 160, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.radio_playlist.setFont(font)
        self.radio_playlist.setObjectName("radio_playlist")
        self.label_done = QtWidgets.QLabel(self.centralwidget)
        self.label_done.setGeometry(QtCore.QRect(20, 240, 551, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_done.setFont(font)
        self.label_done.setText("")
        self.label_done.setAlignment(QtCore.Qt.AlignCenter)
        self.label_done.setObjectName("label_done")
        self.combo_quality = QtWidgets.QComboBox(self.centralwidget)
        self.combo_quality.setGeometry(QtCore.QRect(90, 190, 69, 22))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.combo_quality.setFont(font)
        self.combo_quality.setObjectName("combo_quality")
        self.combo_quality.addItem("")
        self.combo_quality.addItem("")
        self.combo_quality.addItem("")
        self.label_quality = QtWidgets.QLabel(self.centralwidget)
        self.label_quality.setGeometry(QtCore.QRect(50, 160, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_quality.setFont(font)
        self.label_quality.setAlignment(QtCore.Qt.AlignCenter)
        self.label_quality.setObjectName("label_quality")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 592, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_top.setText(_translate("MainWindow", "Youtube Downloader"))
        self.button_download.setText(_translate("MainWindow", "Download"))
        self.check_video.setText(_translate("MainWindow", "Download Video"))
        self.input_url.setPlaceholderText(_translate("MainWindow", "Paste URL Here..."))
        self.button_set.setText(_translate("MainWindow", "Set"))
        self.radio_single.setText(_translate("MainWindow", "Single"))
        self.radio_playlist.setText(_translate("MainWindow", "Playlist"))
        self.combo_quality.setItemText(0, _translate("MainWindow", "Best"))
        self.combo_quality.setItemText(1, _translate("MainWindow", "Semi"))
        self.combo_quality.setItemText(2, _translate("MainWindow", "Worst"))
        self.label_quality.setText(_translate("MainWindow", "Download Quality:"))
