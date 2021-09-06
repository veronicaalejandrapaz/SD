import socket
from stub_server import StubServer
from server import Server

server_address = (('0.0.0.0', 8090))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(server_address)
server.listen()
stub_server = StubServer()
servidor = Server()

while True:
	print('Server disponible!')
	print("Esperando clientes")
	connection, client_address = server.accept() 
	while True:
		data = connection.recv(4096).decode()
		if not data:
			break     
		#respuesta = servidor.open_file(data)
		respuesta = servidor.close_file(data)
		connection.send(respuesta.encode('utf-8'))
			#raise Exception(data)
			#with open(data, 'rb') as f:
			#	data1 = connection.recv(4096)
			#	while data1:
			#		f.read()
			#		respuesta = servidor.open_file(data1)
			#		connection.send(respuesta.encode('utf-8')) 
			#data = connection.recv(4096).decode()
			#with open(data, 'wb') as f:
			#	data1 = connection.recv(4096)
			#	while data1:
			#		f.write(data1)
			#		data1 = connection.recv(4096)
			#	respuesta = servidor.open_file(data1)
			#	connection.send(respuesta.encode('utf-8')) 
		#data = connection.recv(4096).decode() 
		#data = servidor.recibir()
		#if not data:
		#	break     
		#respuesta = servidor.open_file(data)
		#connection.send(respuesta.encode('utf-8'))
	
	connection.close()  
