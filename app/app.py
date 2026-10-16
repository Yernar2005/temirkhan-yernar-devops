
import os
from http.server import BaseHTTPRequestHandler, HTTPServer


NAME = os.getenv("STUDENT_NAME", "Yernar")
SURNAME = os.getenv("STUDENT_SURNAME", "Temirkhan")
GROUP = os.getenv("STUDENT_GROUP", "IT2-2314")
STUDENT_ID = os.getenv("STUDENT_ID", "37722")


BANNER = f"""================================
DevOps Student Application
================================
Name: {NAME}
Surname: {SURNAME}
Group: {GROUP}
Student ID: {STUDENT_ID}
Application is running successfully!"""

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(BANNER.encode())

    def log_message(self, fmt, *args):
        print("Request:", self.address_string(), fmt % args, flush=True)



print(BANNER, flush=True)
HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
