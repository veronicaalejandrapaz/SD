import socket


class Stub:
   
   def __init__(self, host='0.0.0.0', port=8080):
      self.host = host
      self.port = port
   
   def conectar(self):
      self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.client.connect((self.host, self.port))
   
   def desconectar(self):
      self.client.close()
      
   def abrir_file(self, path):
      self.client.send(path.encode('utf-8'))
      print(path)
   
   def enviar_para_cerrar(self, path):
      self.client.send(path.encode('utf-8'))
      #file = path
      #with open(file, 'wb') as f:
         #data = self.client.recv(4096)
       #  while path:
        #    f.write(path)
         #   raise Exception(f)
          #  self.client.send(file)
			   #data = self.client.recv(4096)

			#	respuesta = servidor.open_file(data1)
			#	connection.send(respuesta.encode('utf-8')) 
		#data = connection.recv(4096).decode() 
      #file = path
      #with open(file, 'rb') as f:
       #  data = f.read(4096)
        # while data:
         #   self.client.send(data)
          #  data = f.read(4096)
      #print(path)
   def enviar_para_leer(self, path):
      self.client.send(path.encode('utf-8'))
   
   def recibir(self):
      msg = self.client.recv(4096)
      return msg if not type(msg) == bytes else msg.decode()



      