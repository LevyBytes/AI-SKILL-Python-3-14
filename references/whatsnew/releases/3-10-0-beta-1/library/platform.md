# Python 3.10.0 beta 1 / library / platform

[bpo-43284](https://bugs.python.org/issue?@action=redirect&bpo=43284): platform.win32_ver pulls the windows version from sys.getwindowsversion().platform_version, which itself takes the version off kernel32.dll (a file whose version can differ from that of Windows proper). For that reason platform.win32_ver was changed to compute the version through the platform module's _syscmd_ver private function, yielding an accurate version.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
