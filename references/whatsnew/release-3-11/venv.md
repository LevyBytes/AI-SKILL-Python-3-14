# What's New In Python 3.11 / venv — sysconfig

### venv

- To work out the paths within the environment whenever fresh Python virtual environments get built, the *venv* [sysconfig installation scheme](https://docs.python.org/3.14/library/sysconfig.html#installation-paths) is applied. While Python operates inside a virtual environment, that very same installation scheme serves as the default. So downstream distributors are free to swap the default sysconfig install scheme around while leaving virtual environment behavior intact. Outside code that likewise builds fresh virtual environments ought to follow suit. (Contributed by Miro Hrončok in [bpo-45413](https://bugs.python.org/issue?@action=redirect&bpo=45413).)

[Subject index](INDEX.md) · [Previous source section](unittest.md) · [Next source section](warnings.md) · [Release/subject declaration](summary-release-highlights.md)
