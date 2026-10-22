# Python 3.8.0 alpha 1 / library / take out streamreaderprotocol untrack reader

[bpo-35065](https://bugs.python.org/issue?@action=redirect&bpo=35065): Take out `StreamReaderProtocol._untrack_reader`. As things stand the `_untrack_reader` call fires too early, which makes the protocol drop the reader before `connection_lost` has a chance to run and deliver the EOF to that reader.

[Subject index](INDEX.md) · [Release version, date and status](../../release-overview/overview.md)
