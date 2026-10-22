# What's New In Python 3.11 / CPython bytecode changes — dis

### CPython bytecode changes

Inline cache entries now live in the bytecode as the freshly-introduced [`CACHE`](https://docs.python.org/3.14/library/dis.html#opcode-CACHE) instructions. A given opcode often demands a precise count of caches afterward and tells the interpreter to step past them while running. Because filled caches may resemble ordinary instructions, treat raw, adaptive bytecode that holds quickened data very carefully when you read or alter it.

[Subject index](INDEX.md) · [Previous source section](about.md) · [Next source section](new-opcodes.md) · [Release/subject declaration](summary-release-highlights.md)
