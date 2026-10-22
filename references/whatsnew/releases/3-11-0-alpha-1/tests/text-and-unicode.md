# Python 3.11.0 alpha 1 / tests / text and unicode

[bpo-44647](https://bugs.python.org/issue?@action=redirect&bpo=44647): A permanent Unicode-valued environment variable was added to the regression tests so this case stays covered going forward. Should your test environment break as a result, file a bug with us and, for the moment, set PYTHONREGRTEST_UNICODE_GUARD=0 in that environment.

[bpo-45195](https://bugs.python.org/issue?@action=redirect&bpo=45195): Repair test_readline.test_nonascii(): occasionally the newline character is absent at the end, so the output should not expect it. Victor Stinner authored the change.

[bpo-44949](https://bugs.python.org/issue?@action=redirect&bpo=44949): Repair the auto history tests of test_readline: occasionally the newline character is missing at the end, so the output should not expect it.

[bpo-43921](https://bugs.python.org/issue?@action=redirect&bpo=43921): Correct test_pha_required_nocert() inside test_ssl so it handles two further EOF situations (those where `recv()` hands back an empty string). Victor Stinner authored the patch.

[bpo-31904](https://bugs.python.org/issue?@action=redirect&bpo=31904): Disregard the casing of the error string within test_file_not_exists().

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
