#!/usr/bin/env python3
import http.server
import socketserver
import os
from urllib.parse import urlparse
from urllib.parse import parse_qs
import json


#print('source code for "http.server":', http.server.__file__)

class web_server(http.server.SimpleHTTPRequestHandler):
    
    def do_GET(self):
        parsed = urlparse(self.path)
        qs = parse_qs(parsed.query)

        if len(qs) == 2 and 'num1' in qs.keys() and 'num2' in qs.keys():
            self.protocol_version = 'HTTP/1.1'
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=UTF-8")
            self.end_headers() 
            num1 = int(qs['num1'][0])
            num2 = int(qs['num2'][0])
            response = {
                "sum" : num1+num2,
                "sub" : num1-num2,
                "mul" : num1*num2,
                "div" : num1//num2,
                "mod" : num1%num2
            }
            self.wfile.write(json.dumps(response).encode())
        else:
            if self.path =='/':
                self.protocol_version = 'HTTP/1.1'
                self.send_response(200)
                self.send_header("Content-type", "text/html; charset=UTF-8")
                self.end_headers() 
                self.wfile.write(b"ERROR\n")
            else:
                super().do_GET()
    
# --- main ---

PORT = 4080

print(f'Starting: http://localhost:{PORT}')

tcp_server = socketserver.TCPServer(("",PORT), web_server)
tcp_server.serve_forever()
