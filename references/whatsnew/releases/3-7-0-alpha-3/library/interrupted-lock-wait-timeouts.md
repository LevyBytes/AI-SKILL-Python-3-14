# Python 3.7.0 alpha 3 / library / interrupted lock wait timeouts

[bpo-30768](https://bugs.python.org/issue?@action=redirect&bpo=30768): Repairs the pthread+semaphore implementation of PyThread_acquire_lock_timed() when it is invoked with timeout > 0 and intr_flag=0: the timeout is recomputed should sem_timedwait() be interrupted by a signal (EINTR). Refer also to [**PEP 475**](https://peps.python.org/pep-0475/).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
