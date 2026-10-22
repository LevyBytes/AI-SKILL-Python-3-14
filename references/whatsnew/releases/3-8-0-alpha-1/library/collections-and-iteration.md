# Python 3.8.0 alpha 1 / library / collections and iteration

[bpo-27494](https://bugs.python.org/issue?@action=redirect&bpo=27494): Reverted [bpo-27494](https://bugs.python.org/issue?@action=redirect&bpo=27494). 2to3 now rejects a trailing comma within generator expressions.

[bpo-34010](https://bugs.python.org/issue?@action=redirect&bpo=34010): Repaired a speed regression while reading streams via tarfile. The buffered read ought to accumulate in a list rather than appending onto a bytes object.

[bpo-32221](https://bugs.python.org/issue?@action=redirect&bpo=32221): A range of functions that hand back a tuple holding IPv6 addresses now drop the `%scope` portion, because that same detail already lives in the *scopeid* tuple item. This particularly accelerates `socket.recvfrom()` for multicast packets, since the pointless lookup of the network interface name gets skipped.

[bpo-32852](https://bugs.python.org/issue?@action=redirect&bpo=32852): Ensure sys.argv stays a list while running trace.

[bpo-34610](https://bugs.python.org/issue?@action=redirect&bpo=34610): Corrected the iterator of `multiprocessing.managers.DictProxy`.

[bpo-34970](https://bugs.python.org/issue?@action=redirect&bpo=34970): Guarded the weak set of tasks against unsafe manipulation inside `asyncio.all_tasks()`

[bpo-32929](https://bugs.python.org/issue?@action=redirect&bpo=32929): Drop the tri-state parameter "hash" and introduce the boolean "unsafe_hash". With unsafe_hash set True, a __hash__ function gets added, yet when a __hash__ already exists, raise TypeError. With unsafe_hash set False, add a __hash__ derived from the values of eq= and frozen=. The unsafe_hash=False behavior matches the former hash=None behavior. unsafe_hash=False is the default, exactly as hash=None previously was.

[bpo-33224](https://bugs.python.org/issue?@action=redirect&bpo=33224): Update difflib.mdiff() to suit [**PEP 479**](https://peps.python.org/pep-0479/). Turn an uncaught StopIteration inside a generator into a return-statement.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
