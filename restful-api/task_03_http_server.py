from http.server import HTTPServer, BaseHTTPRequestHandler
import json

HOST = "localhost"
PORT = 8000


class MyHTTPHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        if (self.path == "/"):
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            response = "Hello, this is a simple API!".encode()
            self.wfile.write(response)

        elif (self.path == "/data"):
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            response = {"name": "John", "age": 30, "city": "New York"}
            data = json.dumps(response).encode("utf-8")
            self.wfile.write(data)

        elif (self.path == "/status"):
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'OK')

        elif (self.path == "/info"):
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            response = {"version": "1.0",
                        "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(response).encode("utf-8"))

        else:
            self.send_response(404)
            self.send_error(404, message="Endpoint not found")
            self.end_headers()

            response = {"error": "Endpoint not found"}
            data = json.dumps(response).encode("utf-8")
            self.wfile.write(data)


server = HTTPServer((HOST, PORT), MyHTTPHandler)
print("Server is now running")

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nShutting down server...")
    server.server_close()
