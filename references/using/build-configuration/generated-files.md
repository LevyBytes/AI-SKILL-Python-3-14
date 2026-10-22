# 3.2. Generated files

### 3.2. Generated files

So that build dependencies stay lower, the Python source tree ships with several generated files. To rebuild all of those generated files, run:

```sh
make regen-all
make regen-stdlib-module-names
make regen-limited-abi
make regen-configure

```

Within `Makefile.pre.in` you will find documentation of the generated files together with their inputs and the tools that rebuild them. Look there for the `regen-*` make targets.

[Subject index](INDEX.md) · [Previous source section](requirements-for-optional-modules.md) · [Following source section](configure-script.md)
