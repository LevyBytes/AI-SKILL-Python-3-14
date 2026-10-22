# Audit events table — os

| Audit event | Arguments | References |
| --- | --- | --- |
| os.add_dll_directory | `path` | [1] |
| os.chdir | `path` | [1][2] |
| os.chflags | `path`, `flags` | [1][2] |
| os.chmod | `path`, `mode`, `dir_fd` | [1][2][3] |
| os.chown | `path`, `uid`, `gid`, `dir_fd` | [1][2][3] |
| os.exec | `path`, `args`, `env` | [1] |
| os.fork |  | [1] |
| os.forkpty |  | [1] |
| os.fwalk | `top`, `topdown`, `onerror`, `follow_symlinks`, `dir_fd` | [1] |
| os.getxattr | `path`, `attribute` | [1] |
| os.kill | `pid`, `sig` | [1] |
| os.killpg | `pgid`, `sig` | [1] |
| os.link | `src`, `dst`, `src_dir_fd`, `dst_dir_fd` | [1] |
| os.listdir | `path` | [1] |
| os.listdrives |  | [1] |
| os.listmounts | `volume` | [1] |
| os.listvolumes |  | [1] |
| os.listxattr | `path` | [1] |
| os.lockf | `fd`, `cmd`, `len` | [1] |
| os.mkdir | `path`, `mode`, `dir_fd` | [1][2] |
| os.posix_spawn | `path`, `argv`, `env` | [1][2] |
| os.putenv | `key`, `value` | [1] |
| os.remove | `path`, `dir_fd` | [1][2][3] |
| os.removexattr | `path`, `attribute` | [1] |
| os.rename | `src`, `dst`, `src_dir_fd`, `dst_dir_fd` | [1][2][3] |
| os.rmdir | `path`, `dir_fd` | [1] |
| os.scandir | `path` | [1] |
| os.setxattr | `path`, `attribute`, `value`, `flags` | [1] |
| os.spawn | `mode`, `path`, `args`, `env` | [1] |
| os.startfile | `path`, `operation` | [1] |
| os.startfile/2 | `path`, `operation`, `arguments`, `cwd`, `show_cmd` | [1] |
| os.symlink | `src`, `dst`, `dir_fd` | [1] |
| os.system | `command` | [1] |
| os.truncate | `fd`, `length` | [1][2] |
| os.unsetenv | `key` | [1] |
| os.utime | `path`, `times`, `ns`, `dir_fd` | [1] |
| os.walk | `top`, `topdown`, `onerror`, `followlinks` | [1] |

[Subject index](INDEX.md) · [Previous](audit-events-table-open.md) · [Continue](audit-events-table-pathlib.md) · [Owning module, declaration or section: Audit events table](audit-events-table-section-introduction-and-initial-examples.md)
