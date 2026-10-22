# What’s New in Python 2.7 / Port-Specific Changes: Windows — mimetypes, msvcrt, os, signal, winreg

### Port-Specific Changes: Windows

- A handful of constants drawn from the `crtassem.h` header file now live in the [`msvcrt`](https://docs.python.org/3.14/library/msvcrt.html#module-msvcrt) module: [`CRT_ASSEMBLY_VERSION`](https://docs.python.org/3.14/library/msvcrt.html#msvcrt.CRT_ASSEMBLY_VERSION), [`VC_ASSEMBLY_PUBLICKEYTOKEN`](https://docs.python.org/3.14/library/msvcrt.html#msvcrt.VC_ASSEMBLY_PUBLICKEYTOKEN), and [`LIBRARIES_ASSEMBLY_NAME_PREFIX`](https://docs.python.org/3.14/library/msvcrt.html#msvcrt.LIBRARIES_ASSEMBLY_NAME_PREFIX). (Contributed by David Cournapeau; [bpo-4365](https://bugs.python.org/issue?@action=redirect&bpo=4365).)

- For getting at the registry, the [`_winreg`](https://docs.python.org/3.14/library/winreg.html#module-winreg) module now supplies the [`CreateKeyEx()`](https://docs.python.org/3.14/library/winreg.html#winreg.CreateKeyEx) and [`DeleteKeyEx()`](https://docs.python.org/3.14/library/winreg.html#winreg.DeleteKeyEx) functions, which extend the formerly available functions by accepting a few additional arguments. The [`DisableReflectionKey()`](https://docs.python.org/3.14/library/winreg.html#winreg.DisableReflectionKey), [`EnableReflectionKey()`](https://docs.python.org/3.14/library/winreg.html#winreg.EnableReflectionKey), and [`QueryReflectionKey()`](https://docs.python.org/3.14/library/winreg.html#winreg.QueryReflectionKey) saw testing and documentation as well. (Implemented by Brian Curtin: [bpo-7347](https://bugs.python.org/issue?@action=redirect&bpo=7347).)

- Threads are launched through the new `_beginthreadex()` API, and the native thread-local storage functions are now in use. (Contributed by Kristján Valur Jánsson; [bpo-3582](https://bugs.python.org/issue?@action=redirect&bpo=3582).)

- On Windows the [`os.kill()`](https://docs.python.org/3.14/library/os.html#os.kill) function now functions. Its signal argument may be the [`CTRL_C_EVENT`](https://docs.python.org/3.14/library/signal.html#signal.CTRL_C_EVENT) and [`CTRL_BREAK_EVENT`](https://docs.python.org/3.14/library/signal.html#signal.CTRL_BREAK_EVENT) constants, or any integer at all. Those first two constants dispatch Control-C and Control-Break keystroke events toward subprocesses; supplying anything else routes through the `TerminateProcess()` API. (Contributed by Miki Tebeka; [bpo-1220212](https://bugs.python.org/issue?@action=redirect&bpo=1220212).)

- Given an empty path, the [`os.listdir()`](https://docs.python.org/3.14/library/os.html#os.listdir) function now fails as it should. (Fixed by Hirokazu Yamamoto; [bpo-5913](https://bugs.python.org/issue?@action=redirect&bpo=5913).)

- During initialization the [`mimetypes`](https://docs.python.org/3.14/library/mimetypes.html#module-mimetypes) module will now pull the MIME database from the Windows registry. (Patch by Gabriel Genellina; [bpo-4969](https://bugs.python.org/issue?@action=redirect&bpo=4969).)

[Subject index](INDEX.md) · [Previous source section](capsules.md) · [Next source section](port-specific-changes-mac-os-x.md) · [Release/subject declaration](the-future-for-python-2-x.md)
