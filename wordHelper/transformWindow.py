# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'transfermWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TransformWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(801, 648)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(60, 30, 721, 261))
        self.groupBox.setObjectName("groupBox")
        self.listword = QtWidgets.QListWidget(self.groupBox)
        self.listword.setGeometry(QtCore.QRect(20, 60, 681, 192))
        self.listword.setObjectName("listword")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(20, 30, 681, 22))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.sourcepath = QtWidgets.QLineEdit(self.widget)
        self.sourcepath.setObjectName("sourcepath")
        self.horizontalLayout.addWidget(self.sourcepath)
        self.sourcebrowseButton = QtWidgets.QToolButton(self.widget)
        self.sourcebrowseButton.setObjectName("sourcebrowseButton")
        self.horizontalLayout.addWidget(self.sourcebrowseButton)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(60, 300, 721, 261))
        self.groupBox_2.setObjectName("groupBox_2")
        self.listpdf = QtWidgets.QListWidget(self.groupBox_2)
        self.listpdf.setGeometry(QtCore.QRect(20, 60, 681, 192))
        self.listpdf.setObjectName("listpdf")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 30, 681, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.targetpath = QtWidgets.QLineEdit(self.layoutWidget)
        self.targetpath.setObjectName("targetpath")
        self.horizontalLayout_2.addWidget(self.targetpath)
        self.targetbrowseButton = QtWidgets.QToolButton(self.layoutWidget)
        self.targetbrowseButton.setObjectName("targetbrowseButton")
        self.horizontalLayout_2.addWidget(self.targetbrowseButton)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(60, 570, 721, 25))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.showLoading = QtWidgets.QLabel(self.widget1)
        self.showLoading.setObjectName("showLoding")
        self.horizontalLayout_3.addWidget(self.showLoading)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.singleExecute = QtWidgets.QPushButton(self.widget1)
        self.singleExecute.setObjectName("singleExecute")
        self.horizontalLayout_3.addWidget(self.singleExecute)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 23))
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
        self.groupBox.setTitle(_translate("MainWindow", "源"))
        self.label.setText(_translate("MainWindow", "请选择Word文档所在目录："))
        self.sourcebrowseButton.setText(_translate("MainWindow", "..."))
        self.groupBox_2.setTitle(_translate("MainWindow", "结果"))
        self.label_2.setText(_translate("MainWindow", "转换后PDF文档保存目录："))
        self.targetbrowseButton.setText(_translate("MainWindow", "..."))
        self.showLoading.setText(_translate("MainWindow", "转换进度"))
        self.singleExecute.setText(_translate("MainWindow", "合为一个PDF"))
        self.pushButton_2.setText(_translate("MainWindow", "批量转换"))
