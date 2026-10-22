# What's New In Python 3.9 / compileall

### compileall

A fresh capability to share hardlinks across duplicate `.pyc` files landed: the *hardlink_dupes* parameter plus the ?hardlink-dupes command line option. (Contributed by Lumír ?Frenzy? Balhar in [bpo-40495](https://bugs.python.org/issue?@action=redirect&bpo=40495).)

Fresh options for reshaping paths inside the produced `.pyc` files appeared: the *stripdir*, *prependdir*, *limit_sl_dest* parameters together with the -s, -p, -e command line options. It also became possible to pass the optimization-level option more than once. (Contributed by Lumír ?Frenzy? Balhar in [bpo-38112](https://bugs.python.org/issue?@action=redirect&bpo=38112).)

[Subject index](INDEX.md) · [Previous source section](asyncio.md) · [Next source section](concurrent-futures.md) · [Release/subject declaration](summary-release-highlights.md)
