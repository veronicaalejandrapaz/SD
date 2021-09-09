import os

class FS:

  def __init__(self):
        self._file_manager = {}

  def list_files(path):
    try:
      return os.listdir(path)
    except Exception as e:
      print('error! -> ', e)
      return None

  def open_file(path):
    try:
      if path not in self._file_manager:
        _file = open(path, 'rb')
        self._file_manager[path] = _file
      return True
    except Exception as e:
      print('error! OPENFILE -> ', e)
      return False

  def close_file(path):
    try:
      if path not in self._file_manager:
        self._file_manager[path].close()
        del self._file_manager[path]
      return True
    except Exception as e:
      print('error! close_file -> ', e)
      return False

  def read_file(path):
    #_path = path.value
    payload = {'path': path, 'offset': offset, 'operacion':2, 'nro_bytes':nro_bytes}
    offset = 0
    path = payload.get('path')
    number_bytes = payload.get('nro_bytes')
    try:
      if self.open_file(path):
        _fd = self._file_manager[path]
        _fd.seek(offset)
        data = _fd.read(number_bytes)
      #self.close_file(path)
      return data
    except Exception as e:
      print('error! FS read_file -> ', e)
      return None


      
