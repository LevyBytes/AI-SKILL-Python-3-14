# Python 3.7.0 beta 1 / core and builtins / asyncio

[bpo-32591](https://bugs.python.org/issue?@action=redirect&bpo=32591): Added built-in support for following the origin of coroutine objects; refer to sys.set_coroutine_origin_tracking_depth and CoroutineType.cr_origin. This supersedes the asyncio debug mode's reliance on coroutine wrapping for native coroutine objects.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
