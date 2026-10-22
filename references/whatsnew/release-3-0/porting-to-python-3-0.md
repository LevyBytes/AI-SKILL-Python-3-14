# What's New In Python 3.0 / Porting To Python 3.0

### Porting To Python 3.0

When moving existing Python 2.5 or 2.6 code over to Python 3.0, the recommended plan of attack runs as follows:

1.

(Prerequisite:) Start with excellent test coverage.

2.

Move first to Python 2.6. Doing so ought to take no more effort than a typical step from one Python 2.x release to the next 2.(x+1) one. Confirm that every test still passes.

3.

(Remaining on 2.6:) Flip on the `-3` command-line flag, which surfaces warnings for anything destined to disappear from or change in 3.0. Execute the test suite once more and keep correcting the flagged code until not a single warning remains and the whole suite continues to pass.

4.

Pass your whole source tree through the `2to3` source-to-source converter, then execute what it produces under Python 3.0. Patch whatever problems linger by hand, continuing until the tests are green once more.

Attempting to craft a single body of source that runs untouched on both Python 2.6 and 3.0 is discouraged; pulling it off would force an awfully twisted style — steering clear of `print` statements, metaclasses, and a good deal more. If your job is keeping a library working on both Python 2.6 and Python 3.0, the soundest route is to adjust step 3 above by making your edits in the 2.6 copy and re-running the `2to3` translator, instead of changing the 3.0 copy directly.

If it is C extensions you need to move to Python 3.0, consult [Porting Extension Modules to Python 3](https://docs.python.org/3.14/howto/cporting.html#cporting-howto).

[Subject index](INDEX.md) · [Previous source section](performance.md) · [Release/subject declaration](common-stumbling-blocks.md)
