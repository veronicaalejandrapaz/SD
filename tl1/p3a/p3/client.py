
class Client:

    def __init__(self, adapter):
        self.adapter = adapter

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

    def abrir_file(self, path):
        return self.adapter.open_file(path)

    def cerrar_file(self, path):
        return self.adapter.close_file(path)
    
    def leer_file(self, path):
        return self.adapter.read_file(path)