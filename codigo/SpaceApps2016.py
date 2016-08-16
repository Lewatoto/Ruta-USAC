import bluetooth

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
z = True

try:
    
    while z == True:
        dato = raw_input("Ingrese dato para enviar: ")
        blue.envio(dato)
except KeyboardInterrupt:
    print "\nADIOS"
