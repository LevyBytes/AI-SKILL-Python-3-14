# Python 3.8.0 alpha 1 / tests / tests and documentation

[bpo-34373](https://bugs.python.org/issue?@action=redirect&bpo=34373): Repair the `test_mktime` and `test_pthread_getcpuclickid` tests on AIX. Add bounds checks for `_PyTime_localtime` under AIX. Contributed by Michael Felt.

[bpo-33873](https://bugs.python.org/issue?@action=redirect&bpo=33873): Correct a defect in `regrtest` where an additional test executed whenever –huntrleaks/-R was supplied. Now exits with an error if bad parameters reach –huntrleaks/-R (a minimum of one warmup pass plus one repetition is required).

[bpo-32663](https://bugs.python.org/issue?@action=redirect&bpo=32663): Ensure the `SMTPUTF8SimTests` test class actually executes inside `test_smtplib.py`.

[bpo-31809](https://bugs.python.org/issue?@action=redirect&bpo=31809): Add tests that confirm connectivity using secp ECDH curves.

[bpo-33717](https://bugs.python.org/issue?@action=redirect&bpo=33717): test.pythoninfo now records details for every clock, not just time.time() and time.perf_counter().

[bpo-26704](https://bugs.python.org/issue?@action=redirect&bpo=26704): Added a test showing the double-patching of an instance method. Patch by Anthony Sottile.

[bpo-34542](https://bugs.python.org/issue?@action=redirect&bpo=34542): Switch to 3072 RSA keys plus a SHA-256 signature for the test certs and keys.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
