# Audit events table — winreg

| Audit event | Arguments | References |
| --- | --- | --- |
| winreg.ConnectRegistry | `computer_name`, `key` | [1] |
| winreg.CreateKey | `key`, `sub_key`, `access` | [1][2] |
| winreg.DeleteKey | `key`, `sub_key`, `access` | [1][2] |
| winreg.DeleteValue | `key`, `value` | [1] |
| winreg.DisableReflectionKey | `key` | [1] |
| winreg.EnableReflectionKey | `key` | [1] |
| winreg.EnumKey | `key`, `index` | [1] |
| winreg.EnumValue | `key`, `index` | [1] |
| winreg.ExpandEnvironmentStrings | `str` | [1] |
| winreg.LoadKey | `key`, `sub_key`, `file_name` | [1] |
| winreg.OpenKey | `key`, `sub_key`, `access` | [1] |
| winreg.OpenKey/result | `key` | [1][2][3] |
| winreg.PyHKEY.Detach | `key` | [1] |
| winreg.QueryInfoKey | `key` | [1] |
| winreg.QueryReflectionKey | `key` | [1] |
| winreg.QueryValue | `key`, `sub_key`, `value_name` | [1][2] |
| winreg.SaveKey | `key`, `file_name` | [1] |
| winreg.SetValue | `key`, `sub_key`, `type`, `value` | [1][2] |

[Subject index](INDEX.md) · [Previous](audit-events-table-webbrowser.md) · [Continue](internal-cpython-audit-events.md) · [Owning module, declaration or section: Audit events table](audit-events-table-section-introduction-and-initial-examples.md)
