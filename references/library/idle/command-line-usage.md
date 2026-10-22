# Command-line usage

### Command-line usage

From the command line, IDLE accepts a range of options when launched. Its general syntax reads:

```bash
python -m idlelib [options] [file ...]

```

The following options are available:

 -c &lt;command&gt;

Run the supplied Python command inside the shell window. As an example, pass `-c "print('Hello, World!')"`. Under Windows, the outer quotes have to be double quotes as illustrated.

 -d

Enable the debugger and open the shell window.

 -e

Open an editor window.

 -h

Print a help message with legal combinations of options and exit.

 -i

Open a shell window.

 -r &lt;file&gt;

Execute the given file within the shell window.

 -s

Before the shell window opens, execute the startup file (the one set through the environment variables `IDLESTARTUP` or [`PYTHONSTARTUP`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONSTARTUP)).

 -t &lt;title&gt;

Set the title of the shell window.

 - Within the shell window, read standard input and run it. Place this option last, ahead of any arguments.

If arguments are provided:

-

Should you pass `-`, `-c`, or `-r`, every argument lands in `sys.argv[1:]`, while `sys.argv[0]` takes the value `''`, `'-c'`, or `'-r'` to match. No editor window comes up in that case, even where the *Options* dialog sets one as the default.

- If none of those apply, the arguments are read as files to open for editing, and `sys.argv` carries whatever arguments were handed to IDLE itself.

[Subject index](INDEX.md) · [Previous](startup-and-code-execution.md) · [Continue](startup-failure.md)
