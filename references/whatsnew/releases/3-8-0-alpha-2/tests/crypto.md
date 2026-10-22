# Python 3.8.0 alpha 2 / tests / crypto

[bpo-36037](https://bugs.python.org/issue?@action=redirect&bpo=36037): Repair test_ssl for a strict OpenSSL setup such as the RHEL8 strict crypto policy. When required, use an older TLS version for the server SSL context's minimum TLS version, so that a TLS version below the default minimum can be tested.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
