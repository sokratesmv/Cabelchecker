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

L1_write = [0,83,83,83,67,66,65,86]
L1_read = [0,1,2,3,4,5,6,7]
L1_in = [0,0,0,0,8,16,32,64]
L1_result = [0,0,0,0,0,0,0,0]

L2_write = [0,83,83,83,70,69,68,86]
L2_read = [0,9,10,11,12,13,14,15]
L2_in = [0,0,0,0,8,16,32,64]
L2_result = [0,0,0,0,0,0,0,0]

L3_write = [0,83,83,83,87,72,71,86]
L3_read = [0,17,18,19,20,21,22,23]
L3_in = [0,0,0,0,8,16,32,64]
L3_result = [0,0,0,0,0,0,0,0]

R1_write = [0,83,83,83,75,74,73,86]
R1_read = [0,25,26,27,28,29,30,31]
R1_in = [0,0,0,0,8,16,32,64]
R1_result = [0,0,0,0,0,0,0,0]

R2_write = [0,83,83,83,78,77,76,86]
R2_read = [0,33,34,35,36,37,38,39]
R2_in = [0,0,0,0,8,16,32,64]
R2_result = [0,0,0,0,0,0,0,0]

R3_write = [0,83,83,83,88,80,79,86]
R3_read = [0,41,42,43,44,45,46,47]
R3_in = [0,0,0,0,8,16,32,64]
R3_result = [0,0,0,0,0,0,0,0]

LR_write = [L1_write,L2_write,L3_write,R1_write,R2_write,R3_write]
LR_read = [L1_read,L2_read,L3_read,R1_read,R2_read,R3_read] 
LR_in = [L1_in,L2_in,L3_in,R1_in,R2_in,R3_in]
LR_result = [L1_result,L2_result,L3_result,R1_result,R2_result,R3_result]

#check if cable is OK
def check():
        for LR in range(0,6):
                for out in range(1,8):
                        
                        bus.write_byte_data(adress_24,OLATA,0xff)
                        bus.write_byte_data(adress_24,OLATB,0xff)
                        bus.write_byte_data(adress_25,OLATA,0xff)
                        bus.write_byte_data(adress_25,OLATB,0xff)

                        adress_in,port_in,pin_in = IO.read_pin(LR_read[LR][out])
                        adress_out,port_out,pin_out = IO.write_pin(LR_write[LR][out])
                        
                        bus.write_byte_data(adress_out,port_out,pin_out)
                        time.sleep(0.01)
                        read = bus.read_byte_data(adress_in,port_in)
                        time.sleep(0.01)
                        bus.write_byte_data(adress_out,port_out,0)
                        
                        read = ~read 
                        read = read & 0xff

                        if out==1: 
                                if read == 1 or read == 3 or read == 5 or read == 7:
                                        LR_result[LR][1] = 1
                                else:
                                        LR_result[LR][1] = 0
                        elif out==2:        
                                if read == 2 or read == 3 or read == 6 or read == 7:
                                        LR_result[LR][2] = 1
                                else:
                                        LR_result[LR][2] = 0
                        elif out==3:             
                                if read == 4 or read == 5 or read == 6 or read == 7:
                                        LR_result[LR][3] = 1
                                else:
                                        LR_result[LR][3] = 0
                                   
                        else:
                                if read == LR_in[LR][out]:
                                        LR_result[LR][out] = 1
                                if read != LR_in[LR][out]:
                                        LR_result[LR][out] = 0
                        print ("LR_write-->", LR_write[LR][out], "LR_read-->", LR_read[LR][out], "read-->", read, "result-->", LR_result[LR][out])

                        out = out + 1
                LR = LR +1
                
        return(LR_result)
#check()
