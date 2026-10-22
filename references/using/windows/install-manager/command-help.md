# 4.1.3. Command help

### 4.1.3. Command help

Running `py help` lists every supported command together with their options. You can hand any command the `-?` option to view its help, or pass its name to `py help`.

```none
$> py help
$> py help install
$> py install /?

```

There are some common options shared by all commands, which `py help` will display. You have to give these options after any subcommand. Supplying `-v` or `--verbose` raises the volume of output shown, and `-vv` raises it further for debugging. Supplying `-q` or `--quiet` cuts output, and `-qq` cuts it further.

With the `--config=<PATH>` option you can name a configuration file that overrides several settings together. Refer to Configuration below for more on those files.

[Subject index](INDEX.md) · [Previous source section](basic-use.md) · [Following source section](listing-runtimes.md)
