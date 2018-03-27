# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTdesigner_skjerm_01.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QTdesigner_01(object):
    def setupUi(self, QTdesigner_01):
        QTdesigner_01.setObjectName("QTdesigner_01")
        QTdesigner_01.resize(991, 846)
        self.gridLayout_3 = QtWidgets.QGridLayout(QTdesigner_01)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.LedPa = QtWidgets.QPushButton(QTdesigner_01)
        self.LedPa.setObjectName("LedPa")
        self.horizontalLayout_2.addWidget(self.LedPa)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.LedBlink = QtWidgets.QPushButton(QTdesigner_01)
        self.LedBlink.setObjectName("LedBlink")
        self.horizontalLayout_2.addWidget(self.LedBlink)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.Ledav = QtWidgets.QPushButton(QTdesigner_01)
        self.Ledav.setObjectName("Ledav")
        self.horizontalLayout_2.addWidget(self.Ledav)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.Hei = QtWidgets.QPushButton(QTdesigner_01)
        self.Hei.setObjectName("Hei")
        self.verticalLayout.addWidget(self.Hei)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem2)
        self.Hade = QtWidgets.QPushButton(QTdesigner_01)
        self.Hade.setObjectName("Hade")
        self.verticalLayout.addWidget(self.Hade)
        self.gridLayout_3.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(QTdesigner_01)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.label_1 = QtWidgets.QLabel(QTdesigner_01)
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(QTdesigner_01)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(QTdesigner_01)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(QTdesigner_01)
        QtCore.QMetaObject.connectSlotsByName(QTdesigner_01)

    def retranslateUi(self, QTdesigner_01):
        _translate = QtCore.QCoreApplication.translate
        QTdesigner_01.setWindowTitle(_translate("QTdesigner_01", "Form"))
        self.LedPa.setText(_translate("QTdesigner_01", "Led på"))
        self.LedBlink.setText(_translate("QTdesigner_01", "Led blink"))
        self.Ledav.setText(_translate("QTdesigner_01", "Led av"))
        self.Hei.setText(_translate("QTdesigner_01", "Hei"))
        self.Hade.setText(_translate("QTdesigner_01", "Hade"))
        self.label_3.setText(_translate("QTdesigner_01", "TextLabel"))
        self.label_1.setText(_translate("QTdesigner_01", "TextLabel"))
        self.label_2.setText(_translate("QTdesigner_01", "TextLabel"))
        self.label_4.setText(_translate("QTdesigner_01", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QTdesigner_01 = QtWidgets.QWidget()
    ui = Ui_QTdesigner_01()
    ui.setupUi(QTdesigner_01)
    QTdesigner_01.show()
    sys.exit(app.exec_())

