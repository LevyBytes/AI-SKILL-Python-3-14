# What's New In Python 3.7 / re - copy, re

### re

You can now set the [`re.ASCII`](https://docs.python.org/3.14/library/re.html#re.ASCII), [`re.LOCALE`](https://docs.python.org/3.14/library/re.html#re.LOCALE) and [`re.UNICODE`](https://docs.python.org/3.14/library/re.html#re.UNICODE) flags within the scope of a group. (Contributed by Serhiy Storchaka in [bpo-31690](https://bugs.python.org/issue?@action=redirect&bpo=31690).)

[`re.split()`](https://docs.python.org/3.14/library/re.html#re.split) will now split on a pattern such as `r'\b'`, `'^$'` or `(?=-)` that matches the empty string. (Contributed by Serhiy Storchaka in [bpo-25054](https://bugs.python.org/issue?@action=redirect&bpo=25054).)

Regular expressions built with the [`re.LOCALE`](https://docs.python.org/3.14/library/re.html#re.LOCALE) flag no longer rely on the locale as they compile. The locale settings take effect solely when the compiled regular expression runs. (Contributed by Serhiy Storchaka in [bpo-30215](https://bugs.python.org/issue?@action=redirect&bpo=30215).)

A [`FutureWarning`](https://docs.python.org/3.14/library/exceptions.html#FutureWarning) now fires whenever a regular expression holds character set constructs whose meaning is slated to shift later on, for instance nested sets together with set operations. (Contributed by Serhiy Storchaka in [bpo-30349](https://bugs.python.org/issue?@action=redirect&bpo=30349).)

You can now duplicate compiled regular expression and match objects via [`copy.copy()`](https://docs.python.org/3.14/library/copy.html#copy.copy) and [`copy.deepcopy()`](https://docs.python.org/3.14/library/copy.html#copy.deepcopy). (Contributed by Serhiy Storchaka in [bpo-10076](https://bugs.python.org/issue?@action=redirect&bpo=10076).)

[Subject index](INDEX.md) · [Previous source section](queue.md) · [Next source section](signal.md) · [Release/subject declaration](summary-release-highlights.md)
