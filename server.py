#!/usr/bin/env python3
"""
Servidor local HTTPS simples para testar o app
Execute: python3 server.py
Acesse: https://localhost:8000
"""

import http.server
import ssl
import os

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Adicionar headers necessários para PWA
        self.send_header('Service-Worker-Allowed', '/')
        self.send_header('Cache-Control', 'no-cache')
        super().end_headers()

# Criar certificado self-signed
os.system('openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes -subj "/C=BR/ST=State/L=City/O=Org/CN=localhost"')

httpd = http.server.HTTPServer(('localhost', PORT), MyHTTPRequestHandler)

# Configurar SSL
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('server.pem')
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print(f"🚀 Servidor rodando em https://localhost:{PORT}")
print(f"⚠️  Ignore o aviso de certificado não confiável (é normal para testes)")
print(f"📱 Abra no Chrome e teste o microfone!")
print(f"🛑 Ctrl+C para parar")

httpd.serve_forever()
