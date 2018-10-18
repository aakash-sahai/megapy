from megapy import *
import time

if __name__ == "__main__":
    conn = ArduinoConnection()
    conn.flush()
    conn.ping()
    pin = DigitalPin(conn, 13, mode = 'output')
    a1 = AnalogPin(conn, 'a1')
    a2 = AnalogPin(conn, 'a2')
    for i in range(10):
        print a1.value, a2.value
        pin.value = 0
        time.sleep(1)
        pin.value = 1
        time.sleep(1)
