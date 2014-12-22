# -*- coding: utf-8 -*-
from __future__ import print_function, absolute_import, division
from service_discovery.providers.env_provider import EnvServiceProvider
from service_discovery.errors import (
    ServiceDiscoveryInitError, ServiceDiscoveryError
)


class ServiceDiscovery(object):
    PROVIDER_CLASSES = [EnvServiceProvider]
    INJECTOR_PROVIDER_INDEX = 0

    __initialized = False

    @classmethod
    def init(cls):
        try:
            cls.providers = [provider() for provider in cls.PROVIDER_CLASSES]
            cls.__initialized = True
        except Exception as exp:
            cls.__initialized = False
            raise ServiceDiscoveryInitError(exp)

    @classmethod
    def inject_service(cls, service_address):
        try:
            if not cls.__initialized:
                cls.init()
            cls.providers[cls.INJECTOR_PROVIDER_INDEX].inject(
                service_address
            )
        except Exception as exp:
            raise ServiceDiscoveryError(exp)

    @classmethod
    def _query_providers(cls, service_name, method_name):
        try:
            if not cls.__initialized:
                cls.init()
            for provider in cls.providers:
                provider_response = getattr(provider, method_name)(
                    service_name
                )
                print(provider_response)
                if provider_response:
                    return provider_response
            raise Exception('Could not find {0}'.format(service_name))
        except Exception as exp:
            raise ServiceDiscoveryError(exp)

    @classmethod
    def get_all_service_addresses(cls, service_name):
        return cls._query_providers(
            service_name, 'provide_all_service_addresses'
        )

    @classmethod
    def get_service_address(cls, service_name):
        return cls._query_providers(
            service_name, 'provide_service_address'
        )
