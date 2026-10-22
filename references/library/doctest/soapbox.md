# doctest — Soapbox

### Soapbox

As the introduction noted, `doctest` has come to serve three chief purposes:

1.

Checking examples in docstrings.

2.

Regression testing.

3.

Executable documentation / literate testing.

Each of these purposes demands different things, so telling them apart matters. Stuffing your docstrings full of cryptic test cases, especially, yields poor documentation.

As you compose a docstring, pick its examples thoughtfully. This is a craft you have to acquire — it rarely comes naturally to begin with. An example ought to genuinely enrich the documentation; a well-chosen one is frequently worth a great many words. Handled with care, your examples become priceless to your users and, over the years as things shift, repay the effort of assembling them many times over. To this day I am struck by how regularly one of my `doctest` examples breaks following a supposedly “harmless” change.

Doctest likewise shines as an instrument for regression testing, all the more so when you are generous with explanatory text. Weaving prose together with examples makes it far simpler to track exactly what is under test and the reasons for it. Should a test fail, sound prose can make the nature of the trouble and its remedy much plainer. Granted, you could lard code-based testing with lavish comments, yet hardly any programmer actually does. Plenty of people have discovered that leaning on doctest instead produces noticeably clearer tests. Maybe that is just because doctest renders writing prose a touch easier than writing code, whereas writing comments inside code is a touch harder. My own sense is that it runs deeper: the instinctive frame of mind when authoring a doctest-based test is to explain your software's subtleties and back them with examples. That, in turn, naturally yields test files that open with the most basic features and march in logical order toward complications and edge cases. The upshot is a coherent narrative rather than a heap of isolated functions probing isolated scraps of behavior at apparent random. It is a different frame of mind, it produces different outcomes, and it softens the line between testing and explaining.

Keeping regression testing within dedicated objects or files works best. You have a few ways to organize the tests:

- Put your test cases as interactive examples into text files, then run those files through `testfile()` or `DocFileSuite()`. This is the recommended route, though it comes easiest on fresh projects that were built around doctest from day one.

- Declare functions called `_regrtest_topic` whose body is a lone docstring holding the test cases for the topics they name. You may keep such functions in the module's own file or pull them out into a test file of their own.

- Set up a `__test__` dictionary that maps each regression test topic to a docstring carrying its test cases.

Once your tests sit inside a module, that module can act as its own test runner. On a failure, you can have your runner re-execute just the failing doctest while you work the problem out. Below is a bare-bones instance of such a runner:

```python
if __name__ == '__main__':
    import doctest
    flags = doctest.REPORT_NDIFF|doctest.FAIL_FAST
    if len(sys.argv) > 1:
        name = sys.argv[1]
        if name in globals():
            obj = globals()[name]
        else:
            obj = __test__[name]
        doctest.run_docstring_examples(obj, globals(), name=name,
                                       optionflags=flags)
    else:
        fail, total = doctest.testmod(optionflags=flags)
        print(f"{fail} failures out of {total} tests")

```

Footnotes

[Subject index](INDEX.md) · [Previous](doctest-doctestfailure-to-unexpectedexception-exc-info.md) · [Owning module, declaration or section: doctest](interactive-example-testing-overview.md)
