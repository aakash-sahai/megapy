from megapy import *
import sys

if __name__ == "__main__":
    device = None
    try:
        device = sys.argv[1]
    except:
        pass
    conn = ArduinoConnection(device)
    conn.flush()
    conn.ping()
    s1 = Stepper(conn, 1)
    s2 = Stepper(conn, 2)
    s1.enable()
    s2.enable()
    s1.microsteps = 32
    s2.microsteps = 16
    for i in range(10):
        s1.rpm = i
        s1.stepsperrev = i * 2
        print "RPM: ", s1.rpm, s2.rpm
        print "Microsteps: ", s1.microsteps, s2.microsteps
        print "Steps per rev: ", s1.stepsperrev, s2.stepsperrev
        s1.rotate(i)
        s2.rotate(-i*2)
        print "Steps remaining: ", s1.stepsremaining, s2.stepsremaining
        print "Dir: ", s1.dir, s2.dir
        s1.step(-i)
        s2.step(i*10)
        print "Steps remaining: ", s1.stepsremaining, s2.stepsremaining
        print "Dir: ", s1.dir, s2.dir
    s1.stop()
    s2.stop()
    s1.disable()
    s2.disable()
