from PyQt5.QtWidgets import *
import sys

class texte(QWidget):
    def __init__(self):
        super(QWidget,self).__init__()
        self.setWindowTitle('textedit')
        self.setGeometry(300,300,333,333)
        self.editt = QTextEdit()
        self.butt1 = QPushButton('show text')
        self.butt2 = QPushButton('show html')

        mwindow = QVBoxLayout()
        mwindow.addWidget(self.editt)
        mwindow.addWidget(self.butt1)
        mwindow.addWidget(self.butt2)
        self.setLayout(mwindow)
        self.butt1.clicked.connect(self.show_text)
        self.butt2.clicked.connect(self.show_html)

    def show_text(self):
        self.editt.setPlainText('Hello,Html!\n你好，h5')

    def show_html(self):
        self.editt.setHtml("<font color='red' size='6'><strong>Hello,Html!\n你好，h5</strong></font> ")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = texte()
    w.show()
    sys.exit(app.exec_())


