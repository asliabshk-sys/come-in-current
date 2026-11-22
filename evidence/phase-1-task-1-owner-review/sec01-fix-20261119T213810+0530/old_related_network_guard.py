import socket
def deny(*args,**kwargs):raise AssertionError('Offline related regression prohibits network')
socket.socket.connect=deny
socket.create_connection=deny
