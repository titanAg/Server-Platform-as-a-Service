def app(environ, start_response):
    data = b''
    with open("/var/www/log/logfile", "r") as file:
        data = bytes(file.read(), "utf-8")
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return iter([data])