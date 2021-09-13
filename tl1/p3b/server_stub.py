import socket
import pickle
import structures
from file_system import FS


class ServerFSStub():

  def __init__(self, channel):
    self._channel = channel

  def _process_request(self):
    print('process request')
    data = self._channel.recv(4096)
    if data:
      path = pickle.loads(data)
      if path is not None:
        if path.operacion == 1:
          _path = path.value
          path_files = FS.list_files(_path)
          for _path in path_files:
            self._channel.sendall(_path)
        elif path.operacion == 2:
          path_read = FS.read_file(path)
          payload_read = pickle.dumps(path_read)
          print(payload_read)
          self._channel.sendall(payload_read)
      return 0
    else:
      return 1

  
class ServerStub:
  def __init__(self, adapter, port=8090):
    self._port = port
    self._adapter = adapter
    self._stub = None
    self.server = None

  def _setup(self):
    self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(self._port)
    self.server.bind(("0.0.0.0", self._port)) 

  def run(self):
    self._setup()
    self.server.listen()
    try:
      while True:
        connection, client_address = self.server.accept()
        while True:
          from_client = ''
          self._stub = ServerFSStub(connection)
          if self._stub._process_request():
            break
    except KeyboardInterrupt:
      connection.close()
