# 4.12.8. Return codes

### 4.12.8. Return codes

The Python launcher may hand back the exit codes below. Regrettably, there is no means of telling these apart from Python's own exit code.

The code names are the ones used in the sources and serve for reference only. There is no way to reach or resolve them other than by reading this page. The entries appear in alphabetical order by name.

| Name | Value | Description |
| --- | --- | --- |
| RC_BAD_VENV_CFG | 107 | A `pyvenv.cfg` turned up but is corrupt. |
| RC_CREATE_PROCESS | 101 | Could not launch Python. |
| RC_INSTALLING | 111 | An install got under way, but the command will have to be re-run once it finishes. |
| RC_INTERNAL_ERROR | 109 | Unexpected error. Please report a bug. |
| RC_NO_COMMANDLINE | 108 | Could not obtain the command line from the operating system. |
| RC_NO_PYTHON | 103 | Could not locate the requested version. |
| RC_NO_VENV_CFG | 106 | A `pyvenv.cfg` was needed but could not be found. |

[Subject index](INDEX.md) · [Previous source section](install-on-demand.md)
