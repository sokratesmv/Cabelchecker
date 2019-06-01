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

LR_read = [50,55,51,53,54,52,49]
LR_write = [81,82,83,84,86,90,89]
LR_in = [2,64,4,16,32,8,1]
PW_result = [0,0,0,0,0,0,0]

#check if cable is OK
def check():
        for out in range(0,7):
                
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

                bus.write_byte_data(adress_24,OLATA,0xff)
                bus.write_byte_data(adress_24,OLATB,0xff)
                bus.write_byte_data(adress_25,OLATB,0xff)
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
                        PW_result[out] = 1
                if read != LR_in[out]:
                        PW_result[out] = 0
                print ("LR_write-->", LR_write[out], "LR_read-->", LR_read[out], "read-->", read, "result-->", PW_result[out])

                out = out + 1
                
        return(PW_result)
check()
