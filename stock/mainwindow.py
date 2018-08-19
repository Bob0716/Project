# __author__:"Adolphus"
# project:'stock'
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os
import print_screen
class grab_thread(QThread):
    signal = pyqtSignal(int,str)
    def __init__(self,parent=None,geo=None,fre=None):
        super(grab_thread,self).__init__(parent)
        self.geo=geo
        self.fre=fre
    def run(self):
        print_screen.grab(self.geo,self.fre)
class labelBtn(QLabel):
    """
    自定义图片按钮类
    """
    def __init__(self, parent,id):
        super(labelBtn, self).__init__(parent=parent)
        self.setMouseTracking(True)
        self.id=id
    # def mouseReleaseEvent(self, event):  # 注:
    #     # 鼠标点击事件
    #
    def mouseDoubleClickEvent(self, event):
        print('heih')
        print(self.parent().geometry().x(),self.parent().geometry().y(),self.parent().geometry().height(),self.parent().geometry().width())
        geo=(self.parent().geometry().x(),self.parent().geometry().y(),self.parent().geometry().height(),self.parent().geometry().width())
        # print(geo[1])
        self.parent.h(geo)
# class frist(QMainWindow):
#     def __init__(self):
#         super(frist,self).__init__()
#         self.child=mainwindow(parent=self)
#         self.setCentralWidget(self.child)
#         self.setAttribute(Qt.WA_TranslucentBackground,True)
class mainwindow(QDialog):
    def __init__(self):
        super(mainwindow, self).__init__()
        self.cunr=False
        self.desktop = QDesktopWidget()
        #self.setWindowFlags(Qt.FramelessWindowHint)
        #self.setAttribute(Qt.WA_TranslucentBackground, True)
        #self.setAttribute(Qt.WA_NoSystemBackground,True)
        #self.setAutoFillBackground(True)
        #self.setStyleSheet("background-color:rgba(255, 255, 255, 190);")
        #self.pal=QPalette()
        #self.pal.setBrush(QPalette.Base, Qt.transparent)
        #self.setPalette(self.pal)
        #self.setAttribute(Qt.WA_TranslucentBackground,True)
        #self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowOpacity(0.5)
        self.setGeometry(100, 100, 100, 100)
        self.whole=QVBoxLayout()
        self.btn=labelBtn(self,1)
        #self.btn.setText('选取')
        self.btn=QPushButton('选取')
        self.whole.addWidget(self.btn)
        self.setLayout(self.whole)
        self.btn.clicked.connect(self.h)
        # geo = (self.geometry().x(), self.geometry().y(), self.geometry().height(),
        #        self.geometry().width())
        # print_screen.grab(geo)
        #self.geometry().height()
        # qp = QPainter()
        # qp.begin(self)
        # qp.setBrush(QColor(220, 220, 220))
        # qp.drawRect(0, 0, self.width() - 1, self.height() - 1)
    def h(self):
        # geo=tuple(geo)
        geo = (self.geometry().x(), self.geometry().y(), self.geometry().x()+self.geometry().width(),
               self.geometry().y()+self.geometry().height())
        #print(type(self.geometry().width()))
        print(geo)
        if self.cunr==False:
        #print(self.desktop.availableGeometry().height())
            self.setFixedHeight(100)
            self.setFixedWidth(100)
            self.move(0,self.desktop.availableGeometry().height()-self.height())
            self.cunr=True
            self.grab_thread=grab_thread(self,geo,1)
            self.grab_thread.start()
            self.btn.setText('结束')
            self.setWindowOpacity(1)
        elif self.cunr==True:
            self.close()
        #print_screen.grab(geo)
        #self.show()
#geo=(503,127, 790, 180)
#print_screen.grab(geo)
app = QApplication(sys.argv)
form =mainwindow()
form.show()
app.exec_()