###  1. Distributed web infrastructure
![alt text](https://raw.githubusercontent.com/Alexus91/alx-system_engineering-devops/master/0x09-web_infrastructure_design/1-distributed_web_infrastructure.png)

## Reasons for Adding Each Element:
# Web Server (Nginx):
 Nginx serves static content faster and can also handle basic load balancing, helping to improve performance and resource utilization.

# Application Server:
 The application server runs your code, processes requests, and generates dynamic content to be served.

# Load Balancer (HAProxy):
 The load balancer ensures even distribution of incoming traffic to multiple servers, preventing overload on any single server and improving fault tolerance.

# Load Balancer Configuration:
 Distribution Algorithm: The load balancer can use a round-robin algorithm, sending requests in a cyclical order to each server. This balances the load equally among servers.

# Active-Active vs. Active-Passive:
 The setup is Active-Active, where both application servers are actively receiving traffic. In an Active-Passive setup, only one server would be active, serving traffic, while the other is on standby.

# Database Primary-Replica Cluster (Master-Slave):
 How It Works: The primary (master) database handles write operations and replicates data changes to the replica (slave) database. The replica is used for read operations and backup purposes.

# Difference: 
 The primary node handles write operations, while the replica node is primarily used for read operations, reducing the load on the primary node and providing data redundancy.

## Issues with the Infrastructure:

# Single Point of Failure (SPOF):
 The infrastructure lacks redundancy. If any single component (server, load balancer, etc.) fails, it could disrupt the entire system.

# Security Issues:
 There's no mention of a firewall or HTTPS. A firewall would protect the servers from unauthorized access, and HTTPS would secure data transmission between clients and servers.

# No Monitoring:
 Without monitoring, you won't be able to identify performance bottlenecks, server failures, or other issues promptly.
