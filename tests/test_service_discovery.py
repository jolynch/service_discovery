from service_discovery import ServiceDiscovery
from service_discovery.service_address import ServiceAddress
from service_discovery.errors import ServiceDiscoveryError
import pytest


def test_init():
    # Ensure no errors are thrown
    ServiceDiscovery.init()


def test_injection():
    mock_service = ServiceAddress('test_service', 'localhost', 1337, 'tests')
    ServiceDiscovery.inject_service(mock_service)
    addresses = ServiceDiscovery.get_all_service_addresses('test_service')
    address = ServiceDiscovery.get_service_address('test_service')
    assert [mock_service] == addresses
    assert mock_service == address


def test_errors():
    with pytest.raises(ServiceDiscoveryError):
        ServiceDiscovery.get_service_address('nopenopenope')
