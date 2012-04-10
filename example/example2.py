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
        qbt = QtGui.QPushButton('Quit', self)
        qbt.clicked.connect(QtCore.QCoreApplication.instance().quit)
        qbt.move(200, 200)

def main():
    app = QtGui.QApplication(sys.argv)
    ex = example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
