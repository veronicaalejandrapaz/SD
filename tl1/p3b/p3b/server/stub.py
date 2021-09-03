import socket
from p3b.structures import Path
import server

class FSStub:

    def __init__(self, canal, file_system_adapter):
        self._channel = canal
        self._adapter = file_system_adapter
        self._process_request()

    def _process_request(self):
        path = Path()
        data = self._channel.recv_into(path)
        #if not data: 
         #   break
        if path.operacion == 1:
            path_ = path.path
            path_files = self._adapter.list_files(path_)

            for _path in path_files:
                self._channel.sendall(_path)

        if path.operacion == 2: #abrir archivo
            path_ = path.path
            path_files = self._adapter.open_file(path_)

            for _path in path_files:
                self._channel.sendall(_path)
                
        if path.operacion == 3:   #leer archivo
            path_ = path.path
            path_files = self._adapter.read_file(path_)

            for _path in path_files:
                self._channel.sendall(_path)
        
        if path.operacion == 4:   #cerrar archivo
            path_ = path.path
            path_files = self._adapter.cerrar_file(path_)

            for _path in path_files:
                self._channel.sendall(_path)
    

class Stub:

    def __init__(self, adapter, port='8090'):
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

    def list_files(self, path):
        if self.is_connected():
            path = Path(value=path)
            response = self._stub.ListFiles(path)
            return response.values
        return None
        
    def open_file(self, path):
        if self.is_connected():
            path = Path(value=path)
            response = self._stub.OpenFiles(path)
            return response.values
    
    def close_file(self, path):
        path = Path(value=path)
        response = self._stub.CloseFiles(path)
        return response.value

    def read_file(self, path):
        path = Path(value=path)
        response = self._stub.ReadFiles(path)
        return response.value   
           