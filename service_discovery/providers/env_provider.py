# -*- coding: utf-8 -*-
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
        if env is None:
            env = os.environ

        self.services = {}
        injection_map = env.get('SERVICE_INJECT_MAP')

        injections = injection_map.split('%')
        for injection in injections:
            service_name, service_host_ports = injection.split('?')
            self.services[service_name] = [
                ServiceAddress.from_host_port(service_name, host_port) for
                host_port in service_host_ports.split(',')
            ]


    def provide_all_service_addresses(self, service_name):
        return self.services[service_name]


    def provide_service_address(self, service_name):
        return self.services[service_name][0]
