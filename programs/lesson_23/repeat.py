import http.server


def run(server_class=http.server.HTTPServer, handler_class=http.server.SimpleHTTPRequestHandler):
    server_adress = ('', 8000)
    httpd = server_class(server_adress, handler_class)
    httpd.serve_forever()

run()








