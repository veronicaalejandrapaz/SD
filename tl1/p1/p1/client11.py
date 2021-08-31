from stub import Stub
from mock_stub import MockStub
from client import Cliente


def main():

    # definicion de los stubs stub y mock_stub
    stub = Stub('localhost', 8090)
    mock_stub = MockStub('localhost', 8090)

    # para emplear otro stub, se cambia el parametro 
    # que se le brinda a la clase Cliente
    cliente = Cliente(stub)

    cliente.conectar()

    print("Realice consulta o precione s para salir")
    mensaje = input(" -> ")  # tomo entrada por teclado
    while True:
        if mensaje.lower().strip() != 's':
            cliente.enviar(mensaje)  #cliente envia el mensaje
            data = cliente.recibir()  #cliente recibe la respuesta del servidor
            print('Respuesta servidor: ' + data)  #muestro por terminal
            mensaje = input(" -> ")  #tomo la entrada por teclado
        else:
            break

    cliente.desconectar()


main()
