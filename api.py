from http.server import BaseHTTPRequestHandler, HTTPServer
from faker import Faker
import json

fake = Faker()


class handlerAPI(BaseHTTPRequestHandler):
  def set_response(self, status_code=200, content_type='application/json'):
    self.send_response(status_code)
    self.send_header('Content-type', content_type)
    self.end_headers()
  
  def do_GET(self):
    if self.path == '/api/user':
      self.set_response()
      user = {
        'name' : fake.name(),
        'email': fake.email(),
        'address': fake.address(),
        'phone': fake.phone_number()
      } 
      self.wfile.write(json.dumps(user).encode('utf-8'))
    else:
      self.set_response(404)
      self.wfile.write(b'Endpoint not found')

def run():
  server_address = ('', 8000)
  httpd = HTTPServer(server_address, handlerAPI)
  print(f'Mock API is running at http://localhost:{server_address[1]}/api/user') 
  httpd.serve_forever()
if __name__ == '__main__':
  run()
  
  
  
  
  