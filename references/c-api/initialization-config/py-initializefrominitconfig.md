# int Py_InitializeFromInitConfig(PyInitConfig *config)

### Initialize Python

 int Py_InitializeFromInitConfig(PyInitConfig *config)

Bring up Python from the initialization configuration.

- On success, hand back `0`.

- On error, record an error within *config* and hand back `-1`.

- Should Python need to exit, set an exit code within *config* and hand back `-1`.

For the exit-code scenario, consult `PyInitConfig_GetExitcode()`.

[Subject index](INDEX.md) · [Previous source contract](pyinitconfig-addmodule.md) · [Following source contract](configuration-options.md)
