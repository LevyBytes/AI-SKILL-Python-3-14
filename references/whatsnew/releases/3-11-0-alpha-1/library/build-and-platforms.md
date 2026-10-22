# Python 3.11.0 alpha 1 / library / build and platforms

[bpo-43666](https://bugs.python.org/issue?@action=redirect&bpo=43666): AIX: `Lib/_aix_support.get_platform()` can fail inside an AIX WPAR. The bos.rte fileset seems to carry a builddate within both LPAR and WPAR, so that fileset gets queried in place of bos.mp64. To head off a comparable case (no builddate in ODM) a value (9988) that suffices for finishing a build is supplied. M Felt wrote the patch.

[bpo-26228](https://bugs.python.org/issue?@action=redirect&bpo=26228): On FreeBSD, macOS, and Solaris, pty.spawn no longer hangs.

[bpo-42971](https://bugs.python.org/issue?@action=redirect&bpo=42971): On platforms (macOS, for example) that supply this constant, `errno.EQFULL` is now defined.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
