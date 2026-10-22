# Python 3.5.0 alpha 1 / library / asyncio

[bpo-21209](https://bugs.python.org/issue?@action=redirect&bpo=21209): Corrected asyncio.tasks.CoroWrapper to sidestep a bug within the yield-from implementation on CPythons earlier than 3.4.1.

- asyncio: gi_{frame,running,code} properties were added to CoroWrapper (upstream [bpo-163](https://bugs.python.org/issue?@action=redirect&bpo=163)).

[bpo-22641](https://bugs.python.org/issue?@action=redirect&bpo=22641): For tougher security, asyncio now builds the default SSL context for client connections via ssl.create_default_context().

[bpo-22841](https://bugs.python.org/issue?@action=redirect&bpo=22841): asyncio add_signal_handler() now rejects coroutines. Ludovic.Gasc supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
