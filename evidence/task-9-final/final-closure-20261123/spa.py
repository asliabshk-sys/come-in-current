from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlsplit
from functools import partial

class SPA(SimpleHTTPRequestHandler):
    def do_GET(self):
        path = urlsplit(self.path).path
        if not Path(self.translate_path(path)).exists() and "." not in Path(path).name:
            self.path = "/index.html"
        super().do_GET()

ThreadingHTTPServer(("127.0.0.1", 8089), partial(SPA, directory="/tmp/t9-stage11-web")).serve_forever()
