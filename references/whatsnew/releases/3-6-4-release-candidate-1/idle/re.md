# Python 3.6.4 release candidate 1 / idle / re

[bpo-13802](https://bugs.python.org/issue?@action=redirect&bpo=13802): Put non-Latin characters into the sample shown by IDLE’s Font settings. Even when a chosen font covers only a narrow portion of the unicode Basic Multilingual Plane, tcl/tk falls back to other fonts that supply a glyph. Broadening the example helps users of non-Latin characters picture what IDLE’s shell and editors will look like for them. The Font tab frames were re-arranged to fit the larger sample. A note about the additions appears in the Font/Tabs help.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
