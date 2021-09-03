import socket
import os
import sys
from errno import EPIPE


from p3b.structures import (
    Path, 
    PathFiles,
)


class FSStub:

    def __init__(self, canal):
        self._channel = canal

    def ListFiles(self, path):
        path = Path(path=path, operacion=1)
        self._channel.sendall(path)

        path_files = PathFiles()
        list_files = []
        while self._channel.recv_into(path_files):
            list_files.append(path_files.values)

        return list_files
        


class Stub:

    def __init__(self, host='0.0.0.0', port='8090'):
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
        return None
        #intento agarrar una exception que me sale cuando manejo bytes, es la de broke pip
    def open_file(self, path):
        try:
            broken_pipe_exception = BrokenPipeError
        except NameError:  
            broken_pipe_exception = IOError

        try:
            #raise Exception(path)
            for linea in path:
                self._channel.sendall(bytes(path, 'utf-8'))
                raise Exception(response) 
            response = self._channel.recv_into(path_files)
               
            return response
        except broken_pipe_exception as exc:
            if broken_pipe_exception == IOError:
                if exc.errno != EPIPE:
                    raise

    
    def read_file(self, path):
        path = Path(value=path)
        response = self._stub.ReadFiles(path)
        return response.value
    
    def read_file(self, path):
        path = Path(value=path)
        response = self._stub.ReadFiles(path)
        return response.value
    
    def close_file(self, path):
        archivo = path
        boolean = close(archivo) 
        print(archivo)
        if boolean:
            response = True
            return response 
        else: 
            response = False
            return response