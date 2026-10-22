# Python 3.5.0 alpha 3 / library / exceptions and tracebacks

[bpo-23646](https://bugs.python.org/issue?@action=redirect&bpo=23646): Should a signal interrupt time.sleep(), the sleep now retries against the recomputed delay, unless the signal handler raises an exception (PEP 475).

[bpo-23051](https://bugs.python.org/issue?@action=redirect&bpo=23051): The multiprocessing.Pool methods imap() and imap_unordered() now cope with exceptions thrown by an iterator. Alon Diamant and Davin Potts wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
