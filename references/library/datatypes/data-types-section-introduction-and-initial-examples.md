# Data Types - Section introduction and initial examples

# Datatypes

### Data Types

This chapter's modules supply an assortment of specialized data types, among them enumerations, fixed-type arrays, double-ended queues, heap queues, plus dates and times.

Python ships several built-in data types as well, notably [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict), [`list`](https://docs.python.org/3.14/library/stdtypes.html#list), [`set`](https://docs.python.org/3.14/library/stdtypes.html#set) and [`frozenset`](https://docs.python.org/3.14/library/stdtypes.html#frozenset), and [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple). Unicode strings are stored by the [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) class, whereas binary data is held by the [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) and [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) classes.

This chapter documents the modules listed below:

- [`datetime` - Basic date and time types](https://docs.python.org/3.14/library/datetime.html)
  - [Aware and naive objects](https://docs.python.org/3.14/library/datetime.html#aware-and-naive-objects)
  - [Constants](https://docs.python.org/3.14/library/datetime.html#constants)
  - [Available types](https://docs.python.org/3.14/library/datetime.html#available-types)
    - [Common properties](https://docs.python.org/3.14/library/datetime.html#common-properties)
    - [Determining if an object is aware or naive](https://docs.python.org/3.14/library/datetime.html#determining-if-an-object-is-aware-or-naive)

  - [`timedelta` objects](https://docs.python.org/3.14/library/datetime.html#timedelta-objects)
    - [Examples of usage: `timedelta`](https://docs.python.org/3.14/library/datetime.html#examples-of-usage-timedelta)

  - [`date` objects](https://docs.python.org/3.14/library/datetime.html#date-objects)
    - [Examples of usage: `date`](https://docs.python.org/3.14/library/datetime.html#examples-of-usage-date)

  - [`datetime` objects](https://docs.python.org/3.14/library/datetime.html#datetime-objects)
    - [Examples of usage: `datetime`](https://docs.python.org/3.14/library/datetime.html#examples-of-usage-datetime)

  - [`time` objects](https://docs.python.org/3.14/library/datetime.html#time-objects)
    - [Examples of usage: `time`](https://docs.python.org/3.14/library/datetime.html#examples-of-usage-time)

  - [`tzinfo` objects](https://docs.python.org/3.14/library/datetime.html#tzinfo-objects)
  - [`timezone` objects](https://docs.python.org/3.14/library/datetime.html#timezone-objects)
  - [`strftime()` and `strptime()` behavior](https://docs.python.org/3.14/library/datetime.html#strftime-and-strptime-behavior)
    - [`strftime()` and `strptime()` format codes](https://docs.python.org/3.14/library/datetime.html#strftime-and-strptime-format-codes)
    - [Technical detail](https://docs.python.org/3.14/library/datetime.html#technical-detail)

- [`zoneinfo` - IANA time zone support](https://docs.python.org/3.14/library/zoneinfo.html)
  - [Using `ZoneInfo`](https://docs.python.org/3.14/library/zoneinfo.html#using-zoneinfo)
  - [Data sources](https://docs.python.org/3.14/library/zoneinfo.html#data-sources)
    - [Configuring the data sources](https://docs.python.org/3.14/library/zoneinfo.html#configuring-the-data-sources)
      - [Compile-time configuration](https://docs.python.org/3.14/library/zoneinfo.html#compile-time-configuration)
      - [Environment configuration](https://docs.python.org/3.14/library/zoneinfo.html#environment-configuration)
      - [Runtime configuration](https://docs.python.org/3.14/library/zoneinfo.html#runtime-configuration)

  - [The `ZoneInfo` class](https://docs.python.org/3.14/library/zoneinfo.html#the-zoneinfo-class)
    - [String representations](https://docs.python.org/3.14/library/zoneinfo.html#string-representations)
    - [Pickle serialization](https://docs.python.org/3.14/library/zoneinfo.html#pickle-serialization)

  - [Functions](https://docs.python.org/3.14/library/zoneinfo.html#functions)
  - [Globals](https://docs.python.org/3.14/library/zoneinfo.html#globals)
  - [Exceptions and warnings](https://docs.python.org/3.14/library/zoneinfo.html#exceptions-and-warnings)

- [`calendar` - General calendar-related functions](https://docs.python.org/3.14/library/calendar.html)
  - [Command-line usage](https://docs.python.org/3.14/library/calendar.html#command-line-usage)

- [`collections` - Container datatypes](https://docs.python.org/3.14/library/collections.html)
  - [`ChainMap` objects](https://docs.python.org/3.14/library/collections.html#chainmap-objects)
    - [`ChainMap` Examples and Recipes](https://docs.python.org/3.14/library/collections.html#chainmap-examples-and-recipes)

  - [`Counter` objects](https://docs.python.org/3.14/library/collections.html#counter-objects)
  - [`deque` objects](https://docs.python.org/3.14/library/collections.html#deque-objects)
    - [`deque` Recipes](https://docs.python.org/3.14/library/collections.html#deque-recipes)

  - [`defaultdict` objects](https://docs.python.org/3.14/library/collections.html#defaultdict-objects)
    - [`defaultdict` Examples](https://docs.python.org/3.14/library/collections.html#defaultdict-examples)

  - [`namedtuple()` Factory Function for Tuples with Named Fields](https://docs.python.org/3.14/library/collections.html#namedtuple-factory-function-for-tuples-with-named-fields)
  - [`OrderedDict` objects](https://docs.python.org/3.14/library/collections.html#ordereddict-objects)
    - [`OrderedDict` Examples and Recipes](https://docs.python.org/3.14/library/collections.html#ordereddict-examples-and-recipes)

  - [`UserDict` objects](https://docs.python.org/3.14/library/collections.html#userdict-objects)
  - [`UserList` objects](https://docs.python.org/3.14/library/collections.html#userlist-objects)
  - [`UserString` objects](https://docs.python.org/3.14/library/collections.html#userstring-objects)

- [`collections.abc` - Abstract Base Classes for Containers](https://docs.python.org/3.14/library/collections.abc.html)
  - [Collections Abstract Base Classes](https://docs.python.org/3.14/library/collections.abc.html#collections-abstract-base-classes)
  - [Collections Abstract Base Classes – Detailed Descriptions](https://docs.python.org/3.14/library/collections.abc.html#collections-abstract-base-classes-detailed-descriptions)
  - [Examples and Recipes](https://docs.python.org/3.14/library/collections.abc.html#examples-and-recipes)

- [`heapq` - Heap queue algorithm](https://docs.python.org/3.14/library/heapq.html)
  - [Basic Examples](https://docs.python.org/3.14/library/heapq.html#basic-examples)
  - [Other Applications](https://docs.python.org/3.14/library/heapq.html#other-applications)
  - [Priority Queue Implementation Notes](https://docs.python.org/3.14/library/heapq.html#priority-queue-implementation-notes)
  - [Theory](https://docs.python.org/3.14/library/heapq.html#theory)

[Subject index](INDEX.md) · [Continue](data-types.md)
