"""Only ephemeral loopback backend/Mongo sockets;never load actual dotenv files."""
import os
import socket
import dotenv

_original_connect=socket.socket.connect
_original_connect_ex=socket.socket.connect_ex

def _allowed(address):
    if not isinstance(address,tuple) or len(address)<2:return False
    host,port=address[:2]
    return host in {'localhost','127.0.0.1','::1'} and int(port) in {27018,int(os.environ.get('COMEIN_VALIDATION_PORT','0'))}

def _connect(sock,address):
    if not _allowed(address):raise AssertionError('Only the isolated loopback MongoDB/backend sockets are authorized')
    return _original_connect(sock,address)

def _connect_ex(sock,address):
    if not _allowed(address):raise AssertionError('Only the isolated loopback MongoDB/backend sockets are authorized')
    return _original_connect_ex(sock,address)

def install():
    dotenv.load_dotenv=lambda *args,**kwargs:False
    socket.socket.connect=_connect
    socket.socket.connect_ex=_connect_ex

def pytest_configure(config):install()

