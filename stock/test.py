# __author__:"Adolphus"
# project:'stock'
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPainter, QPen
from PyQt5.QtWidgets import QApplication, QMainWindow
from time import time

class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        #self.setWindowFlags(Qt.FramelessWindowHint)
        self.offset= None
        self.ps= app.primaryScreen()
        self.setGeometry(500, 500, 200, 200)
        self.saveBackground()
        self.csec= time()
        self.moving= False
        self.ratio= 1

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
        elif event.key() in [ Qt.Key_Left, Qt.Key_Right, Qt.Key_Up, Qt.Key_Down ]:
            if time() > self.csec + 1.2:
                point= self.geometry().topLeft()
                if event.key() == Qt.Key_Left:
                    point.setX(point.x() - 1)
                elif event.key() == Qt.Key_Right:
                    point.setX(point.x() + 1)
                elif event.key() == Qt.Key_Up:
                    point.setY(point.y() - 1)
                elif event.key() == Qt.Key_Down:
                    point.setY(point.y() + 1)
                self.move(point)
                self.csec= time()
                self.saveBackground()
        super().keyPressEvent(event)

    def mousePressEvent(self, event):
        self.offset= event.pos()
        self.moving= True
        self.repaint()

    def mouseReleaseEvent(self, event):
        self.saveBackground()
        self.moving= False
        self.repaint()

    def mouseMoveEvent(self, event):
        self.move(self.mapToParent(event.pos() - self.offset))

    def paintEvent(self, event):
        qp= QPainter()
        qp.begin(self)
        if self.moving:
            qp.setBrush(QColor(220, 220, 220))
            qp.drawRect(0, 0, self.width() - 1, self.height() - 1)
        else:
            qp.drawPixmap(0, 0, self.pix.scaled(self.size() * self.ratio, Qt.KeepAspectRatio))
        qp.setPen(QPen(QColor(255, 0, 0), 1, Qt.SolidLine))
        qp.drawRect(0, 0, self.width() - 1, self.height() - 1)

    def saveBackground(self):
        self.hide()
        self.pix= self.ps.grabWindow(app.desktop().winId(), self.x(), self.y(), self.width(), self.height())
        self.show()

if __name__ == "__main__":
    app= QApplication([])
    ui= Window()
    ui.show()
    exit(app.exec_())