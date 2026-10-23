# optparse - Grouping Options - Code example: Usage: &lt;yourscript&gt; [options] arg1 arg2

```text
Usage: <yourscript> [options] arg1 arg2

Options:
  -h, --help            show this help message and exit
  -v, --verbose         make lots of noise [default]
  -q, --quiet           be vewwy quiet (I'm hunting wabbits)
  -f FILE, --filename=FILE
                        write output to FILE
  -m MODE, --mode=MODE  interaction mode: novice, intermediate, or expert
                        [default: intermediate]

  Dangerous Options:
    Caution: use these options at your own risk.  It is believed that some
    of them bite.

    -g                  Group option.

  Debug Options:
    -d, --debug         Print debug information
    -s, --sql           Print all SQL statements executed
    -e                  Print every action done

```

One more method worth noting, especially when you handle option groups programmatically, is:

[Subject index](INDEX.md) · [Previous](optparse-optiongroup-class.md) · [Continue](optionparser-get-option-group.md) · [Owning module, declaration or section: optparse](optparse-parser-for-command-line-options.md) · [Owning module, declaration or section: optparse.OptionGroup](optparse-optiongroup-class.md) · [Owning module, declaration or section: Grouping Options](grouping-options.md)
