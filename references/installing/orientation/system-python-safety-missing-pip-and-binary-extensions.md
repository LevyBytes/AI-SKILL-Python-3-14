# System Python safety, missing pip, and binary extensions

### Common installation issues

### Installing into the system Python on Linux

A Linux distribution generally ships with its own Python already in place. Adding packages into that copy calls for root access, and it risks disrupting the system package manager and other parts of the system should some component get upgraded out of turn through **pip**.

With machines like these, leaning on a virtual environment or a per-user installation while installing packages via **pip** is usually the wiser route.

### Pip not installed

There's a chance **pip** won't be set up out of the box. A possible remedy is:

```shell
python -m ensurepip --default-pip

```

Further material on [installing pip](https://packaging.python.org/en/latest/tutorials/installing-packages/#ensure-pip-setuptools-and-wheel-are-up-to-date) is available too.

### Installing binary extensions

In earlier days Python leaned heavily on shipping source, expecting the people who installed software to build extension modules from that source as part of getting things set up.

Now that the binary wheel format exists and wheels can be published on PyPI, the issue keeps shrinking, since users can far more often grab ready-built extensions instead of having to compile them on their own.

A few of the approaches used to install [scientific software](https://packaging.python.org/science/) that hasn't yet arrived as ready-built wheel files can likewise help you acquire other binary extensions without compiling them on your own machine.

See also

[Python Packaging User Guide: Binary Extensions](https://packaging.python.org/extensions/)

[Subject index](INDEX.md) · [Previous source section](per-user-scientific-and-multiple-interpreter-installation.md)
