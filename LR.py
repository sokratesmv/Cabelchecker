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

LR_read = [4,5,6,12,13,14,20,21,22,28,29,30,36,37,38,44,45,46]
LR_write = [67,66,65,70,69,68,87,72,71,75,74,73,78,77,76,88,80,79]
LR_in = [8,16,32,8,16,32,8,16,32,8,16,32,8,16,32,8,16,32]
LR_result = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#check if cable is OK
def check():
        
        #setting pins as outputs
        bus.write_byte_data(adress_24,IO_DIR_A,0x00)
        bus.write_byte_data(adress_24,IO_DIR_B,0x00)
        bus.write_byte_data(adress_25,IO_DIR_A,0x00)
        bus.write_byte_data(adress_25,IO_DIR_B,0x00)
        #setting pins as pull-up inputs
        bus.write_byte_data(adress_20,IO_DIR_A,0xff)
        bus.write_byte_data(adress_20,IO_DIR_B,0xff)
        bus.write_byte_data(adress_21,IO_DIR_A,0xff)
        bus.write_byte_data(adress_21,IO_DIR_B,0xff)
        bus.write_byte_data(adress_22,IO_DIR_A,0xff)
        bus.write_byte_data(adress_22,IO_DIR_B,0xff)
        bus.write_byte_data(adress_23,IO_DIR_A,0xff)
        bus.write_byte_data(adress_23,IO_DIR_B,0xff)
        bus.write_byte_data(adress_20,0x0d,0xff)
        bus.write_byte_data(adress_20,0x0c,0xff)
        bus.write_byte_data(adress_21,0x0d,0xff)
        bus.write_byte_data(adress_21,0x0c,0xff)
        bus.write_byte_data(adress_22,0x0d,0xff)
        bus.write_byte_data(adress_22,0x0c,0xff)
        bus.write_byte_data(adress_23,0x0d,0xff)
        bus.write_byte_data(adress_23,0x0c,0xff)                        
        
        for out in range(0,18):
                
                bus.write_byte_data(adress_24,OLATA,0xff)
                bus.write_byte_data(adress_24,OLATB,0xff)
                bus.write_byte_data(adress_25,OLATA,0xff)
                bus.write_byte_data(adress_25,OLATB,0xff)
                
                adress_in,port_in,pin_in = IO.read_pin(LR_read[out])
                adress_out,port_out,pin_out = IO.write_pin(LR_write[out])
                        
                bus.write_byte_data(adress_out,port_out,pin_out)
                time.sleep(0.01)
                read = bus.read_byte_data(adress_in,port_in)
                time.sleep(0.01)
                bus.write_byte_data(adress_out,port_out,0)
                        
                read = ~read 
                read = read & 0xff

                if read == LR_in[out]:
                        LR_result[out] = 1
                if read != LR_in[out]:
                        LR_result[out] = 0
                #print ("LR_write-->", LR_write[out], "LR_read-->", LR_read[out], "read-->", read, "result-->", LR_result[out])

                out = out + 1
                
        return(LR_result)
#check()
