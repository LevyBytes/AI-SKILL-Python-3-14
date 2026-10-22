# Configuration Options

### Configuration Options

| Option | PyConfig/PyPreConfig member | Type | Visibility |
| --- | --- | --- | --- |
| `"allocator"` | `allocator` | `int` | Read-only |
| `"argv"` | `argv` | `list[str]` | Public |
| `"base_exec_prefix"` | `base_exec_prefix` | `str` | Public |
| `"base_executable"` | `base_executable` | `str` | Public |
| `"base_prefix"` | `base_prefix` | `str` | Public |
| `"buffered_stdio"` | `buffered_stdio` | `bool` | Read-only |
| `"bytes_warning"` | `bytes_warning` | `int` | Public |
| `"check_hash_pycs_mode"` | `check_hash_pycs_mode` | `str` | Read-only |
| `"code_debug_ranges"` | `code_debug_ranges` | `bool` | Read-only |
| `"coerce_c_locale"` | `coerce_c_locale` | `bool` | Read-only |
| `"coerce_c_locale_warn"` | `coerce_c_locale_warn` | `bool` | Read-only |
| `"configure_c_stdio"` | `configure_c_stdio` | `bool` | Read-only |
| `"configure_locale"` | `configure_locale` | `bool` | Read-only |
| `"cpu_count"` | `cpu_count` | `int` | Public |
| `"dev_mode"` | `dev_mode` | `bool` | Read-only |
| `"dump_refs"` | `dump_refs` | `bool` | Read-only |
| `"dump_refs_file"` | `dump_refs_file` | `str` | Read-only |
| `"exec_prefix"` | `exec_prefix` | `str` | Public |
| `"executable"` | `executable` | `str` | Public |
| `"faulthandler"` | `faulthandler` | `bool` | Read-only |
| `"filesystem_encoding"` | `filesystem_encoding` | `str` | Read-only |
| `"filesystem_errors"` | `filesystem_errors` | `str` | Read-only |
| `"hash_seed"` | `hash_seed` | `int` | Read-only |
| `"home"` | `home` | `str` | Read-only |
| `"import_time"` | `import_time` | `int` | Read-only |
| `"inspect"` | `inspect` | `bool` | Public |
| `"install_signal_handlers"` | `install_signal_handlers` | `bool` | Read-only |
| `"int_max_str_digits"` | `int_max_str_digits` | `int` | Public |
| `"interactive"` | `interactive` | `bool` | Public |
| `"isolated"` | `isolated` | `bool` | Read-only |
| `"legacy_windows_fs_encoding"` | `legacy_windows_fs_encoding` | `bool` | Read-only |
| `"legacy_windows_stdio"` | `legacy_windows_stdio` | `bool` | Read-only |
| `"malloc_stats"` | `malloc_stats` | `bool` | Read-only |
| `"module_search_paths"` | `module_search_paths` | `list[str]` | Public |
| `"optimization_level"` | `optimization_level` | `int` | Public |
| `"orig_argv"` | `orig_argv` | `list[str]` | Read-only |
| `"parse_argv"` | `parse_argv` | `bool` | Read-only |
| `"parser_debug"` | `parser_debug` | `bool` | Public |
| `"pathconfig_warnings"` | `pathconfig_warnings` | `bool` | Read-only |
| `"perf_profiling"` | `perf_profiling` | `bool` | Read-only |
| `"platlibdir"` | `platlibdir` | `str` | Public |
| `"prefix"` | `prefix` | `str` | Public |
| `"program_name"` | `program_name` | `str` | Read-only |
| `"pycache_prefix"` | `pycache_prefix` | `str` | Public |
| `"quiet"` | `quiet` | `bool` | Public |
| `"run_command"` | `run_command` | `str` | Read-only |
| `"run_filename"` | `run_filename` | `str` | Read-only |
| `"run_module"` | `run_module` | `str` | Read-only |
| `"run_presite"` | `run_presite` | `str` | Read-only |
| `"safe_path"` | `safe_path` | `bool` | Read-only |
| `"show_ref_count"` | `show_ref_count` | `bool` | Read-only |
| `"site_import"` | `site_import` | `bool` | Read-only |
| `"skip_source_first_line"` | `skip_source_first_line` | `bool` | Read-only |
| `"stdio_encoding"` | `stdio_encoding` | `str` | Read-only |
| `"stdio_errors"` | `stdio_errors` | `str` | Read-only |
| `"stdlib_dir"` | `stdlib_dir` | `str` | Public |
| `"tracemalloc"` | `tracemalloc` | `int` | Read-only |
| `"use_environment"` | `use_environment` | `bool` | Public |
| `"use_frozen_modules"` | `use_frozen_modules` | `bool` | Read-only |
| `"use_hash_seed"` | `use_hash_seed` | `bool` | Read-only |
| `"use_system_logger"` | `use_system_logger` | `bool` | Read-only |
| `"user_site_directory"` | `user_site_directory` | `bool` | Read-only |
| `"utf8_mode"` | `utf8_mode` | `bool` | Read-only |
| `"verbose"` | `verbose` | `int` | Public |
| `"warn_default_encoding"` | `warn_default_encoding` | `bool` | Read-only |
| `"warnoptions"` | `warnoptions` | `list[str]` | Public |
| `"write_bytecode"` | `write_bytecode` | `bool` | Public |
| `"xoptions"` | `xoptions` | `dict[str, str]` | Public |
| `"_pystats"` | `_pystats` | `bool` | Read-only |

Visibility:

- Public: Available for reading through `PyConfig_Get()` and for writing through `PyConfig_Set()`.

- Read-only: Available for reading through `PyConfig_Get()`, yet not writable through `PyConfig_Set()`.

[Subject index](INDEX.md) · [Previous source contract](py-initializefrominitconfig.md) · [Following source contract](pyconfig-get-to-pyconfig-names.md)
