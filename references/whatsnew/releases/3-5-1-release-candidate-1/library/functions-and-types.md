# Python 3.5.1 release candidate 1 / library / functions and types

[bpo-6973](https://bugs.python.org/issue?@action=redirect&bpo=6973): Once we know that a subprocess.Popen process has died, the send_signal(), terminate(), and kill() methods are barred from doing anything, since they might otherwise signal some other process.

[bpo-25590](https://bugs.python.org/issue?@action=redirect&bpo=25590): Inside the Readline completer, getattr() is now invoked just once for each attribute.

[bpo-22958](https://bugs.python.org/issue?@action=redirect&bpo=22958): Both the constructor and the update method of weakref.WeakValueDictionary now take the self and the dict keyword arguments.

[bpo-22609](https://bugs.python.org/issue?@action=redirect&bpo=22609): The constructor of collections.UserDict now takes the self keyword argument.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
