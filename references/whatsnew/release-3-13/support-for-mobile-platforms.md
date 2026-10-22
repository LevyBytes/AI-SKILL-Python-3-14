# What's New In Python 3.13 / Support for mobile platforms

> (PEP and implementation contributed by Mark Shannon and Tian Gao in [gh-74929](https://github.com/python/cpython/issues/74929). Documentation updates provided by Guido van Rossum and Alyssa Coghlan.)

### Support for mobile platforms

[**PEP 730**](https://peps.python.org/pep-0730/): iOS is recognized as a [**PEP 11**](https://peps.python.org/pep-0011/) supported platform as of this release; its tier 3 targets are `arm64-apple-ios` together with `arm64-apple-ios-simulator` (these cover, in order, iPhone and iPad devices released after 2013 and the Xcode iOS simulator on Apple silicon hardware). The `x86_64-apple-ios-simulator` target (that same Xcode iOS simulator on the older `x86_64` hardware) falls short of tier 3 support, though best-effort coverage applies to it. The PEP and its implementation came from Russell Keith-Magee in [gh-114099](https://github.com/python/cpython/issues/114099).

[**PEP 738**](https://peps.python.org/pep-0738/): Android is recognized as a [**PEP 11**](https://peps.python.org/pep-0011/) supported platform as of this release; its tier 3 targets are `aarch64-linux-android` together with `x86_64-linux-android`. As for the 32-bit pair `arm-linux-androideabi` plus `i686-linux-android`, neither reaches tier 3 support, though best-effort coverage applies to them. The PEP and its implementation came from Malcolm Smith in [gh-116622](https://github.com/python/cpython/issues/116622).

See also

[**PEP 730**](https://peps.python.org/pep-0730/), [**PEP 738**](https://peps.python.org/pep-0738/)

[Subject index](INDEX.md) · [Previous source section](defined-mutation-semantics-for-locals.md) · [Next source section](other-language-changes.md) · [Release/subject declaration](summary-release-highlights.md)
