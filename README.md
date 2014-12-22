Service Discovery
=================

*Please don't rely on this yet, this is a WIP code base.*

This library is intended to provide an abstraction on services running
in a SOA. This is *not* a service discovery system, for that see 
[smartstack](http://nerds.airbnb.com/smartstack-service-discovery-cloud/),
[consul](https://consul.io/),
[curator](http://curator.apache.org/curator-x-discovery/index.html),
[eureka](https://github.com/Netflix/eureka), or your other favorite discovery
system.

The idea would be that no matter which service discovery system your org chooses
to roll out you can use this service discovery interface to access them, and
then create provider plugins for your favorite discovery system.

It provides two main functions:
1. A fixed interface for services to call as part of service discovery
2. A plug and play provider system for providing #1

Interface
---------
At its core service discovery is about an interface:

A few objects:

ServiceDiscovery
----------------

``init()``: Initialized the service discovery subsystem

``inject_service(address)``:

``get_service_address(service_name)``

``get_all_service_addresses(service_name)``

ServiceAddress
--------------
``service_name``

``host``

``port``

``get_host_port``

ServiceProvider
---------------
These are the mechanisms by which we return addresses to the ServiceDiscovery
class, they implement a similar interface to ServiceDiscovery just without
injection.
