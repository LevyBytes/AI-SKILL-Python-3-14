# What’s New In Python 3.5 / distutils

### distutils

The `build` and `build_ext` commands alike henceforth take a `-j` option that turns on parallel building of extension modules. (Contributed by Antoine Pitrou in [bpo-5309](https://bugs.python.org/issue?@action=redirect&bpo=5309).)

The `distutils` module henceforth handles `xz` compression, which you switch on by handing `xztar` to `bdist --format` as an argument. (Contributed by Serhiy Storchaka in [bpo-16314](https://bugs.python.org/issue?@action=redirect&bpo=16314).)

[Subject index](INDEX.md) · [Previous source section](difflib.md) · [Next source section](doctest.md) · [Release/subject declaration](summary-release-highlights.md)
