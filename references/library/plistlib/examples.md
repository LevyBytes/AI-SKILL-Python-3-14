# plistlib - Examples

### Examples

Generating a plist:

```python
import datetime as dt
import plistlib

pl = dict(
    aString = "Doodah",
    aList = ["A", "B", 12, 32.1, [1, 2, 3]],
    aFloat = 0.1,
    anInt = 728,
    aDict = dict(
        anotherString = "<hello & hi there!>",
        aThirdString = "M\xe4ssig, Ma\xdf",
        aTrueValue = True,
        aFalseValue = False,
    ),
    someData = b"<binary gunk>",
    someMoreData = b"<lots of binary gunk>" * 10,
    aDate = dt.datetime.now()
)
print(plistlib.dumps(pl).decode())

```

Parsing a plist:

```python
import plistlib

plist = b"""<plist version="1.0">
<dict>
    <key>foo</key>
    <string>bar</string>
</dict>
</plist>"""
pl = plistlib.loads(plist)
print(pl["foo"])

```

[Subject index](INDEX.md) · [Previous](plistlib-fmt-xml-to-plistlib-invalidfileexception.md) · [Owning module, declaration or section: plistlib](plistlib-load-to-plistlib-loads.md)
