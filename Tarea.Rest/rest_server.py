from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from collections import Counter
from pprint import pprint

estudiantes = [
    {
        "id": 1,
        "nombre": "Pedrito",
        "apellido": "García",
        "carrera": "Ingeniería de Sistemas",
    },
]

class RESTRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/lista_estudiantes':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes, indent=4).encode('utf-8'))
        elif self.path == '/buscar_nombre':
            nombres_con_p = [estudiante for estudiante in estudiantes if estudiante['nombre'].startswith('P')]
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(nombres_con_p, indent=4).encode('utf-8'))
        elif self.path == '/contar_carreras':
            carreras = Counter([estudiante['carrera'] for estudiante in estudiantes])
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(dict(carreras), indent=4).encode('utf-8'))
        elif self.path == '/total_estudiantes':
            total_estudiantes = len(estudiantes)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"total_estudiantes": total_estudiantes}, indent=4).encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"Error": "Ruta no existente"}, indent=4).encode('utf-8'))
            
    def do_POST(self):
        if self.path == '/agrega_estudiante':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            post_data = json.loads(post_data.decode('utf-8'))
            carreras_existentes = [estudiante['carrera'] for estudiante in estudiantes]
            if post_data['carrera'] not in carreras_existentes:
                post_data['id'] = len(estudiantes) + 1
                estudiantes.append(post_data)
                self.send_response(201)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(estudiantes, indent=4).encode('utf-8'))
            else:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"Error": "Ya existe un estudiante con esa carrera"}, indent=4).encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"Error": "Ruta no existente"}, indent=4).encode('utf-8'))
            
def run_server(port = 8000):
    try:
        server_address = ('', port)
        httpd = HTTPServer(server_address, RESTRequestHandler)
        print(f'Iniciando servidor web en http://localhost:{port}/')
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Apagando servidor web')
        httpd.socket.close()

if __name__ == "__main__":
    run_server()
