# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionWord_PDF = QtWidgets.QAction(MainWindow)
        self.actionWord_PDF.setObjectName("actionWord_PDF")
        self.action_Word = QtWidgets.QAction(MainWindow)
        self.action_Word.setObjectName("action_Word")
        self.action_list = QtWidgets.QAction(MainWindow)
        self.action_list.setObjectName("action_list")
        self.toolBar.addAction(self.actionWord_PDF)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_Word)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_list)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionWord_PDF.setText(_translate("MainWindow", "Word转PDF"))
        self.actionWord_PDF.setToolTip(_translate("MainWindow", "<html><head/><body><p>这里为“Word转PDF”</p></body></html>"))
        self.action_Word.setText(_translate("MainWindow", "统计Word文档页码"))
        self.action_Word.setToolTip(_translate("MainWindow", "统计Word文档页码"))
        self.action_list.setText(_translate("MainWindow", "提取总目录"))
        self.action_list.setToolTip(_translate("MainWindow", "提取总目录"))
