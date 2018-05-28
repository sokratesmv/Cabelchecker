
IO_write = None
IO_read = None
IO_output = None

#function to acces outputpins
def write_pin(IO_write):

        adress_array = [0x20, 0x21, 0x22, 0x23, 0x24, 0x25]

        port_array = [0x14, 0x15]

        #pin_array = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80]
        pin_array = [0xfe, 0xfd, 0xfb, 0xf7, 0xef, 0xdf, 0xbf, 0x7f]


        adress = adress_array[int((IO_write-1)/16)]

        port = port_array[int(((IO_write-1)/8)%2)]

        pin = pin_array[7 & (IO_write - 1)]

        return(adress,port,pin)

#function to acces inputpins
def read_pin(IO_read):

        adress_array = [0x20, 0x21, 0x22, 0x23, 0x24, 0x25]

        port_array = [0x12, 0x13]

        pin_array = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80]



        adress = adress_array[int((IO_read-1)/16)]

        port = port_array[int(((IO_read-1)/8)%2)]

        pin = pin_array[7 & (IO_read - 1)]

        return(adress,port,pin)
