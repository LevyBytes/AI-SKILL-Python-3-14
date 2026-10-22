# sysconfig — User scheme

### User scheme

This scheme aims to be the handiest option for anyone who lacks write access to the global site-packages directory or simply prefers not to install there.

Files land in subdirectories of [`site.USER_BASE`](https://docs.python.org/3.14/library/site.html#site.USER_BASE) (denoted `*userbase*` from here on). Under this scheme, pure Python modules and extension modules both go to the same place (also referred to as [`site.USER_SITE`](https://docs.python.org/3.14/library/site.html#site.USER_SITE)).

[Subject index](INDEX.md) · [Previous](installation-paths.md) · [Continue](posix-user.md) · [Owning module, declaration or section: sysconfig](python-configuration-access-overview.md)
