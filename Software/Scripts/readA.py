import smbus2
bus = smbus2.SMBus(1)
d_addr = 0x55
r_addr = 0x0C
data = bus.read_word_data(d_addr,r_addr)
if(data>32767):
    data = data - 65536
print(data)