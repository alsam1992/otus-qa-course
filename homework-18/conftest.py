"""Module with fixtures for tests"""
import socket
import sys
from collections import OrderedDict
import pytest


class Http:
    """Http thought socket class"""

    def __init__(self, url, method, header, port):
        self.url = url
        self.method = method
        self.header = header
        self.port = int(port)
        self.connection = None
        self.reply = None

    def create_socket(self):
        """create socket"""
        try:
            self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            return self.connection
        except socket.error:
            print('Failed to create socket')
            sys.exit()

    def connect_server(self):
        """Connect to remote server"""
        print('# Connecting to server, ' + self.url)
        self.connection.connect((self.url, self.port))

    def send_data(self):
        """Send data to remote server"""
        print('# Sending data to server')
        request = b''
        request += b'GET'
        request += b' / '
        request += b'HTTP/1.0\r\n'
        request += b'\r\n'
        try:
            self.connection.sendall(request)
        except socket.error:
            print("Send failed")
            sys.exit()

    def receive_data(self):
        """Receive data"""
        print('# Receive data from server')
        self.reply = self.connection.recv(4096)
        return self.reply

    def get_header(self):
        """Get header"""
        data = self.reply.split(b'\r\n\r\n\n')
        data.pop()
        data = data[0]
        print("----------")
        print("Header: ", data)
        return data

    def get_retcodes(self):
        """Get return codes"""
        data = self.reply.split(b'\r\n\r\n\n')
        data.pop()
        data = data[0]
        header = data.decode()
        result = header.splitlines()
        retcode = result[0].split(' ')[1]
        retresult = result[0].split(' ')[2]
        print("-------------")
        print("Return code:", retcode)
        print("Return result:", retresult)
        return retcode, retresult

    def get_headers(self):
        """Get geaders"""
        data = self.reply.split(b'\r\n\r\n\n')
        data.pop()
        data = data[0]
        header = data.decode()
        headers = OrderedDict([i.split(': ') for i in header.splitlines()[1:]])
        print("-------------")
        for key, value in headers.items():
            print(key, ':', value)
        return headers


def pytest_addoption(parser):
    """Addoption"""
    parser.addoption("--url", action="store", default="127.0.0.1", help="Host IP")
    parser.addoption("--method", action="store", default="GET", help="http method")
    parser.addoption("--header", action="store", default="HTTP/1.0", help="http header")
    parser.addoption("--port", action="store", default=80, help="connection port")


@pytest.fixture
def cmdopt_url(request):
    """url fixture"""
    return request.config.getoption("--url")


@pytest.fixture
def cmdopt_method(request):
    """method fixture"""
    return request.config.getoption("--method")


@pytest.fixture
def cmdopt_header(request):
    """header fixture"""
    return request.config.getoption("--header")


@pytest.fixture
def cmdopt_port(request):
    """port fixture"""
    return request.config.getoption("--port")


@pytest.fixture
def http(cmdopt_url, cmdopt_method, cmdopt_header, cmdopt_port):
    """http thought fixture"""
    r = Http(cmdopt_url, cmdopt_method, cmdopt_header, cmdopt_port)
    r.create_socket()
    r.connect_server()
    r.send_data()
    r.receive_data()
    header = r.get_header()
    retcode, retresult = r.get_retcodes()
    headers = r.get_headers()
    return header, retcode, retresult, headers
