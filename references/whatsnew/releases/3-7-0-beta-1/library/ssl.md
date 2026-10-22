# Python 3.7.0 beta 1 / library / ssl

[bpo-31429](https://bugs.python.org/issue?@action=redirect&bpo=31429): The default cipher suite choice within the ssl module now follows a blacklist approach in place of a hard-coded whitelist. Python no longer turns back on ciphers that an OpenSSL security update has blocked. The default cipher suite choice can be set up at compile time.

[bpo-31399](https://bugs.python.org/issue?@action=redirect&bpo=31399): To check hostname and IP addresses, the ssl module now calls OpenSSL's X509_VERIFY_PARAM_set1_host() plus X509_VERIFY_PARAM_set1_ip() API. You can turn off subject common name fallback through SSLContext.hostname_checks_common_name.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
