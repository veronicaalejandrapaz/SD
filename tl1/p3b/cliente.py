from client import Client
from client_stub import ClientStub

def main():
    stub = ClientStub('localhost', 8090)
    client = Client('localhost', 8090, stub)
    client.connect()
    response = client.read_file('/home/veronica/Escritorio/dsPrimerTP/tl1/p3b/README.md')
    
    

if __name__ == "__main__":
    main()
    

