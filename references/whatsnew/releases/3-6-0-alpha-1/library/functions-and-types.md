# Python 3.6.0 alpha 1 / library / functions and types

[bpo-25691](https://bugs.python.org/issue?@action=redirect&bpo=25691): Repaired a crash triggered by deleting ElementTree.Element attributes.

[bpo-6973](https://bugs.python.org/issue?@action=redirect&bpo=6973): Once a subprocess.Popen process is known to have terminated, the send_signal(), terminate(), and kill() methods are barred from taking any action, since they might otherwise signal some unrelated process.

[bpo-25287](https://bugs.python.org/issue?@action=redirect&bpo=25287): Refrain from putting crypt.METHOD_CRYPT into crypt.methods whenever it lacks support. A support check is performed first, because on OpenBSD, for instance, it might be unsupported.

[bpo-26177](https://bugs.python.org/issue?@action=redirect&bpo=26177): Repaired the keys() method for the Canvas and Scrollbar widgets.

[bpo-26335](https://bugs.python.org/issue?@action=redirect&bpo=26335): mmap.write() now reports the count of bytes written, in line with other write methods. Jakub Stasiak contributed the patch.

[bpo-26457](https://bugs.python.org/issue?@action=redirect&bpo=26457): Corrected the subnets() methods on the IP network classes for situations where the resulting prefix length equals the maximal prefix length. This builds on a patch from Xiang Zhang.

[bpo-26186](https://bugs.python.org/issue?@action=redirect&bpo=26186): Took out an invalid type check from importlib.util.LazyLoader.

[bpo-26733](https://bugs.python.org/issue?@action=redirect&bpo=26733): Class and static methods are now included when a class gets disassembled. Xiang Zhang contributed the patch.

[bpo-13248](https://bugs.python.org/issue?@action=redirect&bpo=13248): The deprecated inspect.getmoduleinfo function was removed.

[bpo-26050](https://bugs.python.org/issue?@action=redirect&bpo=26050): The asyncio.StreamReader.readuntil() method was added. Марк Коренберг contributed this patch.

[bpo-25447](https://bugs.python.org/issue?@action=redirect&bpo=25447): Copying the lru_cache() wrapper object now always succeeds regardless of the wrapped object's type, since the original object is returned unchanged.

[bpo-26711](https://bugs.python.org/issue?@action=redirect&bpo=26711): Corrected how plistlib.Data compares against values of other types.

[bpo-25788](https://bugs.python.org/issue?@action=redirect&bpo=25788): An "errors" argument is now accepted by fileinput.hook_encoded() to forward on to open. Joseph Hackman wrote the original patch.

[bpo-23804](https://bugs.python.org/issue?@action=redirect&bpo=23804): Corrected the SSL recv(0) and read(0) methods so they yield zero bytes instead of as many as 1024.

[bpo-26616](https://bugs.python.org/issue?@action=redirect&bpo=26616): Corrected a defect in the datetime.astimezone() method.

[bpo-26499](https://bugs.python.org/issue?@action=redirect&bpo=26499): Took the remaining Content-Length into account within HTTPResponse.readline() and read1(). This builds on a patch from Silent Ghost. It is also now documented that HTTPResponse offers these methods.

[bpo-27031](https://bugs.python.org/issue?@action=redirect&bpo=27031): Drop the dummy methods from the Tkinter widget classes: tk_menuBar() and tk_bindForTraversal().

[bpo-27033](https://bugs.python.org/issue?@action=redirect&bpo=27033): For the smtpd.SMTPChannel and smtpd.SMTPServer constructors, the decode_data parameter now defaults to False.

[bpo-27034](https://bugs.python.org/issue?@action=redirect&bpo=27034): Drop the deprecated asynchat.fifo class.

[bpo-27040](https://bugs.python.org/issue?@action=redirect&bpo=27040): Added the loop.get_exception_handler method

[bpo-25590](https://bugs.python.org/issue?@action=redirect&bpo=25590): The Readline completer now invokes getattr() a single time for each attribute. It also fills in attribute names such as properties and slots that dir() reports yet have not been created on an instance.

[bpo-26202](https://bugs.python.org/issue?@action=redirect&bpo=26202): copy.deepcopy() now copies range() objects that carry non-atomic attributes correctly.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
