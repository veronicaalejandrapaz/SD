import socket


class StubServer:

   def __init__(self, adapter=None):
        self.adapter = adapter

   def open_file(self, path):
      self.server.send(path.encode('utf-8'))
      print(path)
   
   def close_file(self, path):
      self.server.send(path.encode('utf-8'))

   def read_file(self, path):
      self.server.send(path.encode('utf-8'))
   
   def recibir(self):
       msg = self.server.recv(4096)
       return msg if not type(msg) == bytes else msg.decode()
      
   def enviar(self, msg):
      self.client.send(msg.encode('utf-8'))
      print(msg)