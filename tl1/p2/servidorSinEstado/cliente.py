from stub import Stub
from mock_stub import MockStub
from client import Cliente
import random


def main():

    # definicion de los stubs stub y mock_stub
    stub = Stub('localhost', 8091)
    mock_stub = MockStub('localhost', 8091)
    cliente = Cliente(stub)
    cliente.conectar()

    keep_working = True
    client_id = random.randint(100000, 999999)
    COMMAND = {'A': 1, 'O': 2}
    #print("Realice consulta o precione s para salir")
    #mensaje = input(" -> ")  # tomo entrada por teclado
    val = 0

    while keep_working:
        print('\n---------------------------------------------------')
        print('Ingrese un comando ([A]cumular, [O]btener, [S]alir)')
        comando = input()
        cliente.enviar(comando)
        if comando == 'A':
            print('Ingrese un valor a acumular')
            valor = int(input())
            cliente.setValor(valor)
            cliente.enviar(str(cliente.valor))
            data = cliente.recibir()  
            cliente.setValor(data)
            #cliente.enviar(str(cliente.valor))
        elif comando == 'O':
            print("INGRESO COMANDO O")
            data = cliente.recibir()  
            cliente.setValor(data)
            print(f'Valor acumulado: {cliente.valor}')
        elif comando == 'S':
           # print("Selecciono comando para salir")
            keep_working = False
            cliente.desconectar()
            print('Sesion finalizada')  

        else:
            print('El comando ingresado no es valido')

    cliente.desconectar()


main()
