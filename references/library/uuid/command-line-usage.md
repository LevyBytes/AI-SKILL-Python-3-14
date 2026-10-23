# uuid - Command-Line Usage

### Command-Line Usage

Added in version 3.12.

You can run the `uuid` module as a script straight from the command line.

```sh
python -m uuid [-h] [-u {uuid1,uuid3,uuid4,uuid5,uuid6,uuid7,uuid8}] [-n NAMESPACE] [-N NAME]

```

The following options are accepted:

 -h, --help

Show the help message and exit.

 -u &lt;uuid&gt;

 --uuid &lt;uuid&gt;

Names the function to employ in generating the uuid. Absent a choice, `uuid4()` is what's used.

Changed in version 3.14: Permitted the generation of UUID versions 6, 7 and 8.

 -n &lt;namespace&gt;

 --namespace &lt;namespace&gt;

The namespace takes the form of a `UUID`, or else `@ns`, where `ns` picks out a well-known predefined UUID by namespace name — for example `@dns`, `@url`, `@oid`, and `@x500`. It's needed only for the `uuid3()` / `uuid5()` functions.

 -N &lt;name&gt;

 --name &lt;name&gt;

The name that figures into generating the uuid. Needed only for the `uuid3()` / `uuid5()` functions.

 -C &lt;num&gt;

 --count &lt;num&gt;

Generate *num* fresh UUIDs.

Added in version 3.14.

[Subject index](INDEX.md) · [Previous](uuid-reserved-microsoft-to-uuid-max.md) · [Continue](example.md) · [Owning module, declaration or section: uuid](uuid-safeuuid-class.md)
