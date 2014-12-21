# -*- coding: utf-8 -*-

class ServiceAddress(object):

    @classmethod
    def from_host_port(cls, service_name, host_port):
        host, port = host_port.split(':')
        return cls(service_name, host, port)

    def __init__(self, service_name, host, port):
        self.service_name = service_name
        self.host = host
        self.port = int(port)

    def get_host_port(self):
        return '{host}:{port}'.format(host=self.host, port=self.port)

    def __eq__(self, other):
        return (
            other.service_name == self.service_name and
            other.host == self.host and
            other.port == self.port
        )
