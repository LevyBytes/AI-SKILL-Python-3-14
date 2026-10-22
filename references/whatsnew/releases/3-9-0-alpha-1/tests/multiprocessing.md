# Python 3.9.0 alpha 1 / tests / multiprocessing

[bpo-37421](https://bugs.python.org/issue?@action=redirect&bpo=37421): The multiprocessing tests now shut down the ForkServer instance while it's running: the "alive" file descriptor is closed to request that the server stop, after which its UNIX address is removed.

[bpo-37421](https://bugs.python.org/issue?@action=redirect&bpo=37421): test_concurrent_futures now tidies up multiprocessing so that temporary directories produced by multiprocessing.util.get_temp_dir() are removed at once.

[bpo-37421](https://bugs.python.org/issue?@action=redirect&bpo=37421): The multiprocessing tests now invoke `_run_finalizers()` directly to clear out temporary directories produced by tests right away.

[bpo-37123](https://bugs.python.org/issue?@action=redirect&bpo=37123): The multiprocessing test test_mymanager() now anticipates -SIGTERM in addition to plain exitcode 0. BaseManager._finalize_manager() dispatches SIGTERM to the manager process whenever it needs more than 1 second to halt, which is what happens on slow buildbots.

[bpo-38212](https://bugs.python.org/issue?@action=redirect&bpo=38212): For the multiprocessing tests, raise the test_queue_feeder_donot_stop_onexc() timeout from 1 up to 60 seconds.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
