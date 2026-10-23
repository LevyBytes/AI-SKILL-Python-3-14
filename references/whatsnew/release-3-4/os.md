# What's New In Python 3.4 / os - multiprocessing, os, os.path

### os

Fresh functions let you read and write the [inheritable flag](https://docs.python.org/3.14/library/os.html#fd-inheritance) of a file descriptor ([`os.get_inheritable()`](https://docs.python.org/3.14/library/os.html#os.get_inheritable), [`os.set_inheritable()`](https://docs.python.org/3.14/library/os.html#os.set_inheritable)) or of a Windows handle ([`os.get_handle_inheritable()`](https://docs.python.org/3.14/library/os.html#os.get_handle_inheritable), [`os.set_handle_inheritable()`](https://docs.python.org/3.14/library/os.html#os.set_handle_inheritable)).

The fresh function [`cpu_count()`](https://docs.python.org/3.14/library/os.html#os.cpu_count) tells you how many CPUs the platform running Python has on hand (or `None` when that figure cannot be worked out). The [`multiprocessing.cpu_count()`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.cpu_count) function is now built on top of it). (Contributed by Trent Nelson, Yogesh Chaudhari, Victor Stinner, and Charles-François Natali in [bpo-17914](https://bugs.python.org/issue?@action=redirect&bpo=17914).)

[`os.path.samestat()`](https://docs.python.org/3.14/library/os.path.html#os.path.samestat) works on the Windows platform now (and the [`os.path.samefile()`](https://docs.python.org/3.14/library/os.path.html#os.path.samefile) implementation is shared across Unix and Windows). (Contributed by Brian Curtin in [bpo-11939](https://bugs.python.org/issue?@action=redirect&bpo=11939).)

[`os.path.ismount()`](https://docs.python.org/3.14/library/os.path.html#os.path.ismount) detects volumes mounted underneath a drive root on Windows. (Contributed by Tim Golden in [bpo-9035](https://bugs.python.org/issue?@action=redirect&bpo=9035).)

[`os.open()`](https://docs.python.org/3.14/library/os.html#os.open) accepts two extra flags where the platform offers them, [`O_PATH`](https://docs.python.org/3.14/library/os.html#os.O_PATH) (an un-opened file descriptor) and [`O_TMPFILE`](https://docs.python.org/3.14/library/os.html#os.O_TMPFILE) (an unnamed temporary file; at the 3.4.0 release only on Linux machines whose kernel is version 3.11 or later and ship uapi headers). (Contributed by Christian Heimes in [bpo-18673](https://bugs.python.org/issue?@action=redirect&bpo=18673) and Benjamin Peterson, respectively.)

[Subject index](INDEX.md) · [Previous source section](operator.md) · [Next source section](pdb.md) · [Release/subject declaration](release-highlights.md)
