import http.server
import json
import os

PORT = int(os.environ.get("PORT", 8000))
VERSION = os.environ.get("APP_VERSION", "unknown")


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            body = json.dumps({"status": "ok", "version": VERSION}).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
        else:
            body = b"Hello, devstuffs!"
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    server = http.server.HTTPServer(("0.0.0.0", PORT), Handler)
    print(f"Serving version {VERSION} on port {PORT}")
    server.serve_forever()
