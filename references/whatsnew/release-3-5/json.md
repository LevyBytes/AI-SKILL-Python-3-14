# What’s New In Python 3.5 / json — json

### json

Within JSON objects supplied as input, the [`json.tool`](https://docs.python.org/3.14/library/json.html#module-json.tool) command line interface now keeps the key ordering intact. Alphabetical key sorting can be requested through the new `--sort-keys` option. (Contributed by Berker Peksag in [bpo-21650](https://bugs.python.org/issue?@action=redirect&bpo=21650).)

For richer context about the failure, the JSON decoder now raises [`JSONDecodeError`](https://docs.python.org/3.14/library/json.html#json.JSONDecodeError) in place of [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError). (Contributed by Serhiy Storchaka in [bpo-19361](https://bugs.python.org/issue?@action=redirect&bpo=19361).)

[Subject index](INDEX.md) · [Previous source section](ipaddress.md) · [Next source section](linecache.md) · [Release/subject declaration](summary-release-highlights.md)
