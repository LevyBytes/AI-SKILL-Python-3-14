# Python 3.5.2 release candidate 1 / library / regexp cache inside strptime clears itself once timezone changes

[bpo-6478](https://bugs.python.org/issue?@action=redirect&bpo=6478): The regexp cache inside _strptime now clears itself once the timezone changes via time.tzset().

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
