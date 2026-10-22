# What's New In Python 3.3 / socketserver — socketserver

[`BaseServer`](https://docs.python.org/3.14/library/socketserver.html#socketserver.BaseServer) gained an overridable hook, [`service_actions()`](https://docs.python.org/3.14/library/socketserver.html#socketserver.BaseServer.service_actions), that the [`serve_forever()`](https://docs.python.org/3.14/library/socketserver.html#socketserver.BaseServer.serve_forever) routine invokes inside its loop. [`ForkingMixIn`](https://docs.python.org/3.14/library/socketserver.html#socketserver.ForkingMixIn) leverages it to reap zombie children. Justin Warkentin landed this work ([bpo-11109](https://bugs.python.org/issue?@action=redirect&bpo=11109)).

[Subject index](INDEX.md) · [Next source section](sqlite3.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](socket.md) · [Preceding release/subject continuation](socket.md)
