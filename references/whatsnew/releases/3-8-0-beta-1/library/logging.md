# Python 3.8.0 beta 1 / library / logging

[bpo-36533](https://bugs.python.org/issue?@action=redirect&bpo=36533): Rebuilds logging.Handler locks within forked child processes, rather than grabbing them all in the parent prior to the fork only to free them again in the child. That acquire/release approach produced deadlocks in any code wiring up chained logging handlers that rely on one another, since the order in which locks get acquired cannot be assured.

[bpo-37035](https://bugs.python.org/issue?@action=redirect&bpo=37035): Suppresses logging of OSError-based exceptions once a fatal error strikes an asyncio transport. A peer can throw nearly any OSError, and user code cannot dodge these by being correct. The errors still reach user code; logging them merely pollutes asyncio logs for no gain.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
