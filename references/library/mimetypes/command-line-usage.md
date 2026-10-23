# mimetypes - Command-line usage

### Command-line usage

You can run the `mimetypes` module directly as a command-line script.

```sh
python -m mimetypes [-h] [-e] [-l] type [type ...]

```

The following options are accepted:

 -h

 --help

Display the help text, then quit.

 -e

 --extension

Guess extension instead of type.

 -l

 --lenient

On top of that, look through some widespread non-standard types as well.

Left to its own devices, the script turns MIME types into file extensions. Supply `--extension`, though, and it goes the other way, turning file extensions into MIME types.

The script emits one line to the standard output stream for every `type` entry. Encountering an unknown type, it sends an error message to that same standard output stream and quits with return code `1`.

[Subject index](INDEX.md) · [Previous](mime-extension-lookup-and-type-registration.md) · [Continue](command-line-example.md) · [Owning module, declaration or section: mimetypes](mimetypes-guess-type-to-mimetypes-encodings-map.md)
