from service_discovery.service_address import ServiceAddress

def test_contract():
    service_address = ServiceAddress('test_service', 'localhost', 1234)
    assert service_address.service_name == 'test_service'
    assert service_address.host == 'localhost'
    assert service_address.port == 1234
    assert service_address.get_host_port() == 'localhost:1234'
