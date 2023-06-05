import http.server
import socketserver
puerto = 5000

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer (("",puerto),handler) as servidor:
    print(f"Servidor levantado mediante http.server")
    servidor.serve_forever()