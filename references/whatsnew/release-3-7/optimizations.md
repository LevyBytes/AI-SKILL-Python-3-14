# What's New In Python 3.7 / Optimizations — asyncio, asyncio-eventloop, asyncio-future, asyncio-task

### Optimizations

Porting additional code over to the `METH_FASTCALL` convention has markedly cut the cost of calling many methods belonging to assorted standard library classes written in C. (Contributed by Victor Stinner in [bpo-29300](https://bugs.python.org/issue?@action=redirect&bpo=29300), [bpo-29507](https://bugs.python.org/issue?@action=redirect&bpo=29507), [bpo-29452](https://bugs.python.org/issue?@action=redirect&bpo=29452), and [bpo-29286](https://bugs.python.org/issue?@action=redirect&bpo=29286).)

Through assorted optimizations, Python startup time dropped by 10% on Linux and as much as 30% on macOS. (Contributed by Victor Stinner, INADA Naoki in [bpo-29585](https://bugs.python.org/issue?@action=redirect&bpo=29585), and Ivan Levkivskyi in [bpo-31333](https://bugs.python.org/issue?@action=redirect&bpo=31333).)

Thanks to bytecode changes that sidestep building bound method instances, method calls now run as much as 20% quicker. (Contributed by Yury Selivanov and INADA Naoki in [bpo-26110](https://bugs.python.org/issue?@action=redirect&bpo=26110).)

For several of its frequently invoked functions, the [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) module gained a set of noteworthy optimizations:

- Reimplemented in C, the [`asyncio.get_event_loop()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.get_event_loop) function is now as much as 15 times quicker. (Contributed by Yury Selivanov in [bpo-32296](https://bugs.python.org/issue?@action=redirect&bpo=32296).)

- Callback handling for [`asyncio.Future`](https://docs.python.org/3.14/library/asyncio-future.html#asyncio.Future) has been optimized. (Contributed by Yury Selivanov in [bpo-32348](https://bugs.python.org/issue?@action=redirect&bpo=32348).)

- [`asyncio.gather()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.gather) now runs as much as 15% quicker. (Contributed by Yury Selivanov in [bpo-32355](https://bugs.python.org/issue?@action=redirect&bpo=32355).)

- When the *delay* argument is zero or negative, [`asyncio.sleep()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.sleep) now runs as much as 2 times quicker. (Contributed by Andrew Svetlov in [bpo-32351](https://bugs.python.org/issue?@action=redirect&bpo=32351).)

-

Running asyncio in debug mode now carries less performance cost. (Contributed by Antoine Pitrou in [bpo-31970](https://bugs.python.org/issue?@action=redirect&bpo=31970).)

Thanks to the PEP 560 effort, loading [`typing`](https://docs.python.org/3.14/library/typing.html#module-typing) at import time happens 7 times more quickly, and a number of typing operations now run faster too. (Contributed by Ivan Levkivskyi in [bpo-32226](https://bugs.python.org/issue?@action=redirect&bpo=32226).)

For frequent scenarios, [`sorted()`](https://docs.python.org/3.14/library/functions.html#sorted) along with [`list.sort()`](https://docs.python.org/3.14/library/stdtypes.html#list.sort) gained speedups reaching as much as 40-75%. (Contributed by Elliot Gorokhovsky in [bpo-28685](https://bugs.python.org/issue?@action=redirect&bpo=28685).)

The [`dict.copy()`](https://docs.python.org/3.14/library/stdtypes.html#dict.copy) operation can now run as much as 5.5 times quicker. (Contributed by Yury Selivanov in [bpo-31179](https://bugs.python.org/issue?@action=redirect&bpo=31179).)

When *name* cannot be located and *obj* leaves [`object.__getattr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getattr__) or [`object.__getattribute__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getattribute__) unmodified, [`hasattr()`](https://docs.python.org/3.14/library/functions.html#hasattr) together with [`getattr()`](https://docs.python.org/3.14/library/functions.html#getattr) now run roughly 4 times quicker. (Contributed by INADA Naoki in [bpo-32544](https://bugs.python.org/issue?@action=redirect&bpo=32544).)

Locating particular Unicode characters within a string (for instance the Ukrainian capital "??") used to run as much as 25 times slower compared with hunting for other characters. The slowdown in the worst case is now merely 3 times. (Contributed by Serhiy Storchaka in [bpo-24821](https://bugs.python.org/issue?@action=redirect&bpo=24821).)

A rewrite of the [`collections.namedtuple()`](https://docs.python.org/3.14/library/collections.html#collections.namedtuple) factory makes building named tuples between 4 and 6 times quicker. (Contributed by Jelle Zijlstra, refined later on by INADA Naoki, plus Serhiy Storchaka and Raymond Hettinger, in [bpo-28638](https://bugs.python.org/issue?@action=redirect&bpo=28638).)

In the typical scenario, [`datetime.date.fromordinal()`](https://docs.python.org/3.14/library/datetime.html#datetime.date.fromordinal) plus [`datetime.date.fromtimestamp()`](https://docs.python.org/3.14/library/datetime.html#datetime.date.fromtimestamp) gained as much as 30% in speed. (Contributed by Paul Ganssle in [bpo-32403](https://bugs.python.org/issue?@action=redirect&bpo=32403).)

By relying on [`os.scandir()`](https://docs.python.org/3.14/library/os.html#os.scandir), the [`os.fwalk()`](https://docs.python.org/3.14/library/os.html#os.fwalk) routine can now run up to twice as fast. (Contributed by Serhiy Storchaka in [bpo-25996](https://bugs.python.org/issue?@action=redirect&bpo=25996).)

Adopting the [`os.scandir()`](https://docs.python.org/3.14/library/os.html#os.scandir) function lifted the [`shutil.rmtree()`](https://docs.python.org/3.14/library/shutil.html#shutil.rmtree) routine's speed by roughly 20–40%. (Contributed by Serhiy Storchaka in [bpo-28564](https://bugs.python.org/issue?@action=redirect&bpo=28564).)

Both matching and lookup that ignore case for [`regular expressions`](https://docs.python.org/3.14/library/re.html#module-re) were tuned. Some patterns can now be located as much as 20 times quicker. (Contributed by Serhiy Storchaka in [bpo-30285](https://bugs.python.org/issue?@action=redirect&bpo=30285).)

When the `flags` argument is a `RegexFlag`, [`re.compile()`](https://docs.python.org/3.14/library/re.html#re.compile) now turns it into an int object. Its speed matches Python 3.5 and, depending on the pattern, beats Python 3.6 by close to 10%. (Contributed by INADA Naoki in [bpo-31671](https://bugs.python.org/issue?@action=redirect&bpo=31671).)

Under heavy loads, the [`modify()`](https://docs.python.org/3.14/library/selectors.html#selectors.BaseSelector.modify) methods belonging to [`selectors.EpollSelector`](https://docs.python.org/3.14/library/selectors.html#selectors.EpollSelector), [`selectors.PollSelector`](https://docs.python.org/3.14/library/selectors.html#selectors.PollSelector) and [`selectors.DevpollSelector`](https://docs.python.org/3.14/library/selectors.html#selectors.DevpollSelector) might gain around 10% in speed. (Contributed by Giampaolo Rodola' in [bpo-30014](https://bugs.python.org/issue?@action=redirect&bpo=30014))

The job of constant folding shifted away from the peephole optimizer and into the fresh AST optimizer, which can apply optimizations with greater consistency. (Contributed by Eugene Toder and INADA Naoki in [bpo-29469](https://bugs.python.org/issue?@action=redirect&bpo=29469) and [bpo-11549](https://bugs.python.org/issue?@action=redirect&bpo=11549).)

The bulk of the functions and methods within [`abc`](https://docs.python.org/3.14/library/abc.html#module-abc) were reimplemented in C. That speeds up building abstract base classes and running [`isinstance()`](https://docs.python.org/3.14/library/functions.html#isinstance) plus [`issubclass()`](https://docs.python.org/3.14/library/functions.html#issubclass) against them by a factor of 1.5x. It additionally trims Python's start-up time by as much as 10%. (Contributed by Ivan Levkivskyi and INADA Naoki in [bpo-31333](https://bugs.python.org/issue?@action=redirect&bpo=31333))

Major speed gains landed for the alternate constructors of [`datetime.date`](https://docs.python.org/3.14/library/datetime.html#datetime.date) and [`datetime.datetime`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime), achieved by taking fast-path constructors whenever no subclass is being built. (Contributed by Paul Ganssle in [bpo-32403](https://bugs.python.org/issue?@action=redirect&bpo=32403))

Comparing [`array.array`](https://docs.python.org/3.14/library/array.html#array.array) instances became markedly quicker in some situations. Where the arrays carry values of one identical integer type, it now runs between 10x and 70x quicker. (Contributed by Adrian Wielgosik in [bpo-24700](https://bugs.python.org/issue?@action=redirect&bpo=24700).)

On the majority of platforms, [`math.erf()`](https://docs.python.org/3.14/library/math.html#math.erf) together with [`math.erfc()`](https://docs.python.org/3.14/library/math.html#math.erfc) now defer to the quicker C library version. (Contributed by Serhiy Storchaka in [bpo-26121](https://bugs.python.org/issue?@action=redirect&bpo=26121).)

[Subject index](INDEX.md) · [Previous source section](build-changes.md) · [Release/subject declaration](summary-release-highlights.md) · [Next source section](other-cpython-implementation-changes.md)
