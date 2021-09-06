import os
import socket
import struct

class Cliente:

    def __init__(self, adapter=None):
        self.adapter = adapter
     
    def conectar(self):
        self.adapter.conectar()

    def desconectar(self):
        self.adapter.desconectar()

    def abrir_file(self, path):
        self.adapter.abrir_file(path)
        print(path)

    def cerrar_file(self, path):
        self.adapter.enviar_para_cerrar(path)
        print(path)
    
    def leer_file(self, path):
        self.adapter.enviar_para_leer(path)
        print(path)

    def recibir(self):
        return self.adapter.recibir()
    