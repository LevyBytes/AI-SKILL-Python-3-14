# Python 3.6.0 beta 1 / library / urllib

[bpo-22450](https://bugs.python.org/issue?@action=redirect&bpo=22450): The default headers sent by urllib now carry an `Accept: */*` entry. REST API calls thus behave more consistently and predictably, particularly once proxy servers enter the picture.

- lib2to3.pgen3.driver.load_grammar() now produces a cache file that stays identical across runs for any given Grammar.txt input, no matter how hash randomization is configured.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
