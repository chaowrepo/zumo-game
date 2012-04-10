import sys
from PyQt4 import QtGui, QtCore

class example(QtGui.QWidget):
    def __init__(self, parent=None):
        super(QtGui.QWidget, self).__init__(parent)
        self.x_position = 50
        self.resize(500, 300)
        self.move(500, 200)
        self.initUI()
        self.show()

    def initUI(self):
        self.loadImage()
        qbt = QtGui.QPushButton('Go', self)
        qbt.clicked.connect(self.go_go_go)
        qbt.move(150, 200)
        qbtB = QtGui.QPushButton('Back', self)
        qbtB.clicked.connect(self.back_back_back)
        qbtB.move(250, 200)
    
    def loadImage(self):
        self.cartoon_label = QtGui.QLabel(self)
        cartoon_pic = QtGui.QPixmap('cartoon.png' )
        self.cartoon_label.setPixmap(cartoon_pic)
        self.cartoon_label.move(self.x_position, 20)

        self.cartoon2_label = QtGui.QLabel(self)
        cartoon2_pic = QtGui.QPixmap('cartoon2.png' )
        self.cartoon2_label.setPixmap(cartoon2_pic)
        self.cartoon2_label.move(self.x_position, 20)
        self.cartoon2_label.hide()

    def go_go_go(self):
        self.cartoon2_label.hide()
        self.cartoon_label.show()
        self.x_position = self.x_position + 50
        self.cartoon_label.move(self.x_position, 20)

    def back_back_back(self):
        self.cartoon_label.hide()
        self.cartoon2_label.show()
        self.x_position = self.x_position - 50
        self.cartoon2_label.move(self.x_position, 20)

def main():
    app = QtGui.QApplication(sys.argv)
    ex = example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
