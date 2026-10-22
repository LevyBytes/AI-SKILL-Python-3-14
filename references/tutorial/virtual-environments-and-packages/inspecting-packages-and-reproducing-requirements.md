# Inspecting packages and reproducing requirements

Details about a given package are shown by `python -m pip show`:

```console
(tutorial-env) $ python -m pip show requests
---
Metadata-Version: 2.0
Name: requests
Version: 2.7.0
Summary: Python HTTP for Humans.
Home-page: http://python-requests.org
Author: Kenneth Reitz
Author-email: me@kennethreitz.com
License: Apache 2.0
Location: /Users/akuchling/envs/tutorial-env/lib/python3.4/site-packages
Requires:

```

Every package installed in the virtual environment is listed by `python -m pip list`:

```console
(tutorial-env) $ python -m pip list
novas (3.1.1.3)
numpy (1.9.2)
pip (7.0.3)
requests (2.7.0)
setuptools (16.0)

```

A comparable rundown of the installed packages comes from `python -m pip freeze`, except its output is in the format that `python -m pip install` expects. By convention this listing often goes into a `requirements.txt` file:

```console
(tutorial-env) $ python -m pip freeze > requirements.txt
(tutorial-env) $ cat requirements.txt
novas==3.1.1.3
numpy==1.9.2
requests==2.7.0

```

You can then check `requirements.txt` into version control and ship it alongside an application. From there, users pull in every required package with `install -r`:

```console
(tutorial-env) $ python -m pip install -r requirements.txt
Collecting novas==3.1.1.3 (from -r requirements.txt (line 1))
  ...
Collecting numpy==1.9.2 (from -r requirements.txt (line 2))
  ...
Collecting requests==2.7.0 (from -r requirements.txt (line 3))
  ...
Installing collected packages: novas, numpy, requests
  Running setup.py install for novas
Successfully installed novas-3.1.1.3 numpy-1.9.2 requests-2.7.0

```

Many further options exist for `pip`. The [Installing Python modules](https://docs.python.org/3.14/installing/index.html#installing-index) guide carries the full `pip` documentation. Once you've authored a package and want to publish it on the Python Package Index, turn to the [Python packaging user guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/).

[Subject index](INDEX.md) · [Previous source section](virtual-environment-package-lifecycle.md) · [Related tutorial example and explanation](virtual-environment-package-lifecycle.md) · [Create and activate the virtual environment](creating-virtual-environments.md)
