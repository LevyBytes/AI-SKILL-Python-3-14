# What’s New In Python 3.5 / signal — enum, signal

### signal

Under Windows, the [`set_wakeup_fd()`](https://docs.python.org/3.14/library/signal.html#signal.set_wakeup_fd) function will now handle socket handles as well. Victor Stinner landed this (see [bpo-22018](https://bugs.python.org/issue?@action=redirect&bpo=22018)).

Inside the [`signal`](https://docs.python.org/3.14/library/signal.html#module-signal) module, the assorted `SIG*` constants have been turned into [`Enums`](https://docs.python.org/3.14/library/enum.html#module-enum). As a result, debugging output shows readable names rather than integer “magic numbers”. Giampaolo Rodola’ made this change (see [bpo-21076](https://bugs.python.org/issue?@action=redirect&bpo=21076)).

[Subject index](INDEX.md) · [Previous source section](shutil.md) · [Next source section](smtpd.md) · [Release/subject declaration](summary-release-highlights.md)
