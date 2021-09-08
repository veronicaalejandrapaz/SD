import os

MAX = 20

class FS:

    def __init__(self):
        self._file_manager = {}

    def list_files(self, path):
        try:
            return os.listdir(path)
        except Exception as e:
            print('ERROR!!! ', e)
            return None

    def open_file(self, path):
        try:
            if path not in self._file_manager:
                _file = open(path, 'r')
                self._file_manager[path] = _file
                print(self._file_manager)
            return True
        except Exception as e:
            print('ERROR!!! ', e)
            return False

    def close_file(self, path):
        try:
            if path in self._file_manager:
                self._file_manager[path].close()
                del self._file_manager[path]
            return True
        except Exception as e:
            print('ERROR!!! ', e)
            return False

    def read_file(self, path):
        pathv = path.value
        offsetb = path.offset
        nro_bytes = path.nro_bytes
        try:
            if self.open_file(pathv):
                #if path in self._file_manager:
                fd = self._file_manager[pathv]
                fd.seek(_offset)
                data = fd.read(pathv)
            self.close_file(pathv)
            return data    
        except Exception as e:
            print('ERROR!!! ', e)
            return None