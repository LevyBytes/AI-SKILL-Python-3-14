# Python 3.9.0 alpha 1 / tests / crypto

[bpo-38275](https://bugs.python.org/issue?@action=redirect&bpo=38275): test_ssl copes better now with TLS/SSL versions that are disabled. The OpenSSL crypto policy along with its run-time settings are detected, and tests covering disabled versions get skipped. The tests likewise tolerate additional TLS minimum_versions on platforms that replace OpenSSL's default with strict settings.

[bpo-38271](https://bugs.python.org/issue?@action=redirect&bpo=38271): The private keys used by test_ssl had been encrypted using 3DES in the traditional PKCS#5 format. Certain strict crypto policies block both 3DES and the PKCS#5 digest algorithm. The PKCS#8 format with AES256 encryption is used in their place.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
