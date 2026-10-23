# What's New In Python 3.2 / unittest - re, unittest

### unittest

A batch of improvements reaches the unittest module: test discovery across packages, smoother tinkering at the interactive prompt, additional testcase methods, sharper diagnostic output when tests fail, and tidier method names.

- Running specific tests, the command-line invocation `python -m unittest` now takes file paths in place of module names ([bpo-10620](https://bugs.python.org/issue?@action=redirect&bpo=10620)). Discovery can reach into packages, picking up any test importable from the top-level directory. Use the `-t` option to name that top-level directory, `-p` to give a file-matching pattern, and `-s` to choose where discovery begins:

```shell
$ python -m unittest discover -s my_proj_dir -p _test.py

```

(Contributed by Michael Foord.)

- Tinkering at the interactive prompt becomes simpler now that the [`unittest.TestCase`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase) class accepts instantiation with no arguments:

```python
>>> from unittest import TestCase
>>> TestCase().assertEqual(pow(2, 3), 8)

```

(Contributed by Michael Foord.)

- Two fresh methods, [`assertWarns()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertWarns) and [`assertWarnsRegex()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertWarnsRegex), arrive in the [`unittest`](https://docs.python.org/3.14/library/unittest.html#module-unittest) module to confirm the code being tested raises a particular warning type:

```python
with self.assertWarns(DeprecationWarning):
    legacy_function('XYZ')

```

(Contributed by Antoine Pitrou, [bpo-9754](https://bugs.python.org/issue?@action=redirect&bpo=9754).)

Yet another addition, [`assertCountEqual()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertCountEqual), compares a pair of iterables to check that their element counts line up (the same elements appearing the same number of times, order aside):

```python
def test_anagram(self):
    self.assertCountEqual('algorithm', 'logarithm')

```

(Contributed by Raymond Hettinger.)

- One hallmark of the unittest module is its drive to deliver useful diagnostics on a failing test. Where it can, it logs the failure together with a diff of the output. That proves particularly handy when sifting through log files from failed runs. Yet because diffs can occasionally run long, a new [`maxDiff`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.maxDiff) attribute caps how many characters of diff appear.

- On top of that, the module's method names received a round of clean-ups.

Take [`assertRegex()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertRegex), the replacement label for `assertRegexpMatches()`, which carried a misleading name given that the test relies on [`re.search()`](https://docs.python.org/3.14/library/re.html#re.search) rather than [`re.match()`](https://docs.python.org/3.14/library/re.html#re.match). The other regular-expression methods now favor the shorter “Regex” spelling over “Regexp” — aligning with the labels other unittest implementations use, echoing Python’s former name for the [`re`](https://docs.python.org/3.14/library/re.html#module-re) module, and keeping the camel-casing unambiguous.

(Contributed by Raymond Hettinger and implemented by Ezio Melotti.)

- For the sake of consistency, a handful of long-established method aliases are being deprecated in favor of the names now preferred:

>
| Old Name | Preferred Name |
| --- | --- |
| `assert_()` | `assertTrue()` |
| `assertEquals()` | `assertEqual()` |
| `assertNotEquals()` | `assertNotEqual()` |
| `assertAlmostEquals()` | `assertAlmostEqual()` |
| `assertNotAlmostEquals()` | `assertNotAlmostEqual()` |

In the same vein, the `TestCase.fail*` methods that were deprecated back in Python 3.1 are slated for removal in Python 3.3.

(Contributed by Ezio Melotti; [bpo-9424](https://bugs.python.org/issue?@action=redirect&bpo=9424).)

- Deprecation hit the `assertDictContainsSubset()` method, since it was built with the arguments reversed. The mix-up bred tricky-to-debug optical illusions in which a test such as `TestCase().assertDictContainsSubset({'a':1, 'b':2}, {'a':1})` would fail.

(Contributed by Raymond Hettinger.)

[Subject index](INDEX.md) · [Previous source section](http-client.md) · [Next source section](random.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md)
