#!/usr/bin/env python3
import http.server
import socketserver
import os
import json

#print('source code for "http.server":', http.server.__file__)

class web_server(http.server.SimpleHTTPRequestHandler):
    
    def do_GET(self):

        print(self.path)
        
        if self.path == '/':
            self.protocol_version = 'HTTP/1.1'
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=UTF-8")
            self.end_headers()            
            self.wfile.write(b"Hello World!\n")
        else:
            if self.path.startswith('/str='):
                self.protocol_version = 'HTTP/1.1'
                self.send_response(200)
                self.send_header("Content-type", "text/html; charset=UTF-8")
                self.end_headers()           
                param = self.path.split('/str=',1)
                strP = param[1]
                cntLowercase = sum(map(str.islower, strP))
                cntUpperCase = sum(map(str.isupper, strP))
                cntDigits = sum(map(str.isdigit, strP))
                rest = 10
                data = {}
                data['lowercase'] = cntLowercase
                data['uppercase'] = cntUpperCase
                data['digits'] = cntDigits
                data['special'] = rest
                json_data = json.dumps(data)
                self.wfile.write(bytes(json_data).encode())

    
# --- main ---

PORT = 4080

print(f'Starting: http://localhost:{PORT}')

tcp_server = socketserver.TCPServer(("",PORT), web_server)
tcp_server.serve_forever()
