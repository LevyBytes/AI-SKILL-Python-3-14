# urllib.request — FileHandler Objects

### FileHandler Objects

 FileHandler.file_open(*req*)

Open the file on the local machine, provided no host name is present or the host name reads `'localhost'`.

Changed in version 3.2: Only local hostnames work with this method. Supplying a remote hostname causes a [`URLError`](https://docs.python.org/3.14/library/urllib.error.html#urllib.error.URLError) to be raised.

[Subject index](INDEX.md) · [Previous](httpshandler-https-open.md) · [Continue](datahandler-data-open.md) · [Owning module, declaration or section: urllib.request](urllib-request-urlopen-to-urllib-request-build-opener.md)
