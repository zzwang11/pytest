# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(170, 50, 611, 192))
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(50, 10, 91, 301))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.toolButton = QtWidgets.QToolButton(self.widget)
        self.toolButton.setObjectName("toolButton")
        self.verticalLayout.addWidget(self.toolButton)
        self.radioButton = QtWidgets.QRadioButton(self.widget)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)
        self.checkBox = QtWidgets.QCheckBox(self.widget)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "1"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "New Column"))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "New Column"))
        self.treeWidget.headerItem().setText(3, _translate("MainWindow", "New Column"))
        self.treeWidget.headerItem().setText(4, _translate("MainWindow", "New Column"))
        self.treeWidget.headerItem().setText(5, _translate("MainWindow", "New Column"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(2).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(3).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(4).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.radioButton.setText(_translate("MainWindow", "RadioButton"))
        self.checkBox.setText(_translate("MainWindow", "CheckBox"))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    Ui_MainWindow().setupUi(w)
    w.show()
    sys.exit(app.exec_())