# What's New In Python 3.3 / subprocess - subprocess

### subprocess

On posix platforms, command strings are now allowed to be bytes objects. Victor Stinner contributed this ? see [bpo-8513](https://bugs.python.org/issue?@action=redirect&bpo=8513).

The fresh [`DEVNULL`](https://docs.python.org/3.14/library/subprocess.html#subprocess.DEVNULL) constant silences output in a way that works across platforms. Ross Lagerwall landed it; refer to [bpo-5870](https://bugs.python.org/issue?@action=redirect&bpo=5870).

[Subject index](INDEX.md) · [Previous source section](struct.md) · [Next source section](sys.md) · [Release/subject declaration](summary-release-highlights.md)
