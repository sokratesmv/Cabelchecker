#importing libraries
import smbus
import time
import IO

Roof_Write = [83,81,86,84,82]
Roof_read = [51,50,54,53,55]
Roof_in = [4,2,32,16,64]
Roof_result = [0,0,0,0,0]

#check if cable is OK
for out in range(0,5):
        adress_in,port_in,pin_in = IO.read_pin(Roof_read[out])
        adress_out,port_out,pin_out = IO.write_pin(Roof_write[out])

        bus.write_byte_data(adress_out,port_out,0)
        bus.write_byte_data(adress_out,port_out,pin_out)
        time.sleep(0.1)
        read = bus.read_byte_data(adress_in,port_in)
        time.sleep(0.1)
        bus.write_byte_data(adress_out,port_out,0)

        if read == Roof_in[out]:
                Roof_result[LR][out] = 1
        if read != Roof_in[out]:
                Roof_result[LR][out] = 0
        print ("Roof_write-->", Roof_write[out], "Roof_read-->", Roof_read[out], "read-->", read, "result-->", Roof_result[out])
                        
        out = out +1
