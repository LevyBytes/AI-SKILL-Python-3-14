# tarfile — Command-line options

### Command-line options

 -l &lt;tarfile&gt;

 --list &lt;tarfile&gt;

List files in a tarfile.

 -c &lt;tarfile&gt; &lt;source1&gt; ... &lt;sourceN&gt;

 --create &lt;tarfile&gt; &lt;source1&gt; ... &lt;sourceN&gt;

Create tarfile from source files.

 -e &lt;tarfile&gt; [<output_dir>]

 --extract &lt;tarfile&gt; [<output_dir>]

Extract tarfile into the current directory if *output_dir* is not specified.

 -t &lt;tarfile&gt;

 --test &lt;tarfile&gt;

Test whether the tarfile is valid or not.

 -v, --verbose

Verbose output.

 --filter &lt;filtername&gt;

Sets the *filter* used by `--extract`. Refer to Extraction filters for specifics. Nothing but string names is accepted here (namely `fully_trusted`, `tar`, and `data`).

[Subject index](INDEX.md) · [Previous](command-line-interface.md) · [Continue](reading-examples.md) · [Owning module, declaration or section: tarfile](tarfile-read-and-write-tar-archive-files.md)
