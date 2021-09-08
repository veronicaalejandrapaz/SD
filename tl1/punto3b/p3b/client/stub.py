import socket
import pickle

import file_system

class FSStub:

    def __init__(self, canal):
        self._channel = canal

    def ListFiles(self, path):
        payload = {'path': path, 'operacion':1}
        pickle_path = pickle.dumps(payload)
        self._channel.sendall(pickle_path)
        data = self._channel.recv(4096)
        path_list = pickle.loads(data)
        print(path_list)
        return path_files
        
    def read_file(self, path):
        payload = {'path': path, 'operacion': 2, 'offset':offset, 'nro_bytes':nro_bytes}
        pickle_path = pickle.dumps(payload)
        self._channel.sendall(pickle_path)
        data = self._channel.recv(4096)
        path_read = pickle.loads(data)
        return path_read

class Stub:

    def __init__(self, host='0.0.0.0', port=8090):
        self._appliance = (host, port)
        self._channel = None
        self._stub = None

    def connect(self):
        """ Returns a gRPC open channel """
        try:
            self._channel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._channel.connect(self._appliance)
            self._stub = FSStub(self._channel)
            return True if self._channel else False
        except Exception as e:
            print('Error when openning channel {}'.format(e))
            return False

    def disconnect(self):
        self._channel.close()
        self._channel = None

    def is_connected(self):
        return self._channel

    def list_files():
        if self.is_connected():
            return self._stub.ListFiles(path)
        else:
            return None
        
    def open_file(self, path):
        #if self.is_connected():
        response = self._stub.open_file(path)
        return response
        #else:
            #return None
      
    def close_file(self, path):
        if self.is_connected():
            response = self.close_file(path)
            return response
        else:
            return None
    
    def read_file(self, path, offset, nro_bytes):
        if self.is_connected():
            #payload = {'path': path, 'operacion': 2, 'offset':offset, 'nro_bytes':nro_bytes} 
            #raise Exception(payload)
            return self._stub.read_file(path)
        else:
            return None
    