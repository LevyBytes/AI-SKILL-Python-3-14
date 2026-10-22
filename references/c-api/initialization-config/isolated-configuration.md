# Isolated Configuration

### Isolated Configuration

The `PyPreConfig_InitIsolatedConfig()` and `PyConfig_InitIsolatedConfig()` functions produce a configuration that walls Python off from the surrounding system, the kind you would want when embedding Python inside an application.

Under this configuration, global configuration variables, environment variables, command line arguments (`PyConfig.argv` goes unparsed), and the user site directory are all disregarded. The C standard streams (such as `stdout`) and the LC_CTYPE locale stay as they were, and no signal handlers get installed.

Configuration files still come into use here for working out whichever paths were left unspecified. Set `PyConfig.home` so that the default path configuration need not be computed.

[Subject index](INDEX.md) · [Previous source contract](pyconfig-initialization.md) · [Following source contract](python-configuration.md)
