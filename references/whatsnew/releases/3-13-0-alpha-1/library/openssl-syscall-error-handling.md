# Python 3.13.0 alpha 1 / library / under certain conditions openssl appears hand back ssl error syscall rather

[gh-107077](https://github.com/python/cpython/issues/107077): Under certain conditions OpenSSL appears to hand back `SSL_ERROR_SYSCALL` rather than `SSL_ERROR_SSL` after a certificate verification fails, yet the error parameters keep holding `ERR_LIB_SSL` together with `SSL_R_CERTIFICATE_VERIFY_FAILED`. That case is now spotted and the suitable `ssl.SSLCertVerificationError` gets raised. Pablo Galindo authored the fix.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
