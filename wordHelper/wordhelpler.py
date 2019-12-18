'''
-*- coding: utf-8 -*-
@Author  : alex_jiang
@Time    : 2019/12/16 16:11
@Software: PyCharm
@File    : wordhelpler.py
'''
import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog,\
    QTableWidgetItem, QTableWidget, QMessageBox
import os
from mainWindow import *
from tools import common, wordtopdf, mergepdf
from transformWindow import *
import _thread


class MyMainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)
        self.setGeometry(100, 100, 1024, 600)
        self.setWindowTitle("Word助手")
        # 设置窗体背景
        palette = QPalette() # 创建调色板类对象
        # 设置窗体背景自适应
        palette.setBrush(self.backgroundRole(), QBrush(QPixmap("./image/bg.jpg").scaled(self.size(),
                                                                                    Qt.IgnoreAspectRatio, Qt.SmoothTransformation)))
        self.setPalette(palette)
        self.setAutoFillBackground(True)
        self.setFixedSize(1024, 600)


class TransformWindow(QMainWindow, Ui_TransformWindow):

    def __init__(self):
        super(TransformWindow, self).__init__()
        self.setupUi(self)
        self.showLoading.setText("")
        self.showLoading.setMinimumWidth(100)

        self.sourcebrowseButton.clicked.connect(self.sourcebrowseClick)
        self.targetbrowseButton.clicked.connect(self.targetbrowseClick)

    def open(self):
        self.__init__()
        self.show()

    def sourcebrowseClick(self):
        # 获取用户选择的文件夹
        dir_path = QFileDialog.getExistingDirectory(self, "请选择源文件目录", r"E:learn\test\doc")
        if not dir_path:
            return
        # 将获取的文件夹路径添加到文本框控件中
        self.sourcepath.setText(dir_path)
        self.listword.clear()
        global filelist
        filelist = common.getfilenames(dir_path, [], '.doc')
        self.listword.addItems(filelist)

    def targetbrowseClick(self):
        dir_path = QFileDialog.getExistingDirectory(self, "请选择目标文件目录", r"E\learn\test")
        self.targetpath.setText(dir_path)

    def multipleExecuteClick(self):
        # 判断是否选择了源文件，如果没有选择则弹出提示框告知
        if self.listword.count() == 0:
            QMessageBox.information(self, "温馨提示:", "没有要转换的Word文档！", QMessageBox.Yes)
            return
        targetpath = self.targetpath.text() # 获取目标文件夹
        # 判断是否选择了目标文件，如果没有选择则弹出提示框告知
        if not os.path.exists(targetpath):
            QMessageBox.information(self, "温馨提示: ", "请选择正确的目标路径!", QMessageBox.Yes)
        self.listpdf.clear()  # 清空列表结果
        self.showLoading.setMovie(self.gif) # 设置gif图片
        self.gif.start()
        _thread.start_new_thread(self.mExecute, ())

    def mExecute(self):
        targetpath = self.targetpath.text()
        valueList = wordtopdf.wordtopdf(filelist, targetpath)
        if valueList != -1:
            self.showLoading.clear()
            self.listpdf.addItems(valueList)

    def singleExecuteClick(self):
        # 判断是否选择了源文件
        if self.listword.count() == 0:
            QMessageBox.information(self, "温馨提示：", "没有要转换的Word文档！", QMessageBox.Yes)
            return
        # 判断是否选择了目标文件夹，如果没有选择则弹出提示框告知
        if not os.path.exists(self.targetpath.text()):
            QMessageBox.information(self, "温馨提示: ", "请选择正确的目标路径!", QMessageBox.Yes)
            return
        self.listpdf.clear() # 清空结果列表
        self.showLoading.setMovie(self.gif)
        self.gif.start()
        # 开启新线程执行多个Word合为一个PDF
        _thread.start_new_thread(self.sExecute, ())

    def sExecute(self):
        targetpath = self.targetpath.text() # 获取目标路径
        valueList = wordtopdf.wordtopdf(filelist, targetpath)
        if valueList != -1:
            # 将多个PDF文件合为一个PDF文件
            mergepdf.mergefiles(targetpath, 'merged.pdf', True)
            self.showLoading.clear()
            temp = [os.path.join(targetpath, 'merged.pdf')]
            self.listpdf.addItems(temp)
            for file in valueList:
                os.remove(file)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    qmovie = QtGui.QMovie("image/loding.gif")

    transforWindow = TransformWindow()
    transforWindow.gif = qmovie
    # 连接槽函数，打开转换窗口

    myWin.actionWord_PDF.triggered.connect(transforWindow.open)

    myWin.show()
    sys.exit(app.exec_())
