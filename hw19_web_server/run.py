import socket

from jinja2 import Environment, FileSystemLoader, TemplateNotFound

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)


def start_web_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 5000))
    server.listen()

    try:
        while True:
            print('Server waiting...')
            client, client_addr = server.accept()
            request = client.recv(4096).decode()
            print(f'Client data : {request}')
            content = load_page_from_request(request)
            client.send(content)
            client.shutdown(socket.SHUT_WR)

    except KeyboardInterrupt:
        server.close()
        print('Shutdown server')


def load_page_from_request(request):
    try:
        path = request.split(' ')[1]
    except IndexError:
        path = '/'

    if path == '/':
        path = 'home.html'

    try:

        template = env.get_template(path)
        output = template.render()
        if "Accept: text/css,*/*;q=0.1" in request:
            with open('templates' + path, 'rb') as file:
                response = file.read()
            return HEADERS_CSS.encode() + response
        return HEADERS_OK.encode() + output.encode()
    except (FileNotFoundError, TemplateNotFound):
        return (HEADERS_404 + '<h1>Sorry, page is not found...</h1>').encode()


HEADERS_OK = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset-utf-8\r\n\r\n'
HEADERS_404 = 'HTTP/1.1 404 OK\r\nContent-Type: text/html; charset-utf-8\r\n\r\n'
HEADERS_CSS = 'HTTP/1.1 200 OK\r\nContent-Type: text/css; charset-utf-8\r\n\r\n'
HEADERS_IMAGE = 'HTTP/1.1 200 OK\r\nContent-Type: image/png; charset-utf-8\r\n\r\n'

if __name__ == '__main__':
    start_web_server()
