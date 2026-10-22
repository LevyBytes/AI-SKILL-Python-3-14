# 5.8.1. __main__.__spec__

### 5.8.1. __main__.__spec__

According to how [`__main__`](https://docs.python.org/3.14/library/__main__.html#module-__main__) is initialized, `__main__.__spec__` is either set fittingly or set to `None`.

Whenever Python is launched with the [`-m`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-m) option, `__spec__` is assigned the module spec of the matching module or package. `__spec__` likewise gets populated when the `__main__` module is loaded as part of running a directory, zipfile or another [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) entry.

Across [the remaining cases](https://docs.python.org/3.14/using/cmdline.html#using-on-interface-options) `__main__.__spec__` is set to `None`, given that the code used to fill in [`__main__`](https://docs.python.org/3.14/library/__main__.html#module-__main__) has no direct counterpart in an importable module:

- interactive prompt

- [`-c`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-c) option

- running from stdin

- running directly from a source or bytecode file

Bear in mind that in this final scenario `__main__.__spec__` always holds `None`, *even if* it would be perfectly feasible to import the file straight away as a module instead. Reach for the [`-m`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-m) switch whenever you want proper module metadata present in [`__main__`](https://docs.python.org/3.14/library/__main__.html#module-__main__).

Observe as well that should `__main__` line up with a module you can import and `__main__.__spec__` be assigned to match, the two count as *distinct* modules regardless. The reason is that code sitting behind `if __name__ == "__main__":` guards runs solely when the module serves to fill out the `__main__` namespace, never under an ordinary import.

[Subject index](INDEX.md) · [Owning language section](the-import-system.md) · [Owning language section](special-considerations-for-main.md) · [Previous source section](special-considerations-for-main.md) · [Following source section](references.md)
