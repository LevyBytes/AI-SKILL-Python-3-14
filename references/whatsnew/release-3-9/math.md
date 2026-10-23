# What's New In Python 3.9 / math - math

### math

The [`math.gcd()`](https://docs.python.org/3.14/library/math.html#math.gcd) function was broadened to take any number of arguments; previously only a pair of arguments was accepted. (Contributed by Serhiy Storchaka in [bpo-39648](https://bugs.python.org/issue?@action=redirect&bpo=39648).)

A new [`math.lcm()`](https://docs.python.org/3.14/library/math.html#math.lcm) was added: it returns the least common multiple of the arguments supplied. (Contributed by Mark Dickinson, Ananthakrishnan and Serhiy Storchaka in [bpo-39479](https://bugs.python.org/issue?@action=redirect&bpo=39479) and [bpo-39648](https://bugs.python.org/issue?@action=redirect&bpo=39648).)

A new [`math.nextafter()`](https://docs.python.org/3.14/library/math.html#math.nextafter) was added: it returns the floating-point value immediately following *x* in the direction of *y*. (Contributed by Victor Stinner in [bpo-39288](https://bugs.python.org/issue?@action=redirect&bpo=39288).)

A new [`math.ulp()`](https://docs.python.org/3.14/library/math.html#math.ulp) was added; for a given float it yields the magnitude of that number's least significant bit. (Contributed by Victor Stinner in [bpo-39310](https://bugs.python.org/issue?@action=redirect&bpo=39310).)

[Subject index](INDEX.md) · [Previous source section](ipaddress.md) · [Next source section](multiprocessing.md) · [Release/subject declaration](summary-release-highlights.md)
