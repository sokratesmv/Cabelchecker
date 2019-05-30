#importing libraries
import smbus
import time
import IO

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

def resetPins():
        #setting pins as outputs
        bus.write_byte_data(adress_20,IO_DIR_A,0x00)
        bus.write_byte_data(adress_20,IO_DIR_B,0x00)
        bus.write_byte_data(adress_21,IO_DIR_A,0x00)
        bus.write_byte_data(adress_21,IO_DIR_B,0x00)
        bus.write_byte_data(adress_22,IO_DIR_A,0x00)
        bus.write_byte_data(adress_22,IO_DIR_B,0x00)
        bus.write_byte_data(adress_23,IO_DIR_A,0x00)
        bus.write_byte_data(adress_23,IO_DIR_B,0x00)
        bus.write_byte_data(adress_24,IO_DIR_A,0x00)
        bus.write_byte_data(adress_24,IO_DIR_B,0x00)
        bus.write_byte_data(adress_25,IO_DIR_A,0x00)
        bus.write_byte_data(adress_25,IO_DIR_B,0x00)
        #setting pins low
        bus.write_byte_data(adress_20,OLATA,0x00)
        bus.write_byte_data(adress_20,OLATB,0x00)
        bus.write_byte_data(adress_21,OLATA,0x00)
        bus.write_byte_data(adress_21,OLATB,0x00)
        bus.write_byte_data(adress_22,OLATA,0x00)
        bus.write_byte_data(adress_22,OLATB,0x00)
        bus.write_byte_data(adress_23,OLATA,0x00)
        bus.write_byte_data(adress_23,OLATB,0x00)
        bus.write_byte_data(adress_24,OLATA,0x00)
        bus.write_byte_data(adress_24,OLATB,0x00)
        bus.write_byte_data(adress_25,OLATA,0x00)
        bus.write_byte_data(adress_25,OLATB,0x00)
        #setting pins as normal inputs
        bus.write_byte_data(adress_20,IO_DIR_A,0xff)
        bus.write_byte_data(adress_20,IO_DIR_B,0xff)
        bus.write_byte_data(adress_21,IO_DIR_A,0xff)
        bus.write_byte_data(adress_21,IO_DIR_B,0xff)
        bus.write_byte_data(adress_22,IO_DIR_A,0xff)
        bus.write_byte_data(adress_22,IO_DIR_B,0xff)
        bus.write_byte_data(adress_23,IO_DIR_A,0xff)
        bus.write_byte_data(adress_23,IO_DIR_B,0xff)
        bus.write_byte_data(adress_24,IO_DIR_A,0xff)
        bus.write_byte_data(adress_24,IO_DIR_B,0xff)
        bus.write_byte_data(adress_25,IO_DIR_A,0xff)
        bus.write_byte_data(adress_25,IO_DIR_B,0xff)
        bus.write_byte_data(adress_20,0x0d,0x00)
        bus.write_byte_data(adress_20,0x0c,0x00)
        bus.write_byte_data(adress_21,0x0d,0x00)
        bus.write_byte_data(adress_21,0x0c,0x00)
        bus.write_byte_data(adress_22,0x0d,0x00)
        bus.write_byte_data(adress_22,0x0c,0x00)
        bus.write_byte_data(adress_23,0x0d,0x00)
        bus.write_byte_data(adress_23,0x0c,0x00)
        bus.write_byte_data(adress_24,0x0d,0x00)
        bus.write_byte_data(adress_24,0x0c,0x00)
        bus.write_byte_data(adress_25,0x0d,0x00)
        bus.write_byte_data(adress_25,0x0c,0x00)
