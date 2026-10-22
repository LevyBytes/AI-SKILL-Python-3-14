# 4.1.7. Uninstalling runtimes

### 4.1.7. Uninstalling runtimes

```none
$> py uninstall [-y|--yes] <TAG>...

```

You can remove runtimes with the `py uninstall` command. At least one tag has to be given. Ranges are not allowed here.

The `--yes` option skips the confirmation prompt that precedes uninstalling.

Rather than listing tags one by one, you may supply the `--purge` option. It removes every runtime managed by the Python install manager, and cleans up the Start menu, registry, and any download caches as well. Runtimes that the Python install manager did not install go unaffected, as do configuration files you created manually.

```none
$> py uninstall [-y|--yes] --purge

```

You can uninstall the Python install manager via the Windows "Installed apps" settings page. That removes no runtimes, and they stay usable, though the global `python` and `py` commands disappear. Reinstalling the Python install manager lets you manage those runtimes once more. To fully clean out every Python runtime, run with `--purge` ahead of uninstalling the Python install manager.

[Subject index](INDEX.md) · [Previous source section](offline-installs.md) · [Following source section](configuration.md)
