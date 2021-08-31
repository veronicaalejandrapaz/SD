import socket


server_address = (('0.0.0.0', 8090))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(server_address)
server.listen(4)

while True:
	print('Server disponible!')
	print("Esperando clientes")
	connection, client_address = server.accept()  #acepta nueva conexion
	print("Conectado desde " + str(client_address))
	while True:
		data = connection.recv(4096).decode() #recibe flujo de datos, no aceptará paquetes de datos de más de 4096 bytes
		if not data:
			break     #si no se reciben datos (data) termina la ejecucion
		print("Desde cliente: " + str(data))
		data = input(' -> ')
		connection.send(data.encode('utf-8'))  #se envian datos al cliente
	
	connection.close()  
	print('cliente desconectado \n')
