from board import *
from PySide.QtGui import QApplication

#Global vaeriable
position = [0]*12
player = 1
p1_name = ''
p2_name = ''

def main(): 
    app = QApplication(sys.argv)
    ex = Board(position, p1_name, p2_name)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()