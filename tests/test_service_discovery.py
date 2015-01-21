from service_discovery import ServiceDiscovery
from service_discovery.service_address import ServiceAddress
from service_discovery.errors import ServiceDiscoveryError
import pytest


class TestServiceDiscovery(object):
    def setup_method(self, method):
        ServiceDiscovery.reset()

    def test_init(self):
        assert not ServiceDiscovery.is_initialized()
        ServiceDiscovery.init()
        assert ServiceDiscovery.is_initialized()

    def test_injection(self):
        assert not ServiceDiscovery.is_initialized()
        mock_service = ServiceAddress(
            'test_service', 'localhost', 1337, 'tests'
        )
        ServiceDiscovery.inject_service(mock_service)

        addresses = ServiceDiscovery.get_all_service_addresses('test_service')
        address = ServiceDiscovery.get_service_address('test_service')
        assert [mock_service] == addresses
        assert mock_service == address

    def test_errors(self):
        assert not ServiceDiscovery.is_initialized()
        with pytest.raises(ServiceDiscoveryError):
            ServiceDiscovery.get_service_address('nopenopenope')
