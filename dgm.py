import smbus
import struct


i2c_ch = 1
# DGM address on the I2C bus
i2c_address = 0x55

# Register addresses
PACKET_CONFIG_POS=(0)
PACKET_I2CADDR_POS=(PACKET_CONFIG_POS+1)
PACKET_PWM_POS=(PACKET_I2CADDR_POS+1)
PACKET_B1_POS=(PACKET_PWM_POS+1)
PACKET_B2_POS=(PACKET_B1_POS+4)
PACKET_TEMPERATURE_POS=(PACKET_B2_POS+4)
PACKET_HUMIDITY_POS=(PACKET_TEMPERATURE_POS+4)

# Initialize I2C (SMBus)
bus = smbus.SMBus(i2c_ch)



def read_temp():

    # Read temperature registers
    array = bus.read_i2c_block_data(i2c_address, PACKET_TEMPERATURE_POS, 4)
    temp = struct.unpack('f', bytes(array))[0]
    return temp

def read_humidity():

    # Read humidity registers
    array = bus.read_i2c_block_data(i2c_address, PACKET_HUMIDITY_POS, 4)
    humidity = struct.unpack('f', bytes(array))[0]
    return humidity

def read_voltage_bridge1():

    # Read voltage1 registers
    array = bus.read_i2c_block_data(i2c_address, PACKET_B1_POS, 4)
    voltage = struct.unpack('f', bytes(array))[0]
    return voltage
	
def read_voltage_bridge2():

    # Read voltage2 registers
    array = bus.read_i2c_block_data(i2c_address, PACKET_B2_POS, 4)
    voltage = struct.unpack('f', bytes(array))[0]
    return voltage
