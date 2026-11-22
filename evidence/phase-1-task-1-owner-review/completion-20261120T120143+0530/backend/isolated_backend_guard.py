"""Only this run's loopback API and retained loopback MongoDB may connect."""
import os
import socket
import dotenv

_connect=socket.socket.connect
_connect_ex=socket.socket.connect_ex
def allowed(address):
    return isinstance(address,tuple) and len(address)>=2 and address[0] in {'127.0.0.1','localhost','::1'} and int(address[1]) in {27018,int(os.environ.get('COMEIN_VALIDATION_PORT','0'))}
def connect(sock,address):
    if not allowed(address):raise AssertionError('Only isolated loopback MongoDB/backend sockets are authorized')
    return _connect(sock,address)
def connect_ex(sock,address):
    if not allowed(address):raise AssertionError('Only isolated loopback MongoDB/backend sockets are authorized')
    return _connect_ex(sock,address)
def install():
    dotenv.load_dotenv=lambda *args,**kwargs:False
    socket.socket.connect=connect
    socket.socket.connect_ex=connect_ex
def pytest_configure(config):install()
