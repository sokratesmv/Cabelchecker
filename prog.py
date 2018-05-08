import test
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from QTdesigner_skjerm_01 import Ui_QTdesigner_01
#import random
            
class MyFirstGuiProgram(Ui_QTdesigner_01):
    def __init__(self, dialog):
        Ui_QTdesigner_01.__init__(self)
        self.setupUi(dialog)
        
        self.Hei.clicked.connect(self.printHei)
        self.Hade.clicked.connect(self.printHade)
        self.LedPa.clicked.connect(self.showLed)
        self.Ledav.clicked.connect(self.hideLed)
        self.LedBlink.clicked.connect(self.blinkLed)

    def showLed(self):
        for i in range(1,5):
            
            xlabel = getattr(self, "label_"+str(i))
            
            image = QtGui.QImage(QtGui.QImageReader("image_Green.png").read())
            xlabel.setPixmap(QtGui.QPixmap(image))

    def hideLed(self):
        for i in range(1,5):
            
            xlabel = getattr(self, "label_"+str(i))
            
            image = QtGui.QImage(QtGui.QImageReader("image_Red.png").read())
            xlabel.setPixmap(QtGui.QPixmap(image))

    def blinkLed(self):
        for pair in range(1,5):
            xlabel = getattr(self, "label_"+str(pair))
            
            image = QtGui.QImage(QtGui.QImageReader("image_Green.png").read())
            xlabel.setPixmap(QtGui.QPixmap(image))
            
    def printHei(Self):
        print("Hei")
    def printHade(Self):
        print("Hade")
    

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()

    prog = MyFirstGuiProgram(dialog)

    dialog.show()
    #sys.exit(app.exec_())
    app.exec_()
