# Python 3.11.0 alpha 2 / build / build and platforms

[bpo-45536](https://bugs.python.org/issue?@action=redirect&bpo=45536): The `configure` script verifies that the OpenSSL headers and libraries expose the APIs that are needed. It checks the most common APIs. The probe flags an OpenSSL that is missing or out of date. A failure will not halt configure.

[bpo-45405](https://bugs.python.org/issue?@action=redirect&bpo=45405): Stop the `internal configure error` from occurring when `configure` runs under recent non-Apple clang releases. David Bohman contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
