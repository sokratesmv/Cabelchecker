# /etc/init.d/sample.py
### BEGIN INIT INFO
# Provides:          sample.py
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start daemon at boot time
# Description:       Enable service provided by daemon.
### END INIT INFO

import test
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from SkjermProg import Ui_Form
import smbus
import time
import IO
#import Roof
import LR

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
            
class MyFirstGuiProgram(Ui_Form):
    def __init__(self, dialog):
        Ui_Form.__init__(self)
        self.setupUi(dialog)
        image = QtGui.QImage(QtGui.QImageReader("background.png").read())
        self.Background.setPixmap(QtGui.QPixmap(image))        

        self.Test1.clicked.connect(self.test_1)
        #self.Test2.clicked.connect(self.test_2)
        #self.Test3.clicked.connect(self.test_3)
        
    def test_1(self):

        LR.check()
        LR_result =LR.LR_result

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

    #def test_2(self):

    #def test_3(self):

        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()

    prog = MyFirstGuiProgram(dialog)

    dialog.show()
    #sys.exit(app.exec_())
    app.exec_()
