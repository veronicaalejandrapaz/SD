import pdb 

class Client:
  
  def __init__(self, adapter):
    self.adapter = adapter
    self.opened_files = []

  def conectar(self):
    try:
      self.adapter.conectar()
    except Exception as e:
      print('Connection error {e}')

  def is_connected(self):
    return self.connection

  def list_files(self, path):
    return self.adapter.list_files(path)
  
  def open_file(self, path):
    fd = self.adapter.open_file(path)
    self.opened_files.append(fd)
    print('opened')
    return fd
  
  def close_file(self, path):
    return self.adapter.close_file(path)

  def read_file(self, path):
    offset = 0
    number_bytes = 4000
    eof = False
    literal = 0
   # try:
    with open('salida.txt', 'w') as f:
      print('salida.txt opened')
      while not eof:
        literal = literal + 1
        payload = {'path': path, 'offset':offset, 'operacion':1, 'nro_bytes':number_bytes}
        print(payload)
       # pdb.set_trace()
        data = self.adapter.read_file(payload.get('path'), offset, number_bytes)
        #raise Exception(data)
        offset = offset + literal
        if not (offset%number_bytes == 0):
          eof = True
        f.write(payload.get('path'))
        print('still reading')
    #except Exception as e:
     # print('ERROR -> -client- read file ', e)
        
    return ('check the ouput file in this directory')