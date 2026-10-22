# Python 3.5.0 alpha 1 / c api / compiler and parser

[bpo-22445](https://bugs.python.org/issue?@action=redirect&bpo=22445): PyBuffer_IsContiguous() has been reworked to perform exact contiguity checks that line up with NumPy’s NPY_RELAXED_STRIDES_CHECKING compilation flag. Earlier on, the routine gave false negatives in certain edge situations.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
