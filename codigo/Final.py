import pygame
import time
import bluetooth

def getJoystick():
    NAME = ["4Axis 12Button USB Vibration Gamepad", " Device V.:MOTE"]
    #NAME = ["4Axis 12Button USB Vibration Gamepad", "4-Axis,12-Button with POV","USB, 3-axis, 4-button joystick", "Logitech Extreme 3D Pro USB"]

    pygame.init()

    pygame.joystick.init()
    joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

    joy = pygame.joystick
    idx = 0
    found = False

    while not found:
        found = True
        for item in range(joy.get_count()):
            if joy.Joystick(item).get_name() in NAME:
                idx = joy.Joystick(item).get_id()
                found = True
                break
        time.sleep(1)
    gamePad = joy.Joystick(idx)
    return gamePad

def getPositions(gPad):
    pygame.event.pump()
    out = []
    for i in range(gPad.get_numaxes()):
        out.append(int(gPad.get_axis(i)*100)/100.0)
    for i in range(gPad.get_numbuttons()):
        out.append(gPad.get_button(i))
    return out


gpad = getJoystick()


gpad.init()

def Posicion():
    try:
        while True:
            dt = getPositions(gpad)
            eje0 = round(gpad.get_axis(0),2)
            eje1 = round(gpad.get_axis(1),2)
            salir = gpad.get_button(4)
            if eje0>=0.90:
                return "b"
            elif eje0<=-0.90:
                return "a"
            elif eje1>=0.90:
                return "d"
            elif eje1<=-0.90:
                return "c"
            elif salir==1:
                return "e"
            else:
                return "Hola Ligia :D "
           
    except KeyboardInterrupt:
        print "\nAdios"

class blueConection():
    def __init__(self):
        self.bname = "linvor"
        self.devices = bluetooth.discover_devices()
        self.address = ""
        self.sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        
    def connection(self):
        print "Buscando dispositivos Bluetooth"
        for Addr in self.devices:
            if self.bname == bluetooth.lookup_name(Addr):
                self.address = Addr
                break
        print "Conectando con "+self.bname+"..."
        self.sock.connect((self.address,1))
        print "Conexion Establecida\n\n"
        return

    def envio(self, data):
        self.sock.send(data)
        return

    def close(self):
        self.sock.close()
        print "Adios"
        return

blue = blueConection()
blue.connection()

evento = True
while evento:
    accion = Posicion()
    vaciar = "n"
    if accion == "e":
        evento = False
    else:
        blue.envio(accion)
        time.sleep(0.2)
