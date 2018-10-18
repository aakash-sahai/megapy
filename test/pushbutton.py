from megapy import *

if __name__ == "__main__":
    conn = ArduinoConnection()
    conn.flush()
    conn.ping()
    pb1 = PushButton(conn, 20)
    pb2 = PushButton(conn, 30)
    print "Pin: ", pb1.pin, pb2.pin

    for i in range(10):
        print "Clicks: ", pb1.clicks, pb2.clicks
        pb1.enable()
        pb2.disable()
        print "State: ", pb1.state, pb2.state
        pb1.disable()
        pb2.enable()
        print "State: ", pb1.state, pb2.state
    pb1.reset()
    pb2.reset()
