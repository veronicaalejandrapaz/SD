
class Client:

    def __init__(self, adapter):
        self.adapter = adapter
        self.open_files = []

    def conectar(self):
        try:
            self.adapter.connect()
        except Exception as e:
            print('Connection error {e}')

    def desconectar(self):
        self.adapter.disconnect()

    def esta_conectado(self):
        return self.adapter.is_connected()

    def listar_archivos(self, path):
        return self.adapter.list_files(path)

    def open_file(self, path):
        _fd = self.adapter.open_file(path)
        self.open_files.append(_fd)
        print('file abierto')
        return _fd

    def close_file(self, path):
        return self.adapter.close_file(path)
    
    def read_file(self, path):
        offset = 0
        nro_bytes = 4000
        EOF = False
        try:
            with open('salida.txt', 'wb') as f:
                print('salida.txt opened')
                while not EOF:
                    data = self.adapter.read_file(path, offset, nro_bytes)
                    offset = offset + len(data)
                    if not (offset%nro_bytes == 0):
                        EOF = True
                    f.write(data)
                    print('still reading')
        except Exception as e:
            print('ERROR -> -client- read file ', e)
            
        return ('check the ouput file in this directory')