# -*- coding: utf-8 -*-
from __future__ import print_function, absolute_import, division
from service_discovery.providers.base_provider import BaseServiceProvider
from service_discovery.service_address import ServiceAddress
import os


class EnvServiceProvider(BaseServiceProvider):
    """Provide services from the SERVICE_INJECT_MAP environment variable

    The map must look like:
    <service_name>?host:port,host:port...%<service_name>?host:port,host:port...

    For example:
    SERVICE_INJECT_MAP=query_lm?search2-devc:14902%federator?localhost:31337

    In addition if asked for a service not in the map SERVICE_%name% will be
    looked up, expecting the format:
    SERVICE_%name%=host:port,host:port...
    """
    def __init__(self, env=None):
        self.env = env
        if self.env is None:
            self.env = os.environ

        self.services = {}
        injection_map = self.env.get('SERVICE_INJECT_MAP', '')

        if injection_map:
            injections = injection_map.split('%')
            for injection in injections:
                service_name, service_host_ports = injection.split('?')
                addrs = EnvServiceProvider.__parse_service_injection(
                    service_name, service_host_ports
                )
                self.services[service_name] = addrs

    @staticmethod
    def __parse_service_injection(service_name, service_host_ports):
        if service_host_ports:
            return [
                ServiceAddress.from_host_port(
                    service_name, host_port, provenance=__name__
                ) for host_port in service_host_ports.split(',')
            ]
        return []

    def inject(self, service_address):
        self.services[service_address.service_name] = [service_address]
        return True

    def provide_all_service_addresses(self, service_name):
        service_addresses = self.services.get(service_name)
        if service_addresses is None:
            service_host_ports = self.env.get(
                'SERVICE_{name}'.format(name=service_name.upper()), ''
            )
            service_addresses = EnvServiceProvider.__parse_service_injection(
                service_name, service_host_ports
            )
            self.services[service_name] = service_addresses
        return service_addresses

    def provide_service_address(self, service_name):
        service_addresses = self.provide_all_service_addresses(service_name)
        if service_addresses:
            return service_addresses[0]
        return None
