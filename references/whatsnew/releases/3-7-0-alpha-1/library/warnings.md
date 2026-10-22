# Python 3.7.0 alpha 1 / library / warnings

[bpo-28727](https://bugs.python.org/issue?@action=redirect&bpo=28727): The _sre.SRE_Pattern objects (regular expression patterns produced via re.compile()) gained comparability, limited to the x==y and x!=y operators. That fix should also address [bpo-18383](https://bugs.python.org/issue?@action=redirect&bpo=18383): warning filters are no longer duplicated when the warnings module gets reloaded (something generally done only within unit tests).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
