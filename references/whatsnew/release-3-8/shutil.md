# What’s New In Python 3.8 / shutil — shutil, tarfile

### shutil

[`shutil.copytree()`](https://docs.python.org/3.14/library/shutil.html#shutil.copytree) henceforth takes a fresh `dirs_exist_ok` keyword argument. (Contributed by Josh Bronson in [bpo-20849](https://bugs.python.org/issue?@action=redirect&bpo=20849).)

[`shutil.make_archive()`](https://docs.python.org/3.14/library/shutil.html#shutil.make_archive) henceforth produces fresh archives using the current pax (POSIX.1-2001) format by default, boosting portability and standards conformance, a change carried over from the matching update to the [`tarfile`](https://docs.python.org/3.14/library/tarfile.html#module-tarfile) module. (Contributed by C.A.M. Gerlach in [bpo-30661](https://bugs.python.org/issue?@action=redirect&bpo=30661).)

Under Windows, [`shutil.rmtree()`](https://docs.python.org/3.14/library/shutil.html#shutil.rmtree) henceforth deletes directory junctions without first recursively clearing out their contents. (Contributed by Steve Dower in [bpo-37834](https://bugs.python.org/issue?@action=redirect&bpo=37834).)

[Subject index](INDEX.md) · [Previous source section](shlex.md) · [Next source section](socket.md) · [Release/subject declaration](assignment-expressions.md)
