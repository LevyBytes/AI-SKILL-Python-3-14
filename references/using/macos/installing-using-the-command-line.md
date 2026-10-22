# 5.5.2. Installing using the command line

### 5.5.2. Installing using the command line

Should you wish to automate installation of the `python.org` installer package (instead of going through the familiar macOS **Installer** GUI app), the macOS command line **installer** utility also lets you pick non-default options. If **installer** is unfamiliar to you, it can come across as a bit cryptic (run **man installer** for more information). For instance, the shell snippet below illustrates one approach, using the `3.14.0b2` release and choosing the free-threaded interpreter option:

```
RELEASE="python-3.140b2-macos11.pkg"

# download installer pkg
curl -O https://www.python.org/ftp/python/3.14.0/${RELEASE}

# create installer choicechanges to customize the install:
#    enable the PythonTFramework-3.14 package
#    while accepting the other defaults (install all other packages)
cat > ./choicechanges.plist <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<array>
        <dict>
                <key>attributeSetting</key>
                <integer>1</integer>
                <key>choiceAttribute</key>
                <string>selected</string>
                <key>choiceIdentifier</key>
                <string>org.python.Python.PythonTFramework-3.14</string>
        </dict>
</array>
</plist>
EOF

sudo installer -pkg ./${RELEASE} -applyChoiceChangesXML ./choicechanges.plist -target /
```

You can then confirm that both installer builds are now present with something along these lines:

```
$ # test that the free-threaded interpreter was installed if the Unix Command Tools package was enabled
$ /usr/local/bin/python3.14t -VV
Python 3.14.0b2 free-threading build (v3.14.0b2:3a83b172af, Jun  5 2024, 12:57:31) [Clang 15.0.0 (clang-1500.3.9.4)]
$ #    and the traditional interpreter
$ /usr/local/bin/python3.14 -VV
Python 3.14.0b2 (v3.14.0b2:3a83b172af, Jun  5 2024, 12:50:24) [Clang 15.0.0 (clang-1500.3.9.4)]
$ # test that they are also available without the prefix if /usr/local/bin is on $PATH
$ python3.14t -VV
Python 3.14.0b2 free-threading build (v3.14.0b2:3a83b172af, Jun  5 2024, 12:57:31) [Clang 15.0.0 (clang-1500.3.9.4)]
$ python3.14 -VV
Python 3.14.0b2 (v3.14.0b2:3a83b172af, Jun  5 2024, 12:50:24) [Clang 15.0.0 (clang-1500.3.9.4)]
```

Note

At present, `python.org` installers install solely to fixed locations such as `/Library/Frameworks/`, `/Applications`, and `/usr/local/bin`. The **installer** `-domain` option cannot be used to install elsewhere.

[Subject index](INDEX.md) · [Previous source section](installing-free-threaded-binaries.md) · [Following source section](distributing-python-applications.md)
