# What’s New In Python 3.8 / Deprecated

### Deprecated

- The distutils `bdist_wininst` command is now deprecated; reach for `bdist_wheel` (wheel packages) instead. (Contributed by Victor Stinner in [bpo-37481](https://bugs.python.org/issue?@action=redirect&bpo=37481).)

- Inside the [`ElementTree`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#module-xml.etree.ElementTree) module, the deprecated `getchildren()` and `getiterator()` methods now raise a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) rather than a [`PendingDeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#PendingDeprecationWarning). Their removal is scheduled for Python 3.9. (Contributed by Serhiy Storchaka in [bpo-29209](https://bugs.python.org/issue?@action=redirect&bpo=29209).)

- Handing [`loop.set_default_executor()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.set_default_executor) an object that is not an instance of [`concurrent.futures.ThreadPoolExecutor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor) is deprecated and will be forbidden in Python 3.9. (Contributed by Elvis Pranskevichus in [bpo-34075](https://bugs.python.org/issue?@action=redirect&bpo=34075).)

- The [`__getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getitem__) methods of [`xml.dom.pulldom.DOMEventStream`](https://docs.python.org/3.14/library/xml.dom.pulldom.html#xml.dom.pulldom.DOMEventStream), [`wsgiref.util.FileWrapper`](https://docs.python.org/3.14/library/wsgiref.html#wsgiref.util.FileWrapper) and [`fileinput.FileInput`](https://docs.python.org/3.14/library/fileinput.html#fileinput.FileInput) have been deprecated.

Those implementations had been disregarding their *index* parameter and handing back the next item regardless. (Contributed by Berker Peksag in [bpo-9372](https://bugs.python.org/issue?@action=redirect&bpo=9372).)

- Within the [`typing.NamedTuple`](https://docs.python.org/3.14/library/typing.html#typing.NamedTuple) class, the `_field_types` attribute is now deprecated; prefer the `__annotations__` attribute, which carries identical data. (Contributed by Raymond Hettinger in [bpo-36320](https://bugs.python.org/issue?@action=redirect&bpo=36320).)

- The [`ast`](https://docs.python.org/3.14/library/ast.html#module-ast) classes `Num`, `Str`, `Bytes`, `NameConstant` and `Ellipsis` are now treated as deprecated and are slated for removal in upcoming Python releases. Use [`Constant`](https://docs.python.org/3.14/library/ast.html#ast.Constant) in their place. (Contributed by Serhiy Storchaka in [bpo-32892](https://bugs.python.org/issue?@action=redirect&bpo=32892).)

- The [`ast.NodeVisitor`](https://docs.python.org/3.14/library/ast.html#ast.NodeVisitor) methods `visit_Num()`, `visit_Str()`, `visit_Bytes()`, `visit_NameConstant()` and `visit_Ellipsis()` are deprecated as of now and will no longer be invoked in later Python releases. Define the [`visit_Constant()`](https://docs.python.org/3.14/library/ast.html#ast.NodeVisitor.visit_Constant) method so every constant node is handled. (Contributed by Serhiy Storchaka in [bpo-36917](https://bugs.python.org/issue?@action=redirect&bpo=36917).)

- The `@asyncio.coroutine` [decorator](https://docs.python.org/3.14/glossary.html#term-decorator) is deprecated and slated to disappear in version 3.10. Rather than `@asyncio.coroutine`, write [`async def`](https://docs.python.org/3.14/reference/compound_stmts.html#async-def) instead. (Contributed by Andrew Svetlov in [bpo-36921](https://bugs.python.org/issue?@action=redirect&bpo=36921).)

- Throughout [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio), explicitly handing in a *loop* argument is now deprecated and is set for removal in version 3.10 across these: [`asyncio.sleep()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.sleep), [`asyncio.gather()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.gather), [`asyncio.shield()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.shield), [`asyncio.wait_for()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.wait_for), [`asyncio.wait()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.wait), [`asyncio.as_completed()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.as_completed), [`asyncio.Task`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task), [`asyncio.Lock`](https://docs.python.org/3.14/library/asyncio-sync.html#asyncio.Lock), [`asyncio.Event`](https://docs.python.org/3.14/library/asyncio-sync.html#asyncio.Event), [`asyncio.Condition`](https://docs.python.org/3.14/library/asyncio-sync.html#asyncio.Condition), [`asyncio.Semaphore`](https://docs.python.org/3.14/library/asyncio-sync.html#asyncio.Semaphore), [`asyncio.BoundedSemaphore`](https://docs.python.org/3.14/library/asyncio-sync.html#asyncio.BoundedSemaphore), [`asyncio.Queue`](https://docs.python.org/3.14/library/asyncio-queue.html#asyncio.Queue), [`asyncio.create_subprocess_exec()`](https://docs.python.org/3.14/library/asyncio-subprocess.html#asyncio.create_subprocess_exec), and [`asyncio.create_subprocess_shell()`](https://docs.python.org/3.14/library/asyncio-subprocess.html#asyncio.create_subprocess_shell).

- Handing coroutine objects to [`asyncio.wait()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.wait) explicitly is now deprecated and is set to be removed in version 3.11. (Contributed by Yury Selivanov in [bpo-34790](https://bugs.python.org/issue?@action=redirect&bpo=34790).)

- These functions and methods within the [`gettext`](https://docs.python.org/3.14/library/gettext.html#module-gettext) module are deprecated: `lgettext()`, `ldgettext()`, `lngettext()` and `ldngettext()`. Because they hand back encoded bytes, you may run into surprising Unicode-related exceptions whenever the translated strings carry encoding problems. Preferring alternatives that yield Unicode strings in Python 3 is far better. These functions have stayed broken for a long stretch.

The `bind_textdomain_codeset()` function, the `NullTranslations.output_charset()` and `NullTranslations.set_output_charset()` methods, plus the *codeset* parameter accepted by the [`translation()`](https://docs.python.org/3.14/library/gettext.html#gettext.translation) and [`install()`](https://docs.python.org/3.14/library/gettext.html#gettext.install) functions are deprecated too, given that their only role supports the `l*gettext()` functions. (Contributed by Serhiy Storchaka in [bpo-33710](https://bugs.python.org/issue?@action=redirect&bpo=33710).)

- The `isAlive()` method of [`threading.Thread`](https://docs.python.org/3.14/library/threading.html#threading.Thread) has been deprecated. (Contributed by Donghee Na in [bpo-35283](https://bugs.python.org/issue?@action=redirect&bpo=35283).)

- A great many builtin and extension functions taking integer arguments will now raise a deprecation warning for [`Decimal`](https://docs.python.org/3.14/library/decimal.html#decimal.Decimal)s, [`Fraction`](https://docs.python.org/3.14/library/fractions.html#fractions.Fraction)s and any other object convertible to an integer only with a loss (for example, one that offers the [`__int__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__int__) method yet lacks the [`__index__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__) method). They will become errors in a future version. (Contributed by Serhiy Storchaka in [bpo-36048](https://bugs.python.org/issue?@action=redirect&bpo=36048).)

- Deprecated passing the following arguments as keyword arguments:

  - *func* in [`functools.partialmethod()`](https://docs.python.org/3.14/library/functools.html#functools.partialmethod), [`weakref.finalize()`](https://docs.python.org/3.14/library/weakref.html#weakref.finalize), [`profile.Profile.runcall()`](https://docs.python.org/3.14/library/profile.html#profile.Profile.runcall), `cProfile.Profile.runcall()`, [`bdb.Bdb.runcall()`](https://docs.python.org/3.14/library/bdb.html#bdb.Bdb.runcall), [`trace.Trace.runfunc()`](https://docs.python.org/3.14/library/trace.html#trace.Trace.runfunc) and [`curses.wrapper()`](https://docs.python.org/3.14/library/curses.html#curses.wrapper).

  - *function* in [`unittest.TestCase.addCleanup()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.addCleanup).

  - *fn* in the [`submit()`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.Executor.submit) method of [`concurrent.futures.ThreadPoolExecutor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor) and [`concurrent.futures.ProcessPoolExecutor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor).

  - *callback* in [`contextlib.ExitStack.callback()`](https://docs.python.org/3.14/library/contextlib.html#contextlib.ExitStack.callback), `contextlib.AsyncExitStack.callback()` and [`contextlib.AsyncExitStack.push_async_callback()`](https://docs.python.org/3.14/library/contextlib.html#contextlib.AsyncExitStack.push_async_callback).

  - *c* and *typeid* in the `create()` method of `multiprocessing.managers.Server` and `multiprocessing.managers.SharedMemoryServer`.

  -

*obj* in [`weakref.finalize()`](https://docs.python.org/3.14/library/weakref.html#weakref.finalize).

Across upcoming Python releases, each of these will turn [positional-only](https://docs.python.org/3.14/glossary.html#positional-only-parameter). (Contributed by Serhiy Storchaka in [bpo-36492](https://bugs.python.org/issue?@action=redirect&bpo=36492).)

[Subject index](INDEX.md) · [Previous source section](build-and-c-api-changes.md) · [Release/subject declaration](assignment-expressions.md) · [Next source section](api-and-feature-removals.md)
