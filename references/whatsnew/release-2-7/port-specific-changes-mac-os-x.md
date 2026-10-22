# What’s New in Python 2.7 / Port-Specific Changes: Mac OS X

### Port-Specific Changes: Mac OS X

- So that added packages can be shared between the system installation and a separately user-installed copy of the same version, the path `/Library/Python/2.7/site-packages` is now tacked onto `sys.path`. (Changed by Ronald Oussoren; [bpo-4865](https://bugs.python.org/issue?@action=redirect&bpo=4865).)

Changed in version 2.7.13: Starting with 2.7.13 this change was reverted. `/Library/Python/2.7/site-packages`, the site-packages directory belonging to the Apple-supplied system Python 2.7, is no longer attached to `sys.path` for user-installed Pythons such as the python.org installers. Beginning with macOS 10.12, Apple altered how the system site-packages directory gets set up, which could break installation of pip components like setuptools. Whatever packages were set up under the system Python will, from now on, not be shared with user-installed Pythons anymore. ([bpo-28440](https://bugs.python.org/issue?@action=redirect&bpo=28440))

[Subject index](INDEX.md) · [Previous source section](port-specific-changes-windows.md) · [Next source section](port-specific-changes-freebsd.md) · [Release/subject declaration](the-future-for-python-2-x.md)
