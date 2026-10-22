# Python 3.5.1 release candidate 1 / library / corrected bug within c implementation ordereddict move to end brought segmentation fault

[bpo-25406](https://bugs.python.org/issue?@action=redirect&bpo=25406): Corrected a bug within the C implementation of OrderedDict.move_to_end() that brought on a segmentation fault or hang while iterating after several items had been moved to the front of an ordered dict.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
