# Is it reasonable to propose incompatible changes to Python?

### Is it reasonable to propose incompatible changes to Python?

By and large, no. Millions of lines of Python code already exist worldwide, so any language change that breaks more than a tiny slice of current programs has to be regarded unfavorably. A conversion program might help, but even then there remains the task of revising all the documentation; numerous books cover Python, and we have no wish to render them all useless overnight.

Whenever a feature must change, a gradual upgrade path has to be offered. [**PEP 5**](https://peps.python.org/pep-0005/) sets out the process used to bring in backward-incompatible changes while keeping user disruption to a minimum.

[Subject index](INDEX.md)
