# 5.5.4. App Store Compliance

### 5.5.4. App Store Compliance

Any app submitted for distribution by way of the macOS App Store has to clear Apple's app review process. Part of that process is a set of automated validation rules that scan the submitted application bundle for problematic code.

Some code in the Python standard library is known to break those automated rules. Even though these violations look like false positives, there is no contesting Apple's review rules. As a result, modifying the Python standard library is necessary for an app to clear App Store review.

Within the Python source tree there is [a patch file](https://github.com/python/cpython/tree/3.14/Mac/Resources/app-store-compliance.patch) that strips out all code known to trigger trouble with the App Store review process. That patch gets applied automatically whenever CPython is configured with the [`--with-app-store-compliance`](https://docs.python.org/3.14/using/configure.html#cmdoption-with-app-store-compliance) option.

Ordinarily this patch is not needed to use CPython on a Mac, nor is it needed when you distribute an app *outside* the macOS App Store. It is needed *only* when you use the macOS App Store as your distribution channel.

[Subject index](INDEX.md) · [Previous source section](distributing-python-applications.md) · [Following source section](other-resources.md)
