# Python 3.11.0 alpha 2 / library / memory and lifetimes

[bpo-45262](https://bugs.python.org/issue?@action=redirect&bpo=45262): Stop a use-after-free in asyncio. Ensure the cached running loop holder is reset during dealloc so a use-after-free in get_running_loop is avoided

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
