# What's New In Python 3.3 / sched - sched, time

### sched

- [`run()`](https://docs.python.org/3.14/library/sched.html#sched.scheduler.run) now takes a *blocking* parameter; passing false tells the method to fire whichever scheduled events are nearest to expiring (should there be any) and then come back at once. That suits situations where you wish to drive the [`scheduler`](https://docs.python.org/3.14/library/sched.html#sched.scheduler) from non-blocking applications. (Contributed by Giampaolo Rodol?? in [bpo-13449](https://bugs.python.org/issue?@action=redirect&bpo=13449).)

- The [`scheduler`](https://docs.python.org/3.14/library/sched.html#sched.scheduler) class is now safe to share across multi-threaded environments. (Contributed by Josiah Carlson and Giampaolo Rodol?? in [bpo-8684](https://bugs.python.org/issue?@action=redirect&bpo=8684).)

- The *timefunc* and *delayfunct* parameters on the [`scheduler`](https://docs.python.org/3.14/library/sched.html#sched.scheduler) class constructor became optional, defaulting respectively to [`time.time()`](https://docs.python.org/3.14/library/time.html#time.time) and [`time.sleep()`](https://docs.python.org/3.14/library/time.html#time.sleep). (Contributed by Chris Clark in [bpo-13245](https://bugs.python.org/issue?@action=redirect&bpo=13245).)

- The *argument* parameter of [`enter()`](https://docs.python.org/3.14/library/sched.html#sched.scheduler.enter) and [`enterabs()`](https://docs.python.org/3.14/library/sched.html#sched.scheduler.enterabs) is now optional. (Contributed by Chris Clark in [bpo-13245](https://bugs.python.org/issue?@action=redirect&bpo=13245).)

- Both [`enter()`](https://docs.python.org/3.14/library/sched.html#sched.scheduler.enter) and [`enterabs()`](https://docs.python.org/3.14/library/sched.html#sched.scheduler.enterabs) now take a *kwargs* parameter. (Contributed by Chris Clark in [bpo-13245](https://bugs.python.org/issue?@action=redirect&bpo=13245).)

[Subject index](INDEX.md) · [Previous source section](re.md) · [Next source section](select.md) · [Release/subject declaration](summary-release-highlights.md)
