# Python 3.6.0 alpha 3 / build / platform

[bpo-23968](https://bugs.python.org/issue?@action=redirect&bpo=23968): Renamed the platform directory, turning plat-$(MACHDEP) into plat-$(PLATFORM_TRIPLET). The config directory (LIBPL) likewise went from config-$(LDVERSION) to config-$(LDVERSION)-$(PLATFORM_TRIPLET). The platform-specific _sysconfigdata module is installed into the platform directory and renamed so it carries the ABIFLAGS.

- Skip largefile support on GNU/Hurd.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
