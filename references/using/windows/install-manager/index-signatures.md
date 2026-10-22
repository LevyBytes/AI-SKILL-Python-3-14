# 4.1.13. Index signatures

### 4.1.13. Index signatures

Added in version 26.2.

Index files can be signed so tampering is detectable. The signature takes the form of a catalog file living at the same URL as the index with `.cat` appended to the filename. That catalog file should hold the hash of the index file it matches and should carry a valid Authenticode signature. As a result, standard tooling (on Windows) can produce a signature, and any certificate works provided the client operating system already trusts its certification authority (root CA).

Index signatures get downloaded and verified only when the local configuration’s `source_settings` section lists the index URL with `requires_signature` set true, or when the index JSON itself sets `requires_signature` to true. Once the setting is present in local configuration -- even with a false value -- whatever the index declares is disregarded.

Beyond demanding a valid signature, the `required_root_subject` and `required_publisher_subject` settings can tighten which signatures are accepted by examining the certificate Subject fields. Every attribute named in the configuration has to match the corresponding attribute in the certificate (extra attributes in the certificate are ignored). Typical attributes are `CN=`, which gives the common name; `O=`, which gives the organizational unit; and `C=`, which gives the country of the publisher.

Lastly, the `required_publisher_eku` setting lets you insist that a particular Enhanced Key Usage (EKU) be present on the publisher certificate. The EKU `1.3.6.1.5.5.7.3.3`, for instance, marks a certificate as meant for code signing (rather than server or client authentication). Paired with a particular root CA, this offers one more way to confirm a signature is legitimate.

Below is a sample `source_settings` section drawn from a configuration file. Here the feed’s publisher is pinned down by combining the Microsoft Identity Verification root with the EKU that root assigns. For this case the signature would reside at `https://www.python.org/ftp/python/index-windows.json.cat`.

```json5
{
  "source_settings": {
    "https://www.python.org/ftp/python/index-windows.json": {
      "requires_signature": true,
      "required_root_subject": "CN=Microsoft Identity Verification Root Certificate Authority 2020",
      "required_publisher_subject": "CN=Python Software Foundation",
      "required_publisher_eku": "1.3.6.1.4.1.311.97.608394634.79987812.305991749.578777327"
    }
  }
}

```

You could place the identical settings in the `index.json` file instead. Here the root and EKU are left out, so the signature simply has to be valid and bear a specific common name in the publisher’s certificate, with no further checks applied.

```json5
{
  "requires_signature": true,
  "required_publisher_subject": "CN=Python Software Foundation",
  "versions": [
    // ...
  ]
}

```

Whenever settings originating inside a feed are applied, the user gets a notification and the settings show up in the log file or verbose output. For feeds you expect to rely on often, copying these settings into a local configuration file is advisable, so that unauthorised feed changes cannot switch off verification.

You cannot redirect where the signature file lives, neither within the feed nor via a configuration file. Administrators may supply their own `source_settings` inside a mandatory configuration file (refer to Administrative configuration).

Should signature validation fail, you are notified and asked whether to proceed. Where interactive confirmation is disallowed (say, because `--yes` was passed), it aborts every time. To work with a feed that has invalid configuration under those conditions, you have to provide a configuration file that turns off signature checking for that feed.

```json5
"source_settings": {
  "https://www.example.com/feed-with-invalid-signature.json": {
    "requires_signature": false
  }
}

```

[Subject index](INDEX.md) · [Previous source section](installing-free-threaded-binaries.md) · [Following source section](troubleshooting.md)
