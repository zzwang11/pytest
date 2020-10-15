import sys
from PyQt5.QtWidgets import *
import datetime
import time
class WinForm(QWidget):
    def __init__(self, parent = None):
        super(WinForm, self).__init__(parent)
        self.setWindowTitle('实时刷新页面例子')
        self.resize(600,500)
        self.listFile = QListWidget()
        self.btnStart = QPushButton('开始')
        layout = QGridLayout(self)
        layout.addWidget(self.listFile, 0, 0, 1, 2)
        layout.addWidget(self.btnStart, 1, 1)

        self.btnStart.clicked.connect(self.slotAdd)
        self.setLayout(layout)

    def slotAdd(self):
        self.btnStart.setEnabled(False)
        for n in range(100):
            time1 = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S.%f')[:-3]
            str_n = time1+'  '+'file index {0}'.format(n)
            self.listFile.addItem(str_n)
            QApplication.processEvents()
            time.sleep(0.1)
        self.btnStart.setEnabled(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = WinForm()
    form.show()
    sys.exit(app.exec_())