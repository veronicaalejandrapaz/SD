from stub import Stub
from mock_stub import MockStub
from client import Cliente


def main():
    stub = Stub('localhost', 8090)
    mock_stub = MockStub('localhost', 8090)
    cliente = Cliente(stub)
    cliente.conectar()
    cliente.abrir_file('/home/veronica/Escritorio/dsPrimerTp/tl1/p3/README.md')
    #cliente.cerrar_file('/home/veronica/Escritorio/dsPrimerTp/tl1/p3/README.md')
    respuesta = cliente.recibir()
    print(respuesta)

if __name__ == '__main__':
    main()
   