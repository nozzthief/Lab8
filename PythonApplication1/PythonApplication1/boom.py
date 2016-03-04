import sys 
from PySide.QtCore import *
from PySide.QtGui import *

class Simple_drawing_window1(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.setWindowTitle("Simple Drawing 1")

    def paintEvent(self,e):
        p = QPainter()
        p.begin(self)
        p.setPen(QColor(200,10,0))
        p.drawArc(300,130,50,50,0,16*360);
        p.drawArc(300,130,100,50,0,16*360);
        p.drawArc(300,130,200,50,0,16*360);
        p.end()

def main():
    app = QApplication(sys.argv)
    w = Simple_drawing_window1()
    w.show()

    return app.exec_()

if __name__=="__main__":
    sys.exit(main())