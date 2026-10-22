# Python 3.6.0 alpha 1 / library / squashed bug within c implementation ordereddict move to end led segmentation fault

[bpo-25406](https://bugs.python.org/issue?@action=redirect&bpo=25406): Squashed a bug within the C implementation of OrderedDict.move_to_end() that led to a segmentation fault or a hang while iterating after several items had been shuffled to the front of an ordered dict.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
