# Running without a subprocess

### Running without a subprocess

As shipped, IDLE runs user code in its own subprocess over a socket that goes through the internal loopback interface. Nothing about this connection is visible outside the machine, and no data crosses to or from the internet. Even if firewall software objects, you're safe to disregard it.

When the socket connection can't be established, Idle lets you know. These failures are sometimes fleeting, but when they stick around the culprit is likely a firewall blocking the link or a particular system's misconfiguration. While the issue remains, you can launch Idle using the -n command line switch.

Starting IDLE with the -n command line switch keeps it in one process and skips creating the subprocess that runs the RPC Python execution server. That can help when Python is unable to spin up the subprocess or the RPC socket interface on your platform. The catch is that, in this mode, user code isn't walled off from IDLE itself. The environment also doesn't restart when you pick Run/Run Module (F5). After editing your code, you have to reload() the touched modules and re-import any specific names (for example, from foo import baz) for the edits to register. Given all this, sticking with the default subprocess is preferable whenever you can.

Deprecated since version 3.4.

[Subject index](INDEX.md) · [Previous](developing-tkinter-applications.md) · [Continue](help-sources.md)
