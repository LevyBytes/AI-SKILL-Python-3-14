# Python 3.9.0 alpha 1 / idle / files and paths

[bpo-27452](https://bugs.python.org/issue?@action=redirect&bpo=27452): Tidy up `config.py` by folding `RemoveFile` inline and easing the way `file` is handled inside `CreateConfigHandlers`.

[bpo-38183](https://bugs.python.org/issue?@action=redirect&bpo=38183): As a safeguard, test_idle steers clear of the user config directory. It will neither create nor touch .idlerc nor anything inside it. To surface settings-saving problems, users have to launch IDLE themselves.

[bpo-38041](https://bugs.python.org/issue?@action=redirect&bpo=38041): Restart lines in the shell now span the full window width, open with "=" every time, and steer clear of needless wrapping. Wrapping still happens when the embedded file name is long compared with the width.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
