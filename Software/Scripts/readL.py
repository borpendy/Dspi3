import smbus2
bus = smbus2.SMBus(1)
d_addr = 0x55
r_addr1 = 0x10
r_addr2 = 0x12
remcap = bus.read_word_data(d_addr,r_addr1)
fullcap = bus.read_word_data(d_addr,r_addr2)
#print(remcap)
#print(fullcap)
data = (remcap/fullcap)*100
print(f"{data:.2f}")
