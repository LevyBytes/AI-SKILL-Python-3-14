# What's New In Python 3.2 / poplib — poplib, ssl

### poplib

A *context* parameter is now accepted by the [`POP3_SSL`](https://docs.python.org/3.14/library/poplib.html#poplib.POP3_SSL) class; that parameter is an [`ssl.SSLContext`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext) object, which lets you gather SSL configuration options, certificates and private keys into one (potentially long-lived) structure.

(Contributed by Giampaolo Rodolà; [bpo-8807](https://bugs.python.org/issue?@action=redirect&bpo=8807).)

[Subject index](INDEX.md) · [Previous source section](random.md) · [Next source section](asyncore.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md)
