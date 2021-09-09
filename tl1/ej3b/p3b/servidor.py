from file_system import FS
from server import Server
from server_stub import ServerStub

def main():
    stub = ServerStub(FS, 8090)
    server = Server(stub)
    server.start()

if __name__ == '__main__':
    main()