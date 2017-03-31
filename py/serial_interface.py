import serial

ser = 0

def initSerial():
    global ser
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

def setPin(whatPin, brightness):
    ser.write(bytes([0, whatPin, brightness]))