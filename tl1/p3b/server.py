class Server:

    def __init__(self, adapter):
        self.adapter = adapter

    def start(self):
        print('Inicializando el servidor')
        self.adapter.run()