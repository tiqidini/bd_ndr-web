import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map.update({
    '.js': 'application/javascript',
    '.json': 'application/json',
})

print(f"Запуск серверу на порту {PORT}...")
print(f"Відкрийте браузер і перейдіть за адресою: http://localhost:{PORT}")
print("Для зупинки серверу натисніть Ctrl+C")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever() 