import test
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Skjerm import Ui_Form
import smbus
import time
import IO

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

#setting pins as outputs
bus.write_byte_data(adress_20,IO_DIR_A,0x00)
bus.write_byte_data(adress_20,IO_DIR_B,0x00)
bus.write_byte_data(adress_21,IO_DIR_A,0x00)
bus.write_byte_data(adress_21,IO_DIR_B,0x00)
bus.write_byte_data(adress_22,IO_DIR_A,0x00)
bus.write_byte_data(adress_22,IO_DIR_B,0x00)
bus.write_byte_data(adress_23,IO_DIR_A,0x00)
bus.write_byte_data(adress_23,IO_DIR_B,0x00)
#setting pins as pull-up inputs
bus.write_byte_data(adress_24,IO_DIR_A,0xff)
bus.write_byte_data(adress_24,IO_DIR_B,0xff)
bus.write_byte_data(adress_25,IO_DIR_A,0xff)
bus.write_byte_data(adress_25,IO_DIR_B,0xff)
bus.write_byte_data(adress_24,0x0d,0x00)
bus.write_byte_data(adress_24,0x0c,0x00)
bus.write_byte_data(adress_25,0x0d,0x00)
bus.write_byte_data(adress_25,0x0c,0x00)
            
class MyFirstGuiProgram(Ui_Form):
    def __init__(self, dialog):
        Ui_Form.__init__(self)
        self.setupUi(dialog)
    
        self.Test1.clicked.connect(self.test_1)
        self.Test2.clicked.connect(self.test_2)
        
    def test_1(self):
        image = QtGui.QImage(QtGui.QImageReader("green.png").read())
        self.label_1.setPixmap(QtGui.QPixmap(image))
           
        adress,port,pin = IO.write_pin(1)
        bus.write_byte_data(adress,port,pin)

    def test_2(self):
        image = QtGui.QImage(QtGui.QImageReader("red.png").read())
        self.label_1.setPixmap(QtGui.QPixmap(image))
            
        adress,port,pin = IO.write_pin(1)
        bus.write_byte_data(adress,port,0)

        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()

    prog = MyFirstGuiProgram(dialog)

    dialog.show()
    #sys.exit(app.exec_())
    app.exec_()
