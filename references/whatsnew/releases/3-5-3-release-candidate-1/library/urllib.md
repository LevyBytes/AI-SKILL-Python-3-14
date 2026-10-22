# Python 3.5.3 release candidate 1 / library / urllib

[bpo-22450](https://bugs.python.org/issue?@action=redirect&bpo=22450): urllib now sends an `Accept: */*` header as part of its default header set. REST API call results become steadier and easier to anticipate, particularly once proxy servers enter the picture.

- lib2to3.pgen3.driver.load_grammar() now produces a cache file that stays identical across runs for one Grammar.txt input, no matter how hash randomization is configured.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
