from client import Client
from p3b import ClientStub

def main():
    stub = ClientStub('localhost', '50051')
    cliente = Client(stub)
    cliente.conectar()
    #respuesta = cliente.open_file('/home/veronica/Escritorio/punto3ds/unpsjb_distribuidos/tl1/p3/README.md')
    #respuesta = cliente.close_file('/home/veronica/Escritorio/punto3ds/unpsjb_distribuidos/tl1/p3/README.md')
    respuesta = cliente.open_file('/home/veronica/Escritorio/punto3b/README.md')
    print(respuesta)

if __name__ == '__main__':
    main()