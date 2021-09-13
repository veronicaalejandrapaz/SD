from client import Client
from p3a import ClientStub

def main():
    stub = ClientStub('localhost', '50051')
    cliente = Client(stub)
    cliente.conectar()
    #respuesta = cliente.listar_archivos('.')
    respuesta = cliente.abrir_file('/home/veronica/Documentos/distribuidos/SD/tl1/p3/README.md')
    #respuesta = cliente.abrir_file('/home/veronica/Escritorio/punto3ds/unpsjb_distribuidos/tl1/p3/README.md')
    #respuesta = cliente.cerrar_file('/home/veronica/Escritorio/punto3ds/unpsjb_distribuidos/tl1/p3/README.md')
    #respuesta = cliente.cerrar_file('/home/veronica/Escritorio/punto3ds/unpsjb_distribuidos/tl1/p3/README.md')
    respuesta = cliente.leer_file('/home/veronica/Documentos/distribuidos/SD/tl1/p3/README.md')
    print(respuesta)

if __name__ == '__main__':
    main()