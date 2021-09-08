import socket
import server
from file_system import *

class FSStub:

    def __init__(self, canal, file_system_adapter):
        self._channel = canal
        self._adapter = file_system_adapter
        self._process_request()

    def _process_request(self):
        data_bytes = self._channel.recv(4096)
        if data_bytes:
            payload = pickle.loads(data_bytes)
            if payload.get('operacion', 1000) == 1:
                pathv = payload.get('path')
                #list_files = []
                #list_files.append(pathv)
                path_files = self.list_files(pathv)
                #for pathv in path_files:
                self._channel.sendall(path_files)
            elif payload.get('operacion', 1000) == 2:
                path_read = self.read_file(path)
                pickle_read = pickle.dumps(path_read)
                self._channel.sendall(pickle_read)
            return 0
        else:
            return 1

class Stub:

    def __init__(self, adapter, port=8090):
        self._port = port
        self._adapter = adapter
        self.server = None
        self._stub = None

    def _setup(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(('0.0.0.0', 8090))        

    def run(self):
        self._setup()
        self.server.listen()
        try:
            while True:
                connection, client_address = self.server.accept()
                from_client = ''
                self._stub = FSStub(connection, self._adapter)

        except KeyboardInterrupt:
            connection.close()
            self.server.stop(0)

   