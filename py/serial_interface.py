import serial

ser = 0

def initSerial():
    global ser
    ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)

def setPin(whatPin, brightness):
    ser.write(bytearray.fromhex("ff ff ff " + "whatPin" + " " + chr(brightness)))