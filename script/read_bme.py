import BME280
from machine import I2C,Pin

# construct an I2C bus
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
bme = BME280.BME280(address=0x77, i2c=i2c)

ergebnis = bme.temperature, bme.humidity, bme.pressure
print (ergebnis)
#print( bme.temperature, bme.humidity, bme.pressure )

