# Python 3.7.0 alpha 1 / library / multiprocessing

[bpo-22807](https://bugs.python.org/issue?@action=redirect&bpo=22807): uuid.SafeUUID and uuid.UUID.is_safe were added to convey, from the platform, whether the UUIDs produced were made by a multiprocessing safe method.

[bpo-28779](https://bugs.python.org/issue?@action=redirect&bpo=28779): Calling multiprocessing.set_forkserver_preload() used to bring down the forkserver process whenever a preloaded module created certain multiprocessing objects, locks among them.

[bpo-30919](https://bugs.python.org/issue?@action=redirect&bpo=30919): Repair a shared memory performance regression that hit multiprocessing in 3.x. In 2.x the shared memory relied on anonymous memory mappings, whereas 3.x mmaps real files. Take care to perform as little disk I/O as you can.

[bpo-5001](https://bugs.python.org/issue?@action=redirect&bpo=5001): A number of asserts inside `multiprocessing` are now more informative, and a few error types were switched to more specific ones.

[bpo-5001](https://bugs.python.org/issue?@action=redirect&bpo=5001): The `multiprocessing` module carries several uninformative asserts, as issue 5001 records. This change repairs two of the riskiest ones, because they live in error-reporting code inside the `multiprocessing.managers.convert_to_error` function. (It also enriches a ValueError message.) The one change that might be troublesome is that the AssertionError became a TypeError; that should nonetheless help tell it apart from an AssertionError that the function or its caller is *reporting* (as happens in issue 31169). - Allen W. Smith (drallensmith on github) wrote the patch.

[bpo-24484](https://bugs.python.org/issue?@action=redirect&bpo=24484): A race during multiprocessing cleanup is now avoided.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
