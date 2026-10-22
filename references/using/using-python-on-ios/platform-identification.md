# 7.1.2. Platform identification

### 7.1.2. Platform identification

While running on iOS, `sys.platform` shows up as `ios`. You get this same value on either an iPhone or iPad, no matter whether the app sits on the simulator or on real hardware.

To learn about the precise runtime environment — the iOS version, which device model, and whether you're on a simulator — call [`platform.ios_ver()`](https://docs.python.org/3.14/library/platform.html#platform.ios_ver). Depending on the hardware, [`platform.system()`](https://docs.python.org/3.14/library/platform.html#platform.system) returns either `iOS` or `iPadOS`.

For kernel-level information, [`os.uname()`](https://docs.python.org/3.14/library/os.html#os.uname) returns a name of `Darwin`.

[Subject index](INDEX.md) · [Previous source section](ios-version-compatibility.md) · [Following source section](standard-library-availability.md)
