# Run and inspect custom severity output

Then invoking it this way:

```shell
python main.py 2>stderr.log >stdout.log

```

shows us the results match what we anticipated:

```shell
$ more *.log
::::::::::::::
app.log
::::::::::::::
DEBUG    - A DEBUG message
INFO     - An INFO message
WARNING  - A WARNING message
ERROR    - An ERROR message
CRITICAL - A CRITICAL message
::::::::::::::
stderr.log
::::::::::::::
ERROR    - An ERROR message
CRITICAL - A CRITICAL message
::::::::::::::
stdout.log
::::::::::::::
INFO     - An INFO message
WARNING  - A WARNING message

```

[Subject index](INDEX.md) · [Route logging severities to stdout, stderr and file](route-logging-severities-to-stdout-stderr-and-file.md) · [Level filter factory and stdout handler configuration](level-filter-factory-and-stdout-handler-configuration.md) · [Complete custom-severity main.py](complete-custom-severity-main-py.md) · [Previous source context](complete-custom-severity-main-py.md) · [Following source context](configuration-server-example.md)
