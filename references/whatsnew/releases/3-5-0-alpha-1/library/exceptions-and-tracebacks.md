# Python 3.5.0 alpha 1 / library / exceptions and tracebacks

[bpo-21883](https://bugs.python.org/issue?@action=redirect&bpo=21883): For unsupported or mismatched argument types, os.path.join() and os.path.relpath() now raise a TypeError carrying a more helpful error message.

[bpo-21775](https://bugs.python.org/issue?@action=redirect&bpo=21775): shutil.copytree(): the crash while copying onto VFAT was fixed. The exception handler had presumed every OSError object carries a "winerror" attribute, which is false, so the handler itself raised AttributeError on Linux (and, presumably, any other non-Windows OS). Greg Ward supplied the patch.

[bpo-19385](https://bugs.python.org/issue?@action=redirect&bpo=19385): Whenever a dbm.dumb database is closed, operations on it now consistently raise one and the same exception.

[bpo-21326](https://bugs.python.org/issue?@action=redirect&bpo=21326): A new is_closed() method was added to asyncio.BaseEventLoop. Once the event loop has been closed, the run_forever() and run_until_complete() methods of asyncio.BaseEventLoop now throw an exception.

[bpo-21677](https://bugs.python.org/issue?@action=redirect&bpo=21677): Chaining of nonnormalized exceptions inside io close() methods was fixed.

[bpo-16382](https://bugs.python.org/issue?@action=redirect&bpo=16382): The exception message produced by warnings.warn() for an invalid category was improved. Phil Elson contributed the first patch.

[bpo-15114](https://bugs.python.org/issue?@action=redirect&bpo=15114): The strict mode plus its argument on HTMLParser, the HTMLParser.error method, and the HTMLParserError exception were all dropped.

[bpo-16133](https://bugs.python.org/issue?@action=redirect&bpo=16133): BlockingIOError exceptions are now disregarded by the asynchat.async_chat.handle_read() method.

[bpo-20539](https://bugs.python.org/issue?@action=redirect&bpo=20539): Made the math.factorial error message better for large positive inputs, and for large negative inputs switched the exception type (OverflowError -> ValueError).

[bpo-22042](https://bugs.python.org/issue?@action=redirect&bpo=22042): Should the file descriptor be in blocking mode, signal.set_wakeup_fd(fd) now throws an exception.

[bpo-23353](https://bugs.python.org/issue?@action=redirect&bpo=23353): Repaired how generators handle exceptions inside PyEval_EvalFrameEx(). On entry, the exception state is saved or swapped even when PyEval_EvalFrameEx() runs with throwflag=0. On exit, that state is now always restored or swapped, no longer just when why equals WHY_YIELD or WHY_RETURN. This patch was co-written with Antoine Pitrou.

[bpo-20980](https://bugs.python.org/issue?@action=redirect&bpo=20980): No longer wraps the exception during use of ThreadPool.

[bpo-21817](https://bugs.python.org/issue?@action=redirect&bpo=21817): Whenever a task handed to a ProcessPoolExecutor raises, the parent process now shows the remote traceback. Claudiu Popa supplied the patch.

[bpo-22384](https://bugs.python.org/issue?@action=redirect&bpo=22384): An exception inside a Tkinter callback no longer crashes the program when it runs under pythonw.exe.

[bpo-11558](https://bugs.python.org/issue?@action=redirect&bpo=11558): When `attach` runs against a message whose `is_multipart` is False, `email.message.Message.attach` now yields a more helpful error message.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
