# 4.1.12. Installing free-threaded binaries

### 4.1.12. Installing free-threaded binaries

Added in version 3.13.

You obtain pre-built free-threaded distributions by installing tags carrying the `t` suffix.

```none
$> py install 3.14t
$> py install 3.14t-arm64
$> py install 3.14t-32

```

Installation and registration proceed as usual. When no other runtimes are present, `python` will start this one. Otherwise you must invoke `py -V:3.14t ...`, or use the `python3.14t.exe` commands if you have placed the global aliases directory on your `PATH` environment variable.

[Subject index](INDEX.md) · [Previous source section](administrative-configuration.md) · [Following source section](index-signatures.md)
