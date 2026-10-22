# Python 3.5.0 alpha 1 / library / compiler and parser

[bpo-21448](https://bugs.python.org/issue?@action=redirect&bpo=21448): To dodge *O*(*n*2) behavior while parsing a long line, FeedParser feed() was changed. Raymond Hettinger contributed the first patch.

[bpo-21486](https://bugs.python.org/issue?@action=redirect&bpo=21486): Netmask parsing within ipaddress.IPv4Network and ipaddress.IPv6Network was optimized.

[bpo-21311](https://bugs.python.org/issue?@action=redirect&bpo=21311): Steer clear of an exception in _osx_support under non-standard compiler configurations. John Szakmeister wrote the patch.

[bpo-19380](https://bugs.python.org/issue?@action=redirect&bpo=19380): Parsing of regular expressions was optimized.

[bpo-22783](https://bugs.python.org/issue?@action=redirect&bpo=22783): When feasible, pickling now emits the NEWOBJ opcode rather than the NEWOBJ_EX opcode.

[bpo-19858](https://bugs.python.org/issue?@action=redirect&bpo=19858): pickletools.optimize() now recognizes the MEMOIZE opcode, so it yields more compact results and stops producing invalid output when the input mixes MEMOIZE opcodes with PUT or BINPUT opcodes.

[bpo-21476](https://bugs.python.org/issue?@action=redirect&bpo=21476): The TextIOWrapper used by email.parser.BytesParser is now discarded once parsing finishes, so the input file does not get closed unexpectedly.

[bpo-22915](https://bugs.python.org/issue?@action=redirect&bpo=22915): The SAX parser now handles files that were opened with a file descriptor or a bytes path.

[bpo-22796](https://bugs.python.org/issue?@action=redirect&bpo=22796): To guard against possible injection attacks, HTTP cookie parsing is now stricter.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
