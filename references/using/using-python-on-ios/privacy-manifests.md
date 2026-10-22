# 7.3.2. Privacy manifests

### 7.3.2. Privacy manifests

Come April 2025, Apple rolled out a mandate that [certain third-party libraries to provide a Privacy Manifest](https://developer.apple.com/support/third-party-SDK-requirements). Because of this, if you ship a binary module relying on one of the impacted libraries, you have to supply an `.xcprivacy` file covering that library. OpenSSL counts among the libraries this rule affects, though it isn't the only one.

When you produce a binary module called `mymodule.so` and rely on the Xcode build script covered in step 7 above, you can drop a `mymodule.xcprivacy` file alongside `mymodule.so`, and the privacy manifest gets installed into the spot it needs to occupy as the binary module becomes a framework.

[Subject index](INDEX.md) · [Previous source section](incompatible-code-in-the-standard-library.md)
