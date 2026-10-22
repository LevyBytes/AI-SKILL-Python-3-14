# Python 3.7.0 beta 1 / library / functions and types

[bpo-32662](https://bugs.python.org/issue?@action=redirect&bpo=32662): Implement the Server.start_serving(), Server.serve_forever(), and Server.is_serving() methods. Add a "start_serving" keyword parameter onto loop.create_server() and loop.create_unix_server().

[bpo-32643](https://bugs.python.org/issue?@action=redirect&bpo=32643): Turn Task._step, Task._wakeup and Future._schedule_callbacks methods private.

[bpo-32622](https://bugs.python.org/issue?@action=redirect&bpo=32622): Add the `asyncio.AbstractEventLoop.sendfile()` method.

[bpo-31801](https://bugs.python.org/issue?@action=redirect&bpo=31801): Add `_ignore_` onto `Enum` so that temporary variables may be used throughout class construction without getting turned into members.

[bpo-31853](https://bugs.python.org/issue?@action=redirect&bpo=31853): Within SSLSocket, prefer super().method over socket.method. Their presence was probably down to legacy reasons.

[bpo-32102](https://bugs.python.org/issue?@action=redirect&bpo=32102): A fresh `capture_output` argument was added to subprocess.run

[bpo-32373](https://bugs.python.org/issue?@action=redirect&bpo=32373): Introduce the socket.getblocking() method.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
