# What's New In Python 3.6 / distutils

### distutils

The `default_format` attribute is gone from `distutils.command.sdist.sdist`, and the `formats` attribute now falls back to `['gztar']`. While we do not expect trouble, anything that counted on `default_format` being there might need adjusting. Refer to [bpo-27819](https://bugs.python.org/issue?@action=redirect&bpo=27819) for fuller details.

[Subject index](INDEX.md) · [Previous source section](decimal.md) · [Next source section](email.md) · [Release/subject declaration](summary-release-highlights.md)
