from PyQt5.QtWidgets import QWidget, QApplication, QToolTip, QLabel, QVBoxLayout
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtCore import Qt
import sys


class title(QWidget):
    def __init__(self):
        super().__init__()
        self.icon()

    def icon(self):
        label = QLabel(self)
        label.setText('first')
        label.setAutoFillBackground(True)
        label.setToolTip('meme')
        label.setAlignment(Qt.AlignCenter)
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.yellow)
        label.setPalette(palette)
        # 设置背景颜色
        vbox = QVBoxLayout()
        vbox.addWidget(label)
        vbox.addStretch()
        self.setLayout(vbox)
        # QToolTip.setFont(QFont('SansSerif', 10))
        self.setGeometry(400, 400, 500, 500)
        self.setWindowIcon(QIcon('./img/cartoon4.ico'))
        self.setWindowTitle('wanganaiwangshu')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = title()
    win.show()
    sys.exit(app.exec_())