from collections import defaultdict
import socket
import pickle

server_address = (('0.0.0.0', 8081))
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(server_address)
server.listen()

acumulador = defaultdict(lambda: 0)


while True:
    print('Server disponible!')
    connection, client_address = server.accept()    

    while True:
        print('-----------------')
        print(acumulador)
        print('-----------------')
        data1 = connection.recv_into(4096).decode()
        data = connection.recv_into(4096)
        payload = pickle.loads(data)
        token = payload.get('token')
        command = payload.get('command')

        if not data1 and not data: break
        
        if data1 == 'A':
            acumulador[token] += payload.get('valor')
            print(valor)

        elif data1 == 'O':
            result = {}
            result['valor'] = acumulador[token]
            connection.sendall(result)
            
        else:
            print(f'El cliente {token} solicito el comando {command}')
            break
        

    connection.close()
    print('cliente desconectado \n')


