# Python 3.7.0 alpha 3 / idle / tk

[bpo-13802](https://bugs.python.org/issue?@action=redirect&bpo=13802): Put non-Latin characters into IDLE’s Font settings sample. Even when one picks a font covering only a limited slice of the unicode Basic Multilingual Plane, tcl/tk falls back to other fonts that supply a character. This broader example gives people who use non-Latin characters a clearer sense of what may appear in IDLE’s editors and shell. The frames on the Font tab were rearranged to fit the larger sample. A short note about the additions now lives in the Font/Tabs help.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
