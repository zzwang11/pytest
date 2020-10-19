from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import PyQt5.sip as sip

class lineedit(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Line edit')

        self.lin1 = QLineEdit()
        lin2 = QLineEdit()
        lin3 = QLineEdit()
        lin4 = QLineEdit()
        lin5 = QLineEdit()
        btn = QPushButton('hello')
        self.lin1.setInputMask('999.999.999.999;_')
        print(self.lin1.parentWidget())
        print(self.lin1.parent())

        lin2.setInputMask('HH-HH-HH-HH-HH;')
        lin3.setPlaceholderText('password')
        lin3.setEchoMode(QLineEdit.Password)
        lin4.setValidator(QDoubleValidator(1.11, 11.33, 2))
        lin5.textChanged.connect(self.txtchange)
        lin5.editingFinished.connect(self.finishi)
        btn.clicked.connect(lambda :self.remove_c(self.lin1))
        self.fo = QFormLayout()
        self.fo.addRow('IP:',self.lin1)
        self.fo.addRow('mac:',lin2)
        self.fo.addRow('password:',lin3)
        self.fo.addRow('limit:',lin4)
        self.fo.addRow('ssss', lin5)
        self.fo.addRow(btn)
        print(self.lin1.parent())
        print(self.lin1.parentWidget())

        self.setLayout(self.fo)
        print(self.lin1.parent())
        print(self.lin1.parentWidget())

    def txtchange(self,text):
        print('change   '+text)
    def finishi(self):
        print('yishuru')

    def remove_c(self,x):
        # self.fo.removeWidget(x)
        sip.delete(x)
        print(sip.isdeleted(x))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = lineedit()
    w.show()

    sys.exit(app.exec_())