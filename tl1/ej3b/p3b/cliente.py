from client import Client
from client_stub import ClientStub

def main():
    stub = ClientStub('localhost', 8095)
    cliente = Client(stub)
    cliente.conectar()
    response = cliente.read_file('/home/veronica/Documentos/p3b/README.md')
   # print("Ingrese una direccion de archivo o precione s para salir")
    #mensaje = input(" -> ") 
    '''while True:
        if mensaje.lower().strip() != 's':

            response = cliente.read_file(mensaje)
            pass
        else:
            break'''
    print(response)
    

if __name__ == "__main__":
    main()
    

