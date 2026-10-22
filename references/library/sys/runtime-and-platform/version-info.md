# sys.version_info

sys.version_info

A tuple bundling the version number’s five pieces: *major*, *minor*, *micro*, *releaselevel*, and *serial*. Every one but *releaselevel* is an integer; the release level reads `'alpha'`, `'beta'`, `'candidate'`, or `'final'`. For Python version 2.0 the matching `version_info` value is `(2, 0, 0, 'final', 0)`. You can also reach the pieces by name, so `sys.version_info[0]` is the same as `sys.version_info.major`, and likewise for the rest.

Changed in version 3.1: Added named component attributes.

[API family](INDEX.md) · [sys context index](../INDEX.md).
