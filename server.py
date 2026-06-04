#!/usr/bin/env python3
import http.server
import socketserver
import os
from pathlib import Path

# Mudar para o diretório do projeto
os.chdir(Path(__file__).parent)

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Adicionar headers para evitar cache
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def do_GET(self):
        # Redirecionar URLs sem extensão para index.html
        if self.path.endswith('/'):
            self.path += 'index.html'
        return super().do_GET()

if __name__ == '__main__':
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"Servidor rodando em http://localhost:{PORT}/")
        print(f"Pressione Ctrl+C para parar")
        httpd.serve_forever()
