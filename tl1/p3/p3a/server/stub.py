import grpc
from concurrent import futures
import time

import file_system_pb2
from file_system_pb2_grpc import (
    add_FSServicer_to_server,
    FSServicer,
)

class StubFSServicer(FSServicer):

    opened_files = {}

    def __init__(self, adapter):
        self._adapter = adapter
        FSServicer.__init__(self)

    def ListFiles(self, request, context):
        response = file_system_pb2.PathFiles()
        try:
            for file in self._adapter.list_files(request.value):
                response.values.append(file)
        except Exception as e:
            print('ERRR En server list files ', e)
        return response
    
    def OpenFiles(self, request, context):
        response = file_system_pb2.Booleano()
        open = self._adapter.open_file(request.value)
        print("Open file")
        response.value = open
        print(response)
        return response
    
    def CloseFiles(self, request, context):
        response = file_system_pb2.Booleano()
        cerrar = self._adapter.close_file(request.value)
        print("Close file")
        response.value = cerrar
        print(response)
        return response
    
    def ReadFiles(self, request, context):
        #with open('test.bin', 'rb') as f:
        response = file_system_pb2.Path()
        #with self._adapter.open_file(request.value) as archivo:
        for r in self._adapter.read_file(request.value):
            response.value = r
            print("leido???¡")
        return response
        #for r in self._adapter.read_file(request.value):
         #   response.value = r
        #return response
        #response = file_system_pb2.Byte()
        #with self._adapter.open_file(request.value) as archivo:
         #   leer = archivo.read_file(request.value)
          #  print(leer)
        #response.value = leer
        #print("estoy leyendo???")
        #print(response.value)
        #yield response


class Stub:

    def __init__(self, adapter, port='50051'):
        self._port = port
        self._adapter = adapter
        self.server = None

    def _setup(self):
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        add_FSServicer_to_server(StubFSServicer(self._adapter), self.server)
        self.server.add_insecure_port('[::]:{}'.format(self._port))

    def run(self):
        self._setup()
        self.server.start()
        try:
            while True:
                time.sleep(86400)
        except KeyboardInterrupt:
            self.server.stop(0)
