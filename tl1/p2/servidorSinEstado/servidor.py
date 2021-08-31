import socket
from collections import defaultdict

server_address = (('0.0.0.0', 8091))
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(server_address)
server.listen()
acumulador = defaultdict(lambda: 0)

while True:
	print('Server disponible!')
	connection, client_address = server.accept()  #acepta nueva conexion
	connection.send(str(client_address).encode('utf-8')) 
	#print("Conectado desde " + str(client_address))
	val = 0 
	while True:
		print('-----------------')
		print(acumulador)
		print('-----------------')
		data = connection.recv(4096).decode() #recibe flujo de datos, no aceptará paquetes de datos de más de 4096 bytes
		if not data: break     #si no se reciben datos (data) termina la ejecucion
		
		if data == 'A':
			data1 = connection.recv(4096).decode()
			print(data1)
			val += int(data1)
			connection.send(str(val).encode('utf-8'))  #se envian datos al cliente
			print(f'{client_address, val}')
		elif data == 'O':
			connection.send(str(val).encode('utf-8'))
			print("Cliente solicito saber el valor acumulado")
		elif data == 'S':
			print("Cliente solicito salir")
		
	connection.close()  
	print('cliente desconectado \n')
