# Python 3.9.0 alpha 1 / build / binary

[bpo-36044](https://bugs.python.org/issue?@action=redirect&bpo=36044): Trim how many unit tests get exercised during the PGO generation step. The result cuts that step's runtime roughly 15x. Executing the whole unit test suite takes a long time. Because fewer code branches now run, the produced binary might end up marginally less optimized. Anyone happy to sit through the far longer build can recover the prior behavior via `./configure [..] PROFILE_TASK="-m test --pgo-extended"`. We offer no promises about which PGO task selection yields the quicker binary. People who care about this should benchmark their own workloads, since outcomes vary with the environment, workload, and compiler tool chain.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
