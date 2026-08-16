import time
import os
import smbus2
from gpiozero import LED

bus = smbus2.SMBus(1)
d_addr = 0x55
r_addr = 0x08
def_voltage = 4200
shutoff_voltage = 3000


stat = LED(10)
stat.on()
v = bus.read_word_data(d_addr,r_addr)
voltages = [v]*5
while(1):
    v = bus.read_word_data(d_addr,r_addr)
    voltages = voltages[1:] + [v]
    voltage = sum(voltages)/5
    if(voltage<shutoff_voltage):
        os.system("shutdown now -h")
    time.sleep(0.5)
    
    
