# Permission requirements

### Permission requirements

On the majority of platforms, hooking into a live Python process for remote debugging demands elevated privileges. Which requirements apply, and how to troubleshoot them, will hinge on the operating system you are running:

Linux

The capability `CAP_SYS_PTRACE`, or an equivalent privilege, must be held by the tracer process. Only processes that you own and are able to signal can be traced. The attempt may not succeed when the process is being traced already, or when it runs under set-user-ID or set-group-ID. Tracing can also be further constrained by security modules such as Yama.

Run the following to loosen ptrace restrictions on a temporary basis (lasting until the next reboot):

>

`echo 0 | sudo tee /proc/sys/kernel/yama/ptrace_scope`

Note

Turning off `ptrace_scope` weakens system hardening, so reserve it for trusted environments only.

When you operate inside a container, apply `--cap-add=SYS_PTRACE` or `--privileged`, and switch to root where that is required.

Attempt the command again, this time with elevated privileges:

>

`sudo -E !!`

macOS

In order to hook into another process, you generally have to launch your debugging tool with elevated privileges. The way to do that is with `sudo`, or by running as root.

Owing to system security restrictions, macOS may refuse to permit debugging — even for processes that you own — unless the debugger runs with root privileges.

Windows

In order to hook into another process, you normally have to launch your debugging tool with administrative privileges. Open the command prompt or terminal as Administrator.

Certain processes can still be out of reach despite Administrator rights, unless the `SeDebugPrivilege` privilege is turned on for you.

When you hit file or folder access problems, change the security permissions like so:

>
1.

Right-click on the file or folder, then choose **Properties**.

2.

Open the **Security** tab, where the users and groups holding access are listed.

3.

Press **Edit** to alter permissions.

4.

Pick your user account.

5.

Within **Permissions**, tick **Read** or **Full control** according to your needs.

6.

Press **Apply**, followed by **OK**, to commit the change.

Note

Confirm that every Permission requirement is met before you continue.

What follows describes the low-level protocol by which outside tools can inject a Python script into a live CPython process and run it there.

This machinery underpins the [`sys.remote_exec()`](https://docs.python.org/3.14/library/sys.html#sys.remote_exec) function, which directs a remote Python process to run a `.py` file. That said, the usage of that function is not covered here. Rather, what this section offers is a thorough walkthrough of the protocol underneath, which accepts as its inputs the `pid` of a target Python process together with the path of a Python source file meant to be run. With this material, the protocol can be reimplemented independently in any programming language.

Warning

Whether the injected script runs hinges on the interpreter arriving at a safe evaluation point. Consequently, how soon it runs can vary with the runtime state of the target process.

After injection, the interpreter inside the target process runs the script the next time it arrives at a safe evaluation point. By this means, remote execution becomes possible without altering how the running Python application behaves or how it is structured.

The sections that follow walk through the protocol one step at a time, covering ways to find interpreter structures in memory, read internal fields safely, and kick off code execution. Where they apply, platform-specific differences are called out, and sample implementations are supplied to make each operation clearer.

[Subject index](INDEX.md) · [Previous source context](disabling-remote-debugging.md) · [Following source context](pyruntime-discovery-model-and-linux-elf-implementation.md)
