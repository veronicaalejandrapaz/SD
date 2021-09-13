import socket
import pickle

import file_system
import structures


class FSStub:

  def __init__(self, channel):
    self._channel = channel

  def list_files(self, path):
    payload = {'path': path, 'operacion':1}
    pickle_path = pickle.dumps(payload)
    self._channel.sendall(pickle_path)
    list_files = []
    while self._channel.recv(4096):
        data = self._channel.recv(4096)
        path_list = pickle.loads(data)
        list_files.append(path_files.values)
    return list_files
    '''_path = structures.Path(path=path, operacion=1)
    pickle_path = pickle.dumps(_path)
    self._channel.sendall(pickle_path)
    path_files = structures.PathFiles()
    list_files = []
    while self._channel.recv_into(path_files):
        list_files.append(path_files.values)
    return list_files'''

  def read_file(self, path):
    pickle_path = pickle.dumps(path)
    self._channel.sendall(pickle_path)
    data = self._channel.recv(4096)
    path_read_value = pickle.loads(data)
    return path_read_value


class ClientStub:

  def __init__(self, host='0.0.0.0', port='8090'):
    self.host = host
    self.port = port
    self.url = (host, port)
    self.channel = None
    self.stub = None


  def connect(self, host, port):
    self.host = host
    self.port = port
    try:
      print(self.url)
      self.channel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.channel.connect(self.url)
      self.stub = FSStub(self.channel)
      return True if self.channel else False
    except Exception as e:
      print('error when openning channel {e}')
      return False

  def disconnect(self):
    self.channel.close()
    self.channel = None

  def is_connected(self):
    return self.channel

  def list_files(self, path):
    if self.is_connected():
      response = self.stub.list_files(path)
      return response
    else:
      return None

  def open_file(self, path):
    if self.is_connected():
      response = self.stub.open_file(path)
      return response
    else:
      return None

  def close_file(self, path):
    if self.is_connected():
      response = self.stub.close_file(path)
      return response
    else:
      return None

  def read_file(self, path, offset, number_bytes):
    if self.is_connected():
      paquete = structures.Path()
      paquete.value = path
      paquete.offset = offset
      paquete.number_bytes = number_bytes
      paquete.operacion = 2
      response = self.stub.read_file(paquete)
      print(response)
      return response
    else:
      return None
