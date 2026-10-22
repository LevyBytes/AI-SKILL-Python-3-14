# What’s New In Python 3.12 / Optimizations — asyncio-task, dis, re, tokenize

### Optimizations

- The `wstr` and `wstr_length` members are gone from Unicode objects. That trims each object by 8 or 16 bytes on a 64bit platform. ([**PEP 623**](https://peps.python.org/pep-0623/)) (Contributed by Inada Naoki in [gh-92536](https://github.com/python/cpython/issues/92536).)

- Experimental use of the BOLT binary optimizer during the build is now supported; it raises performance by roughly 1-5%. Kevin Modzelewski landed this in [gh-90536](https://github.com/python/cpython/issues/90536), with Donghee Na contributing tuning in [gh-101525](https://github.com/python/cpython/issues/101525).

- For replacement strings that include group references, regular expression substitution (the [`re.sub()`](https://docs.python.org/3.14/library/re.html#re.sub) and [`re.subn()`](https://docs.python.org/3.14/library/re.html#re.subn) functions, plus the matching `re.Pattern` methods) now runs 2–3 times quicker. (Contributed by Serhiy Storchaka in [gh-91524](https://github.com/python/cpython/issues/91524).)

- By holding off on costly string formatting, [`asyncio.Task`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task) creation has been sped up. (Contributed by Itamar Oren in [gh-103793](https://github.com/python/cpython/issues/103793).)

- As a knock-on effect of the work needed to support [**PEP 701**](https://peps.python.org/pep-0701/) within the [`tokenize`](https://docs.python.org/3.14/library/tokenize.html#module-tokenize) module, the [`tokenize.tokenize()`](https://docs.python.org/3.14/library/tokenize.html#tokenize.tokenize) and [`tokenize.generate_tokens()`](https://docs.python.org/3.14/library/tokenize.html#tokenize.generate_tokens) functions now run as much as 64% faster. (Contributed by Marta Gómez Macías and Pablo Galindo in [gh-102856](https://github.com/python/cpython/issues/102856).)

- The new [`LOAD_SUPER_ATTR`](https://docs.python.org/3.14/library/dis.html#opcode-LOAD_SUPER_ATTR) instruction accelerates [`super()`](https://docs.python.org/3.14/library/functions.html#super) method calls together with attribute loads. (Contributed by Carl Meyer and Vladimir Matveev in [gh-103497](https://github.com/python/cpython/issues/103497).)

[Subject index](INDEX.md) · [Previous source section](uuid.md) · [Next source section](cpython-bytecode-changes.md) · [Release/subject declaration](summary-release-highlights.md)
