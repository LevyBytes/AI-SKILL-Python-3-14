# Python 3.7.0 alpha 3 / library / traceback

[bpo-28603](https://bugs.python.org/issue?@action=redirect&bpo=28603): traceback: Resolved a TypeError raised while printing exception tracebacks whenever the active exception, or any exception along its context/cause chain, is unhashable. Zane Bitter wrote the patch.

[bpo-32121](https://bugs.python.org/issue?@action=redirect&bpo=32121): Adjusted `tracemalloc.Traceback` to act more like the traceback module by ordering the frames oldest-first. A negative *limit* is now accepted by `Traceback.format()`, which trims the output down to the `abs(limit)` oldest frames. The previous behaviour is reachable through the new *most_recent_first* argument on `Traceback.format()`. Jesse Bakker provided the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
