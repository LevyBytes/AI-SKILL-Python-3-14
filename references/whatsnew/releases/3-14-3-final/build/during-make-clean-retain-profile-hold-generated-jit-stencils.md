# Python 3.14.3 final / build / during make clean retain profile hold generated jit stencils

[gh-141808](https://github.com/python/cpython/issues/141808): During `make clean-retain-profile`, hold on to the generated JIT stencils. This prevents the stencils from being regenerated a second time whenever Profile-guided optimization (PGO) is in use. It additionally lets distributors ship their own pre-built JIT stencils.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
