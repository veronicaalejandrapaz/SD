
class Cliente:

    dirclient = 0
    valor = 0

    def __init__(self, adapter=None):
        self.adapter = adapter
     
    def conectar(self):
        self.adapter.conectar()

    def desconectar(self):
        self.adapter.desconectar()

    def enviar(self, mensaje):
        self.adapter.enviar(mensaje)

    def recibir(self):
        return self.adapter.recibir()

    def setValor(self, val):
        self.valor = val
    
    def setDir(self, dirclient):
        self.dirclient = dirclient
