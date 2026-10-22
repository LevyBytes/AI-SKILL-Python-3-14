# Python 3.6.0 beta 4 / library / warnings

[bpo-28727](https://bugs.python.org/issue?@action=redirect&bpo=28727): Regular expression patterns, the _sre.SRE_Pattern objects that re.compile() builds, are now comparable (only the x==y and x!=y operators). This change ought to address [bpo-18383](https://bugs.python.org/issue?@action=redirect&bpo=18383): avoid duplicating warning filters whenever the warnings module is reloaded (something normally done only within unit tests).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
