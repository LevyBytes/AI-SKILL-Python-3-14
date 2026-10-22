# Python 3.5.0 alpha 1 / library / zipfile

[bpo-14315](https://bugs.python.org/issue?@action=redirect&bpo=14315): Extra fields in the central directory that are too short to parse are now skipped by the zipfile module rather than letting a struct.unpack error propagate, since such ?bad data? shows up in plenty of real world zip files in the wild and other zip tools simply ignore it.

[bpo-22219](https://bugs.python.org/issue?@action=redirect&bpo=22219): The zipfile module CLI now records entries for directories, empty ones included, inside the ZIP file.

[bpo-22217](https://bugs.python.org/issue?@action=redirect&bpo=22217): Reprs were implemented for the classes within the zipfile module.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
