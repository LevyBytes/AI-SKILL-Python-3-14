# What's New In Python 3.11 / Removed — asyncio-eventloop, binascii, fileinput, gettext, inspect, wsgiref, xml.dom.pulldom

### Removed

Here is the roster of Python APIs taken out in Python 3.11.

The removed C APIs appear in their own section.

- Gone is the `@asyncio.coroutine()` [decorator](https://docs.python.org/3.14/glossary.html#term-decorator) that let old generator-based coroutines interoperate with [`async`](https://docs.python.org/3.14/reference/compound_stmts.html#async) / [`await`](https://docs.python.org/3.14/reference/expressions.html#await) code. That function carried a deprecation since Python 3.8 and had originally been targeted for removal in Python 3.10. Reach for [`async def`](https://docs.python.org/3.14/reference/compound_stmts.html#async-def) instead. (Contributed by Illia Volochii in [bpo-43216](https://bugs.python.org/issue?@action=redirect&bpo=43216).)

- Gone too is `asyncio.coroutines.CoroWrapper`, which wrapped old generator-based coroutine objects while in debug mode. (Contributed by Illia Volochii in [bpo-43216](https://bugs.python.org/issue?@action=redirect&bpo=43216).)

- On serious security grounds, the *reuse_address* parameter of [`asyncio.loop.create_datagram_endpoint()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_datagram_endpoint), which had been turned off in Python 3.9, is gone entirely now. The driver is how the `SO_REUSEADDR` socket option acts under UDP. (Contributed by Hugo van Kemenade in [bpo-45129](https://bugs.python.org/issue?@action=redirect&bpo=45129).)

- Gone is the `binhex` module, which Python 3.9 deprecated. Alongside it went the related, likewise-deprecated [`binascii`](https://docs.python.org/3.14/library/binascii.html#module-binascii) functions:

  - `binascii.a2b_hqx()`

  - `binascii.b2a_hqx()`

  - `binascii.rlecode_hqx()`

  - `binascii.rldecode_hqx()`

You can still use the [`binascii.crc_hqx()`](https://docs.python.org/3.14/library/binascii.html#binascii.crc_hqx) function.

(Contributed by Victor Stinner in [bpo-45085](https://bugs.python.org/issue?@action=redirect&bpo=45085).)

- Gone is the `distutils` `bdist_msi` command that Python 3.9 deprecated. Use `bdist_wheel` (wheel packages) instead. (Contributed by Hugo van Kemenade in [bpo-45124](https://bugs.python.org/issue?@action=redirect&bpo=45124).)

- Gone are the [`__getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getitem__) methods on [`xml.dom.pulldom.DOMEventStream`](https://docs.python.org/3.14/library/xml.dom.pulldom.html#xml.dom.pulldom.DOMEventStream), [`wsgiref.util.FileWrapper`](https://docs.python.org/3.14/library/wsgiref.html#wsgiref.util.FileWrapper) and [`fileinput.FileInput`](https://docs.python.org/3.14/library/fileinput.html#fileinput.FileInput), which were deprecated as of Python 3.9. (Contributed by Hugo van Kemenade in [bpo-45132](https://bugs.python.org/issue?@action=redirect&bpo=45132).)

- Gone are the deprecated [`gettext`](https://docs.python.org/3.14/library/gettext.html#module-gettext) functions `lgettext()`, `ldgettext()`, `lngettext()` and `ldngettext()`. Also taken out: the `bind_textdomain_codeset()` function, both the `NullTranslations.output_charset()` and `NullTranslations.set_output_charset()` methods, plus the *codeset* parameter on `translation()` and `install()`, since the `l*gettext()` functions alone relied on them. (Contributed by Donghee Na and Serhiy Storchaka in [bpo-44235](https://bugs.python.org/issue?@action=redirect&bpo=44235).)

- Pulled out of the [`inspect`](https://docs.python.org/3.14/library/inspect.html#module-inspect) module:

  - The `getargspec()` function, deprecated as of Python 3.0; turn to [`inspect.signature()`](https://docs.python.org/3.14/library/inspect.html#inspect.signature) or [`inspect.getfullargspec()`](https://docs.python.org/3.14/library/inspect.html#inspect.getfullargspec) instead.

  - The `formatargspec()` function, deprecated as of Python 3.5; turn to the [`inspect.signature()`](https://docs.python.org/3.14/library/inspect.html#inspect.signature) function or the [`inspect.Signature`](https://docs.python.org/3.14/library/inspect.html#inspect.Signature) object directly.

  - The undocumented `Signature.from_builtin()` and `Signature.from_function()` methods, deprecated as of Python 3.5; turn to the [`Signature.from_callable()`](https://docs.python.org/3.14/library/inspect.html#inspect.Signature.from_callable) method instead.

(Contributed by Hugo van Kemenade in [bpo-45320](https://bugs.python.org/issue?@action=redirect&bpo=45320).)

- Dropped the [`__class_getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__class_getitem__) method from [`pathlib.PurePath`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath); it served no purpose and had been added accidentally in earlier releases. (Contributed by Nikita Sobolev in [bpo-46483](https://bugs.python.org/issue?@action=redirect&bpo=46483).)

- Dropped the `MailmanProxy` class from the `smtpd` module, since it cannot function without the third-party `mailman` package. (Contributed by Donghee Na in [bpo-35800](https://bugs.python.org/issue?@action=redirect&bpo=35800).)

- Dropped the deprecated `split()` method belonging to `_tkinter.TkappType`. (Contributed by Erlend E. Aasland in [bpo-38371](https://bugs.python.org/issue?@action=redirect&bpo=38371).)

- Dropped namespace package support from [`unittest`](https://docs.python.org/3.14/library/unittest.html#module-unittest) discovery. The feature arrived in Python 3.4 yet has been non-functional ever since Python 3.7. (Contributed by Inada Naoki in [bpo-23882](https://bugs.python.org/issue?@action=redirect&bpo=23882).)

- Dropped the undocumented private `float.__set_format__()` method, which went by the name `float.__setformat__()` back in Python 3.7. Its docstring read as follows:

> “You probably don’t want to use this function. It exists mainly to be used in Python’s test suite.” (Contributed by Victor Stinner in [bpo-46852](https://bugs.python.org/issue?@action=redirect&bpo=46852).)

- Both the `--experimental-isolated-subinterpreters` configure flag and the matching `EXPERIMENTAL_ISOLATED_SUBINTERPRETERS` macro are gone.

- [Pynche](https://pypi.org/project/Pynche/) — The Pythonically Natural Color and Hue Editor — left `Tools/scripts` and is now [being developed independently](https://gitlab.com/warsaw/pynche/-/tree/main) from the Python source tree.

[Subject index](INDEX.md) · [Previous source section](pending-removal-in-python-3-12.md) · [Release/subject declaration](summary-release-highlights.md) · [Next source section](porting-to-python-3-11.md)
