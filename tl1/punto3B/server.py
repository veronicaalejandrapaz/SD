import os
import socket

class Server:

    def __init__(self, adapter=None):
        self.adapter = adapter
    
    def open_file(self, path):
        respuesta = ''
        print(path)
        if open(path):
            respuesta = "True"
            return respuesta
        else:
            respuesta = "False"
            return respuesta
    
    def close_file(self, path):
        with open(path, 'rb') as f:
            f.read()
            f.close()
            respuesta = "True"
            return respuesta
        
        
        #file_name = path
        #size = 
        #archivo = path
        #if archivo.close():
         #   respuesta = "True"
          #  return respuesta
        #else:
         #   respuesta = "False"
          #  return respuesta

    def recibir(self):
        return self.adapter.recibir()
    
    def enviar(self, msg):
        self.adapter.enviar(msg)
        print(msg)