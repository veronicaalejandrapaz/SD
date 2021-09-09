from client import Client
from client_stub import ClientStub

def main():
    stub = ClientStub('localhost', '50051')
    cliente = Client(stub)
    cliente.conectar()
    #response = client.list_files('/home/veronica/Documentos/p3b/README.md')
    response = cliente.read_file('/home/veronica/Documentos/p3b/README.md')
    #response = client.open_file('/home/veronica/Documentos/p3b/README.md')
    print("salida del main")
    print(response)
    

if __name__ == "__main__":
    main()
    

