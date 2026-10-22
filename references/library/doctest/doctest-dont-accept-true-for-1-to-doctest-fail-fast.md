# doctest: Doctest comparison, reporting and failure flags

### Option Flags

Several option flags govern assorted facets of doctest's behavior. The flags carry symbolic names exposed as module constants, which you may [bitwise OR](https://docs.python.org/3.14/reference/expressions.html#bitwise) together and pass into the various functions. Those same names also work inside doctest directives, and they can be fed to the doctest command line interface through the `-o` option.

The first cluster of options sets test semantics, steering how doctest judges whether actual output lines up with an example's expected output:

 doctest.DONT_ACCEPT_TRUE_FOR_1

Out of the box, when an expected output block holds only `1`, an actual output block holding only `1` or only `True` counts as a match, and the same goes for `0` against `False`. Specifying `DONT_ACCEPT_TRUE_FOR_1` rules out either substitution. The default exists because Python switched the return type of numerous functions from integer to boolean; doctests still anticipating "little integer" output keep working in those situations. This option will likely be retired someday, but not for several years yet.

 doctest.DONT_ACCEPT_BLANKLINE

Out of the box, when an expected output block has a line holding nothing but the string `<BLANKLINE>`, that line will match a blank line in the actual output. Since a truly blank line marks the boundary of the expected output, this stands as the sole means of expressing that a blank line is expected. Specifying `DONT_ACCEPT_BLANKLINE` disallows this substitution.

 doctest.NORMALIZE_WHITESPACE

With this set, every run of whitespace (blanks and newlines) is regarded as equivalent. Any whitespace run inside the expected output will match any whitespace run inside the actual output. Out of the box, whitespace has to line up exactly. `NORMALIZE_WHITESPACE` proves particularly handy when a line of expected output runs very long and you'd like to fold it over several lines in your source.

 doctest.ELLIPSIS

With this set, an ellipsis marker (`...`) within the expected output is allowed to match any substring of the actual output. That covers substrings crossing line boundaries as well as empty substrings, so keeping your use of it simple is wise. Elaborate uses can invite the same sort of "oops, it matched too much!" surprises that `.*` tends to produce in regular expressions.

 doctest.IGNORE_EXCEPTION_DETAIL

With this set, doctests anticipating exceptions pass as long as an exception of the expected type gets raised, even when the particulars (message and fully qualified exception name) fail to match.

For instance, an example anticipating `ValueError: 42` will pass when the exception actually raised is `ValueError: 3*14`, yet will fail if, for example, a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) comes up instead. It additionally overlooks any fully qualified name preceding the exception class, which may differ across Python implementations and versions and across the code/libraries involved. So all three of these variants will function with the flag set:

```pycon
>>> raise Exception('message')
Traceback (most recent call last):
Exception: message

>>> raise Exception('message')
Traceback (most recent call last):
builtins.Exception: message

>>> raise Exception('message')
Traceback (most recent call last):
__main__.Exception: message

```

Bear in mind that `ELLIPSIS` is another route to ignoring the specifics of the exception message, although such a test might yet fail depending on whether the module name shows up or lines up exactly.

Changed in version 3.2: `IGNORE_EXCEPTION_DETAIL` will, from now on, additionally disregard whatever details concern the module that holds the exception being tested.

 doctest.SKIP

With this set, skip running the example altogether. That can come in handy in settings where doctest examples double as documentation and as test cases, and where an example belongs there for documentation's sake yet shouldn't be checked. For example, the example's output could be random; or the example might lean on resources the test driver can't reach.

The SKIP flag is also serviceable for temporarily "commenting out" examples.

 doctest.COMPARISON_FLAGS

A bitmask or'ing together every comparison flag listed above.

The second cluster of options governs the way test failures get reported:

 doctest.REPORT_UDIFF

With this set, failures spanning multi-line expected and actual outputs are shown as a unified diff.

 doctest.REPORT_CDIFF

With this set, failures spanning multi-line expected and actual outputs will be shown as a context diff.

 doctest.REPORT_NDIFF

With this set, differences get computed by `difflib.Differ`, applying the same algorithm behind the well-known `ndiff.py` utility. It's the only approach that flags differences inside lines in addition to across them. As an example, when a line of expected output carries digit `1` where the actual output carries letter `l`, a line gets added bearing a caret to flag the columns that don't match.

 doctest.REPORT_ONLY_FIRST_FAILURE

With this set, show the first failing example within each doctest, while holding back output for all the rest. This keeps doctest from flagging correct examples that fall over on account of earlier failures; but it may equally conceal incorrect examples that fail on their own, apart from the first failure. With `REPORT_ONLY_FIRST_FAILURE` set, the leftover examples still get run, and still add to the overall failure tally reported; only their output is held back.

 doctest.FAIL_FAST

With this set, bail out after the first failing example and skip any attempt at the rest. Consequently, the failure count reported tops out at 1. This flag can be handy while debugging, since the examples past the first failure won't even emit any debugging output.

[Subject index](INDEX.md) · [Previous](what-about-exceptions-code-example-1-none.md) · [Continue](doctest-reporting-flags-to-doctest-register-optionflag.md) · [Owning module, declaration or section: doctest](interactive-example-testing-overview.md)
