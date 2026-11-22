"""Pytest-only fail-closed network guard for reviewed offline test selection."""
import socket

def _blocked(*args, **kwargs):
    raise AssertionError('Network access is forbidden in the offline regression process')

def pytest_configure(config):
    socket.socket.connect = _blocked
    socket.socket.connect_ex = _blocked
    socket.create_connection = _blocked

