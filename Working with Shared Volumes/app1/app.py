import random

MY_ID = random.randrange(65536)

def app(environ, start_response):
    data = b'Hello World!\n'
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    log(environ)
    return iter([data])

def log(environ):
    with open("/var/www/log/logfile", "a") as file:
        file.write('Visitor from ' + str(environ['REMOTE_ADDR']) + ' visited server ' + str(MY_ID) + '\n')