# 4.11.4. Installing without downloading

### 4.11.4. Installing without downloading

Because some of Python's features are left out of the initial installer download, choosing those features can call for an internet connection. To sidestep that requirement, every possible component can be fetched on-demand to assemble a full *layout* that no longer needs an internet connection no matter which features you choose. Keep in mind that this download may run larger than necessary, but whenever a great many installations are planned, having a locally cached copy proves very handy.

Run the command below from Command Prompt to fetch every file that could be needed. Don't forget to swap `python-3.9.0.exe` for the real name of your installer, and to build layouts each in their own directory so that files sharing a name don't collide.

```none
python-3.9.0.exe /layout [optional target directory]

```

You can additionally add the `/quiet` option to suppress the progress display.

[Subject index](INDEX.md) · [Previous source section](installing-without-ui.md) · [Following source section](modifying-an-install.md)
