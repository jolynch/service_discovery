# -*- coding: utf-8 -*-
from __future__ import print_function, absolute_import, division
from abc import ABCMeta, abstractmethod


class BaseServiceProvider(object):
    """The abstraction on service discovery.

    This is the interface that all providers of service discovery must provide,
    whether it be looking in a file, DNS, environment variables, or whatever
    the implementer decides. If you implement this interface, service_discovery
    can allow your clients to be discovered.
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def provide_all_service_addresses(self, service_name):
        """Provide an iterable of ServiceAddress objects"""
        raise NotImplementedError(
            'You must implement provide_all_service_addresses'
        )

    @abstractmethod
    def provide_service_address(self, service_name):
        """Provide a single ServiceAddress object corresponding to
        service_name"""
        raise NotImplementedError('You must implement provide_service_address')


class InjectableServiceProvider(object):
    """The abstraction on service discovery injection.

    This is the interface that providers of service discovery *may* provide if
    they wish to be the system used to inject.
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def inject(self, service_address):
        """Inject a single ServiceAddress into the mapping"""
        raise NotImplementedError('You must implement provide_service_address')
