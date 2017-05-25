
import serial
ser = serial.Serial("/dev/cu.usbmodem1421", 9600)
ser.write("L")
