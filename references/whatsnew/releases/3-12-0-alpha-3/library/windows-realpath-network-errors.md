# Python 3.12.0 alpha 3 / library / windows realpath network errors

[bpo-44817](https://bugs.python.org/issue?@action=redirect&bpo=44817): Disregard WinError 53 (ERROR_BAD_NETPATH), 65 (ERROR_NETWORK_ACCESS_DENIED) and 161 (ERROR_BAD_PATHNAME) while running ntpath.realpath().

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
