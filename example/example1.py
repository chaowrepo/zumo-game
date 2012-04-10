import sys
from PyQt4 import QtGui

class example(QtGui.QWidget):
    def __init__(self, parent=None):
        super(QtGui.QWidget, self).__init__(parent)
        self.resize(500, 300)
        self.move(500, 100)
        self.setWindowTitle('Example app.')
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
