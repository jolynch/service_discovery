# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

class BaseServiceProvider(object):
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
