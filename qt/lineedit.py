from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys


class lineedit(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Line edit')

        self.lin1 = QLineEdit()
        lin2 = QLineEdit()
        lin3 = QLineEdit()
        lin4 = QLineEdit()
        lin5 = QLineEdit()
        self.lin1.setInputMask('999.999.999.999;_')
        lin2.setInputMask('HH-HH-HH-HH-HH;')
        lin3.setPlaceholderText('password')
        lin3.setEchoMode(QLineEdit.Password)
        lin4.setValidator(QDoubleValidator(1.11, 11.33, 2))
        lin5.textChanged.connect(self.txtchange)
        lin5.editingFinished.connect(self.finishi)
        fo = QFormLayout()
        fo.addRow('IP:',self.lin1)
        fo.addRow('mac:',lin2)
        fo.addRow('password:',lin3)
        fo.addRow('limit:',lin4)
        fo.addRow('ssss', lin5)

        self.setLayout(fo)
    def txtchange(self,text):
        print('change   '+text)
    def finishi(self):
        print('yishuru')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = lineedit()
    w.show()

    sys.exit(app.exec_())