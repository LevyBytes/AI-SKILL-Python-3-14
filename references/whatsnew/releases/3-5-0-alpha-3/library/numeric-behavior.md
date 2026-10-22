# Python 3.5.0 alpha 3 / library / numeric behavior

[bpo-23605](https://bugs.python.org/issue?@action=redirect&bpo=23605): os.walk() now invokes os.scandir() in place of os.listdir(). Drawing on os.scandir() trims the number of os.stat() calls. Ben Hoyt wrote the initial patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
