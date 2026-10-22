# Audit events table — socket

| Audit event | Arguments | References |
| --- | --- | --- |
| socket.__new__ | `self`, `family`, `type`, `protocol` | [1] |
| socket.bind | `self`, `address` | [1] |
| socket.connect | `self`, `address` | [1][2] |
| socket.getaddrinfo | `host`, `port`, `family`, `type`, `protocol` | [1] |
| socket.gethostbyaddr | `ip_address` | [1] |
| socket.gethostbyname | `hostname` | [1][2] |
| socket.gethostname |  | [1] |
| socket.getnameinfo | `sockaddr` | [1] |
| socket.getservbyname | `servicename`, `protocolname` | [1] |
| socket.getservbyport | `port`, `protocolname` | [1] |
| socket.sendmsg | `self`, `address` | [1] |
| socket.sendto | `self`, `address` | [1] |
| socket.sethostname | `name` | [1] |

[Subject index](INDEX.md) · [Previous](audit-events-table-smtplib.md) · [Continue](audit-events-table-sqlite3.md) · [Owning module, declaration or section: Audit events table](audit-events-table-section-introduction-and-initial-examples.md)
