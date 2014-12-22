# -*- coding: utf-8 -*-
from __future__ import print_function, absolute_import, division


class ServiceAddress(object):

    @classmethod
    def from_host_port(cls, service_name, host_port, provenance='Unknown'):
        host, port = host_port.split(':')
        return cls(service_name, host, port, provenance)

    def __init__(self, service_name, host, port, provenance='Unknown'):
        self.service_name = service_name
        self.host = host
        self.port = int(port)
        self.provenance = provenance

    def get_host_port(self):
        return '{host}:{port}'.format(host=self.host, port=self.port)

    def __eq__(self, other):
        return (
            other.service_name == self.service_name and
            other.host == self.host and
            other.port == self.port
        )

    def __repr__(self):
        return '[{0}] @ {1}:{2} ({3})'.format(
            self.service_name, self.host, self.port, self.provenance
        )
