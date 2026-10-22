# How do I copy a file?

### How do I copy a file?

A [`copyfile()`](https://docs.python.org/3.14/library/shutil.html#shutil.copyfile) function lives in the [`shutil`](https://docs.python.org/3.14/library/shutil.html#module-shutil) module. Keep in mind that on Windows NTFS volumes it copies neither [alternate data streams](https://en.wikipedia.org/wiki/NTFS#Alternate_data_stream_(ADS)) nor [resource forks](https://en.wikipedia.org/wiki/Resource_fork) on macOS HFS+ volumes, even though both see little use nowadays. File permissions and metadata aren't copied either, though reaching for [`shutil.copy2()`](https://docs.python.org/3.14/library/shutil.html#shutil.copy2) instead retains most (but not all) of it.

[Subject index](INDEX.md)
