# ssl: `ssl.VERIFY_DEFAULT`, `ssl.VERIFY_CRL_CHECK_LEAF`, `ssl.VERIFY_CRL_CHECK_CHAIN`, `ssl.VERIFY_X509_STRICT`, `ssl.VERIFY_ALLOW_PROXY_CERTS`, `ssl.VERIFY_X509_TRUSTED_FIRST`, `ssl.VERIFY_X509_PARTIAL_CHAIN`

ssl.VERIFY_DEFAULT

A possible setting for `SSLContext.verify_flags`. Under this mode, no checking of certificate revocation lists (CRLs) takes place. OpenSSL by default neither demands nor verifies CRLs.

Added in version 3.4.

 ssl.VERIFY_CRL_CHECK_LEAF

A possible setting for `SSLContext.verify_flags`. Under this mode, only the peer cert undergoes the check, leaving the intermediate CA certificates untouched. It calls for a valid CRL signed by the issuer of the peer cert (that is, its direct ancestor CA). When no suitable CRL has been loaded by way of `SSLContext.load_verify_locations`, validation fails.

Added in version 3.4.

 ssl.VERIFY_CRL_CHECK_CHAIN

A possible setting for `SSLContext.verify_flags`. Under this mode, every certificate across the peer cert chain has its CRLs checked.

Added in version 3.4.

 ssl.VERIFY_X509_STRICT

A possible setting for `SSLContext.verify_flags` that turns off the workarounds for broken X.509 certificates.

Added in version 3.4.

 ssl.VERIFY_ALLOW_PROXY_CERTS

A possible setting for `SSLContext.verify_flags` that enables proxy certificate verification.

Added in version 3.10.

 ssl.VERIFY_X509_TRUSTED_FIRST

A possible setting for `SSLContext.verify_flags`. It tells OpenSSL to favor trusted certificates as it assembles the trust chain for validating a certificate. The flag is on by default.

Added in version 3.4.4.

 ssl.VERIFY_X509_PARTIAL_CHAIN

A possible setting for `SSLContext.verify_flags`. It tells OpenSSL to let intermediate CAs sitting in the trust store serve as trust-anchors, exactly as the self-signed root CA certificates do. That lets you trust certificates an intermediate CA issued without needing to trust the root CA above it.

Added in version 3.10.

[Subject index](INDEX.md) · [Previous](ssl-verifymode-class.md) · [Continue](ssl-verifyflags-class.md) · [Owning module, declaration or section: ssl](ssl-tls-ssl-wrapper-for-socket-objects.md) · [Owning module, declaration or section: Constants](ssl-cert-none-to-ssl-cert-required.md)
