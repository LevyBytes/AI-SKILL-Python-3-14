# What's New In Python 3.10 / Changes in the Python syntax

### Changes in the Python syntax

- Compiling formerly valid syntax now triggers a deprecation warning whenever a numeric literal sits flush against a keyword (for instance `0in x`). That becomes a syntax warning down the line, then ultimately a syntax error. Simply inserting a space between the numeric literal and the keyword that follows clears the warning and keeps your code working in later releases. (Contributed by Serhiy Storchaka in [bpo-43833](https://bugs.python.org/issue?@action=redirect&bpo=43833).)

[Subject index](INDEX.md) · [Previous source section](porting-to-python-3-10.md) · [Next source section](changes-in-the-python-api.md) · [Release/subject declaration](summary-release-highlights.md)
