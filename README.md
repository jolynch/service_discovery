Service Discovery
=================
This library is intended to provide an abstraction on services running
in a SOA.

It provides two main functions:
1) A fixed interface for services to call as part of service discovery
2) A plug and play provider system for providing #1

Interface
---------

At its core service discovery is about an interface:

A few objects:

ServiceDiscovery
----------------

``init()``: Initialized the service discovery subsystem
``inject_service(address)``:
``get_service_address(service_name, provider=None)``
``get_all_service_addresses(service_name, provider=None)``

ServiceAddress
--------------
``service_name``
``host``
``port``
``get_host_port``

ServiceProvider
---------------
These are the mechanisms by which we return addresses to the ServiceDiscovery
class
