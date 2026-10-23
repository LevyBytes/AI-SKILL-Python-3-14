# What's New In Python 3.10 / threading - threading

### threading

Add [`threading.gettrace()`](https://docs.python.org/3.14/library/threading.html#threading.gettrace) and [`threading.getprofile()`](https://docs.python.org/3.14/library/threading.html#threading.getprofile) to read back the functions installed via [`threading.settrace()`](https://docs.python.org/3.14/library/threading.html#threading.settrace) and [`threading.setprofile()`](https://docs.python.org/3.14/library/threading.html#threading.setprofile) respectively. (Contributed by Mario Corchero in [bpo-42251](https://bugs.python.org/issue?@action=redirect&bpo=42251).)

Add [`threading.__excepthook__`](https://docs.python.org/3.14/library/threading.html#threading.__excepthook__) so that the original value of [`threading.excepthook()`](https://docs.python.org/3.14/library/threading.html#threading.excepthook) can be recovered should it get replaced by a broken or otherwise different value. (Contributed by Mario Corchero in [bpo-42308](https://bugs.python.org/issue?@action=redirect&bpo=42308).)

[Subject index](INDEX.md) · [Previous source section](thread.md) · [Next source section](traceback.md) · [Release/subject declaration](summary-release-highlights.md)
