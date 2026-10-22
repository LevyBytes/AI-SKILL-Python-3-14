# Python 3.8.0 alpha 2 / tests / skip test shutil test unpack archive xztar memoryerror avoided bit aix whenever maxdata setting

[bpo-35704](https://bugs.python.org/issue?@action=redirect&bpo=35704): Skip `test_shutil.test_unpack_archive_xztar` so a MemoryError is avoided on 32-bit AIX whenever the MAXDATA setting falls below 0x20000000.

Patch by Michael Felt (aixtools)

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
