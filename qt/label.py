from PyQt5.QtWidgets import *
import sys


class LabelLine(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('label and line')

        label1 = QLabel('&Name')
        lineedit1 = QLineEdit(self)
        label1.setBuddy(lineedit1)
        label2 = QLabel('&Age')
        lineedit2 = QLineEdit(self)
        label2.setBuddy(lineedit2)

        btok = QPushButton('&Ok')
        btcc = QPushButton('&Cancel')
        mainlayout = QGridLayout(self)
        mainlayout.addWidget(label1,0,0)
        mainlayout.addWidget(lineedit1,0,1,1,2)
        mainlayout.addWidget(label2,1,0)
        mainlayout.addWidget(lineedit2,1,1,1,2)
        mainlayout.addWidget(btok,2,1)
        mainlayout.addWidget(btcc,2,2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = LabelLine()
    w.show()
    sys.exit(app.exec_())


