# What's New In Python 3.3 / nntplib — socket

The `nntplib.NNTP` class gained support for the context management protocol, which unconditionally absorbs [`socket.error`](https://docs.python.org/3.14/library/socket.html#socket.error) exceptions and tears down the NNTP connection once finished:

```python
>>> from nntplib import NNTP
>>> with NNTP('news.gmane.org') as n:
...     n.group('gmane.comp.python.committers')
...
('211 1755 1 1755 gmane.comp.python.committers', 1755, 1, 1755, 'gmane.comp.python.committers')
>>>

```

(Contributed by Giampaolo Rodol?? in [bpo-9795](https://bugs.python.org/issue?@action=redirect&bpo=9795).)

[Subject index](INDEX.md) · [Next source section](os.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](multiprocessing.md) · [Preceding release/subject continuation](multiprocessing.md)
