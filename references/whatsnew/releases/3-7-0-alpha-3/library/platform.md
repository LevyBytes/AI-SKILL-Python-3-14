# Python 3.7.0 alpha 3 / library / platform

[bpo-28684](https://bugs.python.org/issue?@action=redirect&bpo=28684): Here the freshly added test.support.skip_unless_bind_unix_socket() decorator skips asyncio tests that break because the platform offers no working bind() for unix domain sockets (as happens for non root users on the newer Android versions now running SELinux in enforcing mode).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
