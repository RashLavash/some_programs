import http.server

# константы кода статуса -> http.HTTPStatus.OK 
# http.HTTPMethod.GET и т.д. - константы методов


# Создаем экземпляр сервера и записываем в переменную httpd
# httpd = http.server.HTTPServer(
#     ('', 8000), 
#     http.server.SimpleHTTPRequestHandler

# )

# def run(server_class=http.server.HTTPServer, handler_class=http.server.SimpleHTTPRequestHandler):
#     server_adress = ('', 8000)
#     httpd = server_class(server_adress, handler_class)
#     httpd.serve_forever()

# run()



def run(server_class=http.server.HTTPServer, handler_class=http.server.CGIHTTPRequestHandler):
    server_adress = ('', 8000)
    httpd = server_class(server_adress, handler_class)
    httpd.serve_forever()

run()
