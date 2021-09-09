import socket
import pickle
import file_system

class FSStub:

  def __init__(self, channel):
    self._channel = channel

  def list_files(self, path):
    payload = {'path': path, 'operacion':1}
    pickle_path = pickle.dumps(payload)
    self._channel.sendall(pickle_path)
    data = self._channel.recv(4096)
    path_list = pickle.loads(data)
    print(path_list)
    return path_files

  def read_file(self, path):
    print("entre en el FSStub?????????")
    payload = {'path': path, 'operacion': 2}
    pickle_path = pickle.dumps(payload)
    self._channel.sendall(pickle_path)
    data = self._channel.recv(4096)
    path_read = pickle.loads(data)
    return path_read


class ClientStub:

  def __init__(self, host='0.0.0.0', port=8090):
        self._appliance = (host, port)
        self._channel = None
        self._stub = None


  def connect(self, host, port):
    self.host = host
    self.port = port
    try:
      print(self.url)
      self._channel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self._channel.connect(self._appliance)
      self._stub = FSStub(self._channel)
      return True if self._channel else False
    except Exception as e:
      print('error when openning channel {e}')
      return False

  def disconnect(self):
    self._channel.close()
    self._channel = None

  def is_connected(self):
    return self._channel

  def list_files(self, path):
    if self.is_connected():
      response = self._stub.list_files(path)
      return response
    else:
      return None

  def open_file(self, path):
    if self.is_connected():
      response = self._stub.open_file(path)
      return response
    else:
      return None

  def close_file(self, path):
    if self.is_connected():
      response = self._stub.close_file(path)
      return response
    else:
      return None

  def read_file(self, path, offset, nro_bytes):
    if self.is_connected():
      print(path)
      payload = {'path': path, 'offset':offset, 'operacion':2, 'nro_bytes':nro_bytes}
      pickle_path = payload.get('path')
      return self._stub.read_file(pickle_path)
    else:
      return None
      '''_path = file_system_structures.Path()
      _path.value = path
      _path.offset = offset
      _path.number_bytes = number_bytes
      _path.operacion = 2
      response = self.stub.read_file(_path)
      return response
    else:
      return None'''
