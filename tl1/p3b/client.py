class Client:
  
  def __init__(self, host, port, adapter):
    self.host = host
    self.port = port
    self.adapter = adapter
    self.connection = None
    self.opened_files = []

  def connect(self):
    try:
      self.connection = self.adapter.connect(self.host, self.port)
    except Exception as e:
      print('connection error {e}')

  def is_connected(self):
    return self.connection

  def list_files(self, path):
    return self.adapter.list_files(path)
  
  def open_file(self, path):
    fd = self.adapter.open_file(path)
    self.opened_files.append(fd)
    print('abierto')
    return fd
  
  def close_file(self, path):
    return self.adapter.close_file(path)

  def read_file(self, path):
    offset = 0
    nro_bytes = 4000
    eof = False
    literal = 0
    try:
      with open('salida.txt', 'wb') as f:
        print('salida.txt opened')
        while not eof:
          data = self.adapter.read_file(path, offset, nro_bytes)
          offset = offset + len(data)
          print(offset)
          print("data:")
          print(data)
          if not (offset%nro_bytes == 0):
            eof = True
          f.write(data)
    except Exception as e:
      print('ERROR -> -client- read file ', e)
        
    return ('check the ouput file in this directory')