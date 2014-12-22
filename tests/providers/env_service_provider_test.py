from service_discovery.providers.env_provider import EnvServiceProvider
from service_discovery.service_address import ServiceAddress


def test_injection_map():
    mock_environment = {
        'SERVICE_INJECT_MAP':
        'test_service?test_host:12%test_service2?localhost:1337'
    }

    env_services = EnvServiceProvider(env=mock_environment)

    for service in ['test_service', 'test_service2']:
        assert len(env_services.provide_all_service_addresses(service)) == 1

    test_service = env_services.provide_service_address('test_service')
    assert test_service == ServiceAddress('test_service', 'test_host', 12)


def test_service_override():
    mock_environment = {
        'SERVICE_INJECT_MAP': 'test_service?test_host:17'
    }

    env_services = EnvServiceProvider(env=mock_environment)
    assert len(env_services.provide_all_service_addresses('no_service')) == 0

    new_mock_environment = {
        'SERVICE_INJECT_MAP': 'test_service?test_host:17',
        'SERVICE_NO_SERVICE': 'test_host:11'
    }
    env_services = EnvServiceProvider(env=new_mock_environment)
    no_service = env_services.provide_service_address('no_service')
    assert no_service == ServiceAddress('no_service', 'test_host', 11)


def test_no_env():
    mock_environment = {}

    env_services = EnvServiceProvider(env=mock_environment)

    test_service = env_services.provide_all_service_addresses('test_service')
    assert len(test_service) == 0
    test_service = env_services.provide_service_address('test_service')
    assert test_service is None
