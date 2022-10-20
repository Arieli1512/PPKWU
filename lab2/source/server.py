#!/usr/bin/env python3
import http.server
import socketserver
import os
import time

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
            if self.path == '/?cmd=time':
                self.protocol_version = 'HTTP/1.1'
                self.send_response(200)
                self.send_header("Content-type", "text/html; charset=UTF-8")
                self.end_headers()        
                self.wfile.write(bytes(time.strftime("%H:%M:%S"), "utf-8"))
            else:
                param = self.path.split('&')
                cmd = param[0]
                cmd = cmd[2:].split('=')
                str = param[1].split('=')
                super().do_GET()
                if cmd[1] == 'rev' and str[0] == 'str':
                    self.protocol_version = 'HTTP/1.1'
                    self.send_response(200)
                    self.send_header("Content-type", "text/html; charset=UTF-8")
                    self.end_headers()     
                    self.wfile.write(str[1][::-1].encode())
                else:
                    super().do_GET()

    
# --- main ---

PORT = 4080
time.tzset()
os.environ["TZ"] = "Europe/Warsaw"
print(f'Starting: http://localhost:{PORT}')

tcp_server = socketserver.TCPServer(("",PORT), web_server)
tcp_server.serve_forever()
