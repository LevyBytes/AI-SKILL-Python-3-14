# What’s New In Python 3.1 / New, Improved, and Deprecated Modules - functools, io, logging, logging.handlers, os, pdb, pydoc, re, runpy, sys, unittest, zipimport

(Contributed by Raymond Hettinger; [bpo-1818](https://bugs.python.org/issue?@action=redirect&bpo=1818).)

- A flags parameter is now accepted by the [`re.sub()`](https://docs.python.org/3.14/library/re.html#re.sub), [`re.subn()`](https://docs.python.org/3.14/library/re.html#re.subn) and [`re.split()`](https://docs.python.org/3.14/library/re.html#re.split) functions.

(Contributed by Gregory Smith.)

- A basic [`logging.NullHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.NullHandler) class is now provided by the [`logging`](https://docs.python.org/3.14/library/logging.html#module-logging) module, aimed at programs that skip logging themselves yet invoke library code that logs. Wiring up a null handler quiets bogus warnings of the sort “No handlers could be found for logger foo”:

```python
>>> h = logging.NullHandler()
>>> logging.getLogger("foo").addHandler(h)

```

(Contributed by Vinay Sajip; [bpo-4384](https://bugs.python.org/issue?@action=redirect&bpo=4384)).

- Backing the `-m` command line switch, the [`runpy`](https://docs.python.org/3.14/library/runpy.html#module-runpy) module can now run packages: given a package name, it hunts for a `__main__` submodule and executes it.

(Contributed by Andi Vajda; [bpo-4195](https://bugs.python.org/issue?@action=redirect&bpo=4195).)

- Source code pulled in through [`zipimport`](https://docs.python.org/3.14/library/zipimport.html#module-zipimport) (or any other compliant [**PEP 302**](https://peps.python.org/pep-0302/) loader) can now be reached and shown by the [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb) module.

(Contributed by Alexander Belopolsky; [bpo-4201](https://bugs.python.org/issue?@action=redirect&bpo=4201).)

- It is now possible to pickle [`functools.partial`](https://docs.python.org/3.14/library/functools.html#functools.partial) objects.

>

(Suggested by Antoine Pitrou and Jesse Noller. Implemented by Jack Diederich; [bpo-5228](https://bugs.python.org/issue?@action=redirect&bpo=5228).)

- Add [`pydoc`](https://docs.python.org/3.14/library/pydoc.html#module-pydoc) help topics for symbols, letting `help('@')` behave as you would expect inside the interactive environment.

(Contributed by David Laban; [bpo-4739](https://bugs.python.org/issue?@action=redirect&bpo=4739).)

- You can now have the [`unittest`](https://docs.python.org/3.14/library/unittest.html#module-unittest) module skip single tests or whole test classes. It also lets you tag a test as an expected failure, meaning one known to be broken yet not tallied as a failure against a TestResult:

```python
class TestGizmo(unittest.TestCase):

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_gizmo_on_windows(self):
        ...

    @unittest.expectedFailure
    def test_gimzo_without_required_library(self):
        ...

```

On top of that, exception tests were extended to cooperate with context managers via the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement:

```python
def test_division_by_zero(self):
    with self.assertRaises(ZeroDivisionError):
        x / 0

```

Several fresh assertion methods joined the lineup as well, among them [`assertSetEqual()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertSetEqual), [`assertDictEqual()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertDictEqual), `assertDictContainsSubset()`, [`assertListEqual()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertListEqual), [`assertTupleEqual()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertTupleEqual), [`assertSequenceEqual()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertSequenceEqual), [`assertRaisesRegexp()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertRaisesRegex), [`assertIsNone()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertIsNone), and [`assertIsNotNone()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertIsNotNone).

(Contributed by Benjamin Peterson and Antoine Pitrou.)

- Three fresh constants for the [`seek()`](https://docs.python.org/3.14/library/io.html#io.IOBase.seek) method now live in the [`io`](https://docs.python.org/3.14/library/io.html#module-io) module: [`SEEK_SET`](https://docs.python.org/3.14/library/os.html#os.SEEK_SET), [`SEEK_CUR`](https://docs.python.org/3.14/library/os.html#os.SEEK_CUR), and [`SEEK_END`](https://docs.python.org/3.14/library/os.html#os.SEEK_END).

- What was the [`sys.version_info`](https://docs.python.org/3.14/library/sys.html#sys.version_info) tuple is now a named tuple:

[Subject index](INDEX.md) · [Previous source section](standard-library-module-changes.md) · [Next source section](imap-import-and-pickle-module-changes.md) · [Release/subject declaration](pep-372-ordered-dictionaries.md) · [Release/subject declaration](standard-library-module-changes.md)
