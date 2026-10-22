# 7.3.1. Incompatible code in the standard library

### 7.3.1. Incompatible code in the standard library

A portion of the code inside the Python standard library is recognized as breaking these automated rules. Even though those breaches look like false positives, there's no contesting Apple's review rules; thus the Python standard library has to be altered for an app to clear App Store review.

Bundled in the Python source tree is [a patch file](https://github.com/python/cpython/tree/3.14/Mac/Resources/app-store-compliance.patch) that strips out every bit of code known to trip up the App Store review process. When building for iOS, this patch gets applied on its own automatically.

[Subject index](INDEX.md) · [Previous source section](app-store-compliance.md) · [Following source section](privacy-manifests.md)
