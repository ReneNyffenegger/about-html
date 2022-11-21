#
#   https://gist.github.com/kainam00/39c8d5876027e38f112d6f07c785bb56
#
#!/usr/bin/env python

from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
import time

class DelayedHTTPResponse(BaseHTTPRequestHandler):

    def do_GET(s):
        print("GETting " + s.path)

        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        s.wfile.write(b"""<!DOCTYPE html>
<html>
<head>
<title>Javascript test</title>
</head>
<body>
<script>
  alert('hello world');
</script>
""");

        s.wfile.flush()

        for i in range(1, 10):
            time.sleep(1)
            s.wfile.write(bytes(str(i), 'latin1') + b" second(s) later.<br>")
            s.wfile.flush();

        s.wfile.write(b"</body></html>");

server_address = ('', 8080) # 8080 is the port on which the server listens
httpd = HTTPServer(server_address, DelayedHTTPResponse)

try:                                               
    httpd.serve_forever()                          
except KeyboardInterrupt:                          
    pass                                           

httpd.server_close()
