# Python 3.9.0 alpha 1 / library / platform

[bpo-18049](https://bugs.python.org/issue?@action=redirect&bpo=18049): A definition of THREAD_STACK_SIZE for AIX is now present in Python/thread_pthread.h. With the default recursion limit, the platform's default thread stacksize had been producing crashes. M Felt supplied the patch.

[bpo-28009](https://bugs.python.org/issue?@action=redirect&bpo=28009): Repair uuid.getnode() on systems using "." as the MAC Addr delimiter, and also handle a MAC Addr format that drops a leading 0 in MAC Addr values. So far AIX is the sole known platform exhibiting these settings. Michael Felt provided the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
