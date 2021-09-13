from client import Client
from stubCliente import ClientStub

def main():
    stub = ClientStub('localhost', 8090)
    client = Client('localhost', 8090, stub)
    client.connect()
    response = client.read_file('/home/veronica/Escritorio/dsPrimerTp/tl1/p3b/README.md')
    
    

if __name__ == "__main__":
    main()
    

