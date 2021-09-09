import socket
import pickle
from file_system import FS


class FSStub():

  def __init__(self, canal):
    self._channel = canal

  def _process_request(self):
    print('process request')
    while True:
      data_bytes = self._channel.recv(4096)
      if data_bytes:
        payload = pickle.loads(data_bytes)
        if payload.get('operacion', 1000) == 1:
          _path = payload.get('path')
          path_files = FS.list_files(_path)
          for _path in path_files:
            self._channel.sendall(_path)
        elif payload.get('operacion', 1000) == 2:
          path_read = FS.read_file(payload.get('path'))
          pickle_read = pickle.dumps(path_read)
          self._channel.sendall(pickle_read)
        return 0
      elif data_bytes == 's':
        break
        #return 1

  
class ServerStub:

  def __init__(self, adapter, port=8095):
    self._port = port
    self._adapter = adapter
    self.server = None
    self._stub = self

  def _setup(self):
    self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.server.bind(('0.0.0.0', 8095))        

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

   