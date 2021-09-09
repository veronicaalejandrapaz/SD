from file_system import FS
from server import Server
from server_stub import ServerStub
import pdb

def main():
    stub = ServerStub(FS(), 8095)
    server = Server(stub)
   # pdb.set_trace()
    server.start()

if __name__ == '__main__':
    main()