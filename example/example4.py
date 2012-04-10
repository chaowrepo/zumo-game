import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

class example(QtGui.QWidget):
    def __init__(self, parent=None):
        super(QtGui.QWidget, self).__init__(parent)
        self.resize(500, 300)
        self.move(500, 200)
        self.initUI()
        self.show()

    def initUI(self):
        self.loadImage()
        qbt = QtGui.QPushButton('Go', self)
        qbt.clicked.connect(self.go_go_go)
        qbt.move(200, 200)
    
    def loadImage(self):
        self.cartoon_label = QtGui.QLabel(self)
        cartoon_pic = QtGui.QPixmap('cartoon.png' )
        self.cartoon_label.setPixmap(cartoon_pic)
        self.cartoon_label.move(50, 20)

    def go_go_go(self):
        self.cartoon_label.move(150, 20)


def main():
    app = QtGui.QApplication(sys.argv)
    ex = example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
