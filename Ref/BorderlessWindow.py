import sys
from PyQt5.QtWidgets import QVBoxLayout,QLabel,QDesktopWidget,QWidget,QApplication
from PyQt5.QtCore import Qt


class SpecialBG(QLabel):
    def __init__(self, parent):
        QLabel.__init__(self, parent)
        # mess with border-radius, thatDarklordGuy!
        self.setStyleSheet( """
                color: rgba(237,174,28,100%);
                background-color: rgba(0,0,0,100%);
                text-align: center;
                border-radius: 150px;
                border: 1px solid rgba(237,174,28,100%);
                padding: 0px;
                """)

class SimpleRoundedCorners(QWidget):
    def __init__(self):
        super(SimpleRoundedCorners, self).__init__()
        self.initUI()

    def initUI(self):
        winwidth = 320
        winheight = 320
        VBox = QVBoxLayout()
        roundyround = SpecialBG(self)
        VBox.addWidget(roundyround)
        self.setLayout(VBox)
        # transparency cannot be set for window BG in style sheets, so...
        #self.setWindowOpacity(0.5) 
        self.setWindowFlags(
                  Qt.FramelessWindowHint # hides the window controls
                | Qt.WindowStaysOnTopHint # forces window to top... maybe
                | Qt.SplashScreen # this one hides it from the task bar!
                )
        # alternative way of making base window transparent
        self.setAttribute(Qt.WA_TranslucentBackground, True) #100% transparent
    
        self.setGeometry(0, 0, winwidth, winheight)
        self.setWindowTitle('Simple Rounded Corners')
        self.show()


def main():
    app = QApplication(sys.argv)
    alldone = SimpleRoundedCorners()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
