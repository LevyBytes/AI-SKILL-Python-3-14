# faulthandler - Issue with file descriptors

### Issue with file descriptors

`enable()`, `dump_traceback_later()` and `register()` retain the file descriptor belonging to their *file* argument. Should the file be closed and a new file reuse its file descriptor, or should [`os.dup2()`](https://docs.python.org/3.14/library/os.html#os.dup2) swap the file descriptor, the traceback ends up in some other file. Re-invoke these functions whenever the file gets swapped.

[Subject index](INDEX.md) · [Previous](faulthandler-register-to-faulthandler-unregister.md) · [Continue](example.md) · [Owning module, declaration or section: faulthandler](faulthandler-dump-the-python-traceback.md)
