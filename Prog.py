import test
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from skjerm import Ui_Form
import smbus
import time
import IO
import ROOF
import L123R123
import LR
import PW
import LED

#bus = smbus.SMBus(0)
bus = smbus.SMBus(1)
# Device address
adress_20  = 0x20 
adress_21 = 0x21
adress_22 = 0x22
adress_23 = 0x23
adress_24 = 0x24
adress_25 = 0x25
# Pin direction register
IO_DIR_A = 0x00 
IO_DIR_B = 0x01
# Register for outputs
OLATA  = 0x14 
OLATB  = 0x15
# Register for inputs
GPIOA  = 0x12 
GPIOB  = 0x13

b = [1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,21,22,23,24,25,31,32,33,34,35,36,37]
a = [0,1,2,5,6,8,11,12,13,14]  
c = [4,10]
d = [31,34]

class MyFirstGuiProgram(Ui_Form):
    def __init__(self, dialog):
        Ui_Form.__init__(self)
        self.setupUi(dialog)

        self.Test.clicked.connect(self.test)
        self.Reset.clicked.connect(self.reset)
        
        for i in range(0,10):
            xsquare = getattr(self, "square_"+str(a[i]))            
            image = QtGui.QImage(QtGui.QImageReader("square.png").read())
            xsquare.setPixmap(QtGui.QPixmap(image))
            
        for i in range(0,2):
            xsquare = getattr(self, "square_"+str(c[i]))            
            image = QtGui.QImage(QtGui.QImageReader("square1.png").read())
            xsquare.setPixmap(QtGui.QPixmap(image))

        self.reset()
        
    def reset(self):

        for i in range(0,6):
            for a in range(1,8):
                xlabel = getattr(self, "label_"+str(i)+str(a))            
                image = QtGui.QImage(QtGui.QImageReader("gray.png").read())
                xlabel.setPixmap(QtGui.QPixmap(image))
                
        for a in range(0,30):
            xlabel = getattr(self, "lab_"+str(b[a]))            
            image = QtGui.QImage(QtGui.QImageReader("gray.png").read())
            xlabel.setPixmap(QtGui.QPixmap(image))
        
        for a in range(1,5):
            xlabel = getattr(self, "led_"+str(a))            
            image = QtGui.QImage(QtGui.QImageReader("gray.png").read())
            xlabel.setPixmap(QtGui.QPixmap(image))

        image = QtGui.QImage(QtGui.QImageReader("logo.png").read())
        self.square_3.setPixmap(QtGui.QPixmap(image))
        image = QtGui.QImage(QtGui.QImageReader("logo.png").read())
        self.square_9.setPixmap(QtGui.QPixmap(image))

    def test(self):
        
        L123R123.check()
        LR_result =L123R123.LR_result

        for i in range(0,6):
            for a in range(1,8):
                        if LR_result[i][a] == 1:
                            xlabel = getattr(self, "label_"+str(i)+str(a))            
                            image = QtGui.QImage(QtGui.QImageReader("green.png").read())
                            xlabel.setPixmap(QtGui.QPixmap(image))
                        else:
                            xlabel = getattr(self, "label_"+str(i)+str(a))
                            image = QtGui.QImage(QtGui.QImageReader("red.png").read())
                            xlabel.setPixmap(QtGui.QPixmap(image))
        
        PW.check()
        PW_result = PW.PW_result
        
        for a in range(18,23):
                        if PW_result[a-18] == 1:
                            xlabel = getattr(self, "lab_"+str(b[a]))            
                            image = QtGui.QImage(QtGui.QImageReader("green.png").read())
                            xlabel.setPixmap(QtGui.QPixmap(image))
                        else:
                            xlabel = getattr(self, "lab_"+str(b[a]))
                            image = QtGui.QImage(QtGui.QImageReader("red.png").read())
                            xlabel.setPixmap(QtGui.QPixmap(image))
         
        ROOF.check()
        ROOF_result = ROOF.ROOF_result
        
        for a in range(23,30):
                        if ROOF_result[a-23] == 1:
                            xlabel = getattr(self, "lab_"+str(b[a]))            
                            image = QtGui.QImage(QtGui.QImageReader("green.png").read())
                            xlabel.setPixmap(QtGui.QPixmap(image))
                        else:
                            xlabel = getattr(self, "lab_"+str(b[a]))
                            image = QtGui.QImage(QtGui.QImageReader("red.png").read())
                            xlabel.setPixmap(QtGui.QPixmap(image))
          
        #LR.check()
        #LR_result =LR.LR_result
        
        #for a in range(0,18):
        #                if LR_result[a] == 1:
        #                    xlabel = getattr(self, "lab_"+str(b[a]))            
        #                    image = QtGui.QImage(QtGui.QImageReader("green.png").read())
        #                    xlabel.setPixmap(QtGui.QPixmap(image))
        #                else:
        #                    xlabel = getattr(self, "lab_"+str(b[a]))
        #                    image = QtGui.QImage(QtGui.QImageReader("red.png").read())
        #                    xlabel.setPixmap(QtGui.QPixmap(image))
                         
        #LED.check()
        #LED_result = LED.LED_result
        
        #for a in range(0,4):
        #                if LED_result[a] == 1:
        #                    xlabel = getattr(self, "led_"+str(a+1))            
        #                    image = QtGui.QImage(QtGui.QImageReader("green.png").read())
        #                    xlabel.setPixmap(QtGui.QPixmap(image))
        #                else:
        #                    xlabel = getattr(self, "led_"+str(a+1))
        #                    image = QtGui.QImage(QtGui.QImageReader("red.png").read())
        #                    xlabel.setPixmap(QtGui.QPixmap(image))
                            
        #for a in range(4,6):
        #                if LED_result[a] == 1:
        #                    xlabel = getattr(self, "lab_"+str(d[a-4]))            
        #                    image = QtGui.QImage(QtGui.QImageReader("green.png").read())
        #                    xlabel.setPixmap(QtGui.QPixmap(image))
        #                else:
        #                    xlabel = getattr(self, "lab_"+str(d[a-4]))
        #                    image = QtGui.QImage(QtGui.QImageReader("red.png").read())
        #                    xlabel.setPixmap(QtGui.QPixmap(image))
        
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()

    prog = MyFirstGuiProgram(dialog)
    #dialog.show()
    dialog.showFullScreen()
    #sys.exit(app.exec_())
    app.exec_()
