import os

MAX_BUFF = 20

class FS:
  file_manager = {}

  def list_files(path):
    try:
      return os.listdir(path)
    except Exception as e:
      print('error! -> ', e)
      return None

  def open_file(path):
    try:
      if path not in FS.file_manager:
        _file = open(path, 'rb')
        FS.file_manager[path] = _file
      return True
    except Exception as e:
      print('error! OPENFILE -> ', e)
      return False

  def close_file(path):
    try:
      if path not in FS.file_manager:
        FS.file_manager[path].close()
        del FS.file_manager[path]
      return True
    except Exception as e:
      print('error! close_file -> ', e)
      return False

  def read_file(path):
    _path = path.value
    _offset = path.offset
    _number_bytes = path.number_bytes
    try:
      if FS.open_file(_path):
        _fd = FS.file_manager[_path]
        _fd.seek(_offset)
        data = _fd.read(_number_bytes)
      FS.close_file(_path)
      return data
    except Exception as e:
      print('error! FS read_file -> ', e)
      return None


      
