# What's New In Python 3.3 / os - os, os.path, shutil

### os

- A fresh [`pipe2()`](https://docs.python.org/3.14/library/os.html#os.pipe2) function in the [`os`](https://docs.python.org/3.14/library/os.html#module-os) module lets you build a pipe whose [`O_CLOEXEC`](https://docs.python.org/3.14/library/os.html#os.O_CLOEXEC) or [`O_NONBLOCK`](https://docs.python.org/3.14/library/os.html#os.O_NONBLOCK) flags are set in a single atomic step. That capability is particularly handy for sidestepping race conditions when several threads run together.

- The [`os`](https://docs.python.org/3.14/library/os.html#module-os) module gained a [`sendfile()`](https://docs.python.org/3.14/library/os.html#os.sendfile) function that offers a fast "zero-copy" mechanism to move bytes from one file (or socket) descriptor across to another. Calling it "zero-copy" reflects that the kernel alone moves every byte between the pair of descriptors, never staging the bytes through userspace buffers. You might use `sendfile()` to stream bytes quickly from an on-disk file out to a network socket, such as when serving a file for download.

(Patch submitted by Ross Lagerwall and Giampaolo Rodol?? in [bpo-10882](https://bugs.python.org/issue?@action=redirect&bpo=10882).)

- Operating on file descriptors rather than path strings is both safer (dodging symlink attacks and the usual temporary-file and temporary-directory pitfalls) and quicker. Python 3.3 both upgrades existing functions and adds brand-new ones that operate over file descriptors ([bpo-4761](https://bugs.python.org/issue?@action=redirect&bpo=4761), [bpo-10755](https://bugs.python.org/issue?@action=redirect&bpo=10755) and [bpo-14626](https://bugs.python.org/issue?@action=redirect&bpo=14626)).

  - The [`os`](https://docs.python.org/3.14/library/os.html#module-os) module gained an [`fwalk()`](https://docs.python.org/3.14/library/os.html#os.fwalk) function that mirrors [`walk()`](https://docs.python.org/3.14/library/os.html#os.walk) but additionally yields file descriptors pointing at each directory it traverses. That extra yield is particularly handy for dodging symlink races.

  - These functions gain fresh optional *dir_fd* ([paths relative to directory descriptors](https://docs.python.org/3.14/library/os.html#dir-fd)) and/or *follow_symlinks* ([not following symlinks](https://docs.python.org/3.14/library/os.html#follow-symlinks)) arguments: [`access()`](https://docs.python.org/3.14/library/os.html#os.access), [`chflags()`](https://docs.python.org/3.14/library/os.html#os.chflags), [`chmod()`](https://docs.python.org/3.14/library/os.html#os.chmod), [`chown()`](https://docs.python.org/3.14/library/os.html#os.chown), [`link()`](https://docs.python.org/3.14/library/os.html#os.link), [`lstat()`](https://docs.python.org/3.14/library/os.html#os.lstat), [`mkdir()`](https://docs.python.org/3.14/library/os.html#os.mkdir), [`mkfifo()`](https://docs.python.org/3.14/library/os.html#os.mkfifo), [`mknod()`](https://docs.python.org/3.14/library/os.html#os.mknod), [`open()`](https://docs.python.org/3.14/library/os.html#os.open), [`readlink()`](https://docs.python.org/3.14/library/os.html#os.readlink), [`remove()`](https://docs.python.org/3.14/library/os.html#os.remove), [`rename()`](https://docs.python.org/3.14/library/os.html#os.rename), [`replace()`](https://docs.python.org/3.14/library/os.html#os.replace), [`rmdir()`](https://docs.python.org/3.14/library/os.html#os.rmdir), [`stat()`](https://docs.python.org/3.14/library/os.html#os.stat), [`symlink()`](https://docs.python.org/3.14/library/os.html#os.symlink), [`unlink()`](https://docs.python.org/3.14/library/os.html#os.unlink), [`utime()`](https://docs.python.org/3.14/library/os.html#os.utime). Whether a given platform honors these parameters can be queried through the sets [`os.supports_dir_fd`](https://docs.python.org/3.14/library/os.html#os.supports_dir_fd) and [`os.supports_follow_symlinks`](https://docs.python.org/3.14/library/os.html#os.supports_follow_symlinks).

  - These functions now permit passing a file descriptor where their path argument goes: [`chdir()`](https://docs.python.org/3.14/library/os.html#os.chdir), [`chmod()`](https://docs.python.org/3.14/library/os.html#os.chmod), [`chown()`](https://docs.python.org/3.14/library/os.html#os.chown), [`execve()`](https://docs.python.org/3.14/library/os.html#os.execve), [`listdir()`](https://docs.python.org/3.14/library/os.html#os.listdir), [`pathconf()`](https://docs.python.org/3.14/library/os.html#os.pathconf), [`exists()`](https://docs.python.org/3.14/library/os.path.html#os.path.exists), [`stat()`](https://docs.python.org/3.14/library/os.html#os.stat), [`statvfs()`](https://docs.python.org/3.14/library/os.html#os.statvfs), [`utime()`](https://docs.python.org/3.14/library/os.html#os.utime). You can confirm platform availability through the [`os.supports_fd`](https://docs.python.org/3.14/library/os.html#os.supports_fd) set.

- [`access()`](https://docs.python.org/3.14/library/os.html#os.access) takes an `effective_ids` keyword argument that switches the permission check to use the effective uid/gid in place of the real uid/gid. Whether a platform offers this is reported by the [`supports_effective_ids`](https://docs.python.org/3.14/library/os.html#os.supports_effective_ids) set.

- Two functions are new to the [`os`](https://docs.python.org/3.14/library/os.html#module-os) module: [`getpriority()`](https://docs.python.org/3.14/library/os.html#os.getpriority) and [`setpriority()`](https://docs.python.org/3.14/library/os.html#os.setpriority). They read or assign a process's niceness/priority much like [`os.nice()`](https://docs.python.org/3.14/library/os.html#os.nice) does, but reach every process rather than only the running one.

(Patch submitted by Giampaolo Rodol?? in [bpo-10784](https://bugs.python.org/issue?@action=redirect&bpo=10784).)

- The newly added [`os.replace()`](https://docs.python.org/3.14/library/os.html#os.replace) function renames a file across platforms while clobbering whatever is at the destination. By contrast [`os.rename()`](https://docs.python.org/3.14/library/os.html#os.rename) silently overwrites an existing destination on POSIX yet throws an error on Windows. (Contributed by Antoine Pitrou in [bpo-8828](https://bugs.python.org/issue?@action=redirect&bpo=8828).)

- The stat family ([`stat()`](https://docs.python.org/3.14/library/os.html#os.stat), [`fstat()`](https://docs.python.org/3.14/library/os.html#os.fstat), and [`lstat()`](https://docs.python.org/3.14/library/os.html#os.lstat)) can now read a file's timestamps down to nanosecond resolution. Mirroring that, [`utime()`](https://docs.python.org/3.14/library/os.html#os.utime) is now able to record file timestamps at nanosecond resolution too. (Contributed by Larry Hastings in [bpo-14127](https://bugs.python.org/issue?@action=redirect&bpo=14127).)

- The brand-new [`os.get_terminal_size()`](https://docs.python.org/3.14/library/os.html#os.get_terminal_size) function reports the dimensions of whatever terminal is bound to a file descriptor. Refer also to [`shutil.get_terminal_size()`](https://docs.python.org/3.14/library/shutil.html#shutil.get_terminal_size). (Contributed by Zbigniew Jędrzejewski-Szmek in [bpo-13609](https://bugs.python.org/issue?@action=redirect&bpo=13609).)

- Functions added to handle Linux extended attributes ([bpo-12720](https://bugs.python.org/issue?@action=redirect&bpo=12720)): [`getxattr()`](https://docs.python.org/3.14/library/os.html#os.getxattr), [`listxattr()`](https://docs.python.org/3.14/library/os.html#os.listxattr), [`removexattr()`](https://docs.python.org/3.14/library/os.html#os.removexattr), [`setxattr()`](https://docs.python.org/3.14/library/os.html#os.setxattr).

- A fresh interface onto the scheduler. The functions below govern the operating system's allocation of CPU time to a process. New functions: [`sched_get_priority_max()`](https://docs.python.org/3.14/library/os.html#os.sched_get_priority_max), [`sched_get_priority_min()`](https://docs.python.org/3.14/library/os.html#os.sched_get_priority_min), [`sched_getaffinity()`](https://docs.python.org/3.14/library/os.html#os.sched_getaffinity), [`sched_getparam()`](https://docs.python.org/3.14/library/os.html#os.sched_getparam), [`sched_getscheduler()`](https://docs.python.org/3.14/library/os.html#os.sched_getscheduler), [`sched_rr_get_interval()`](https://docs.python.org/3.14/library/os.html#os.sched_rr_get_interval), [`sched_setaffinity()`](https://docs.python.org/3.14/library/os.html#os.sched_setaffinity), [`sched_setparam()`](https://docs.python.org/3.14/library/os.html#os.sched_setparam), [`sched_setscheduler()`](https://docs.python.org/3.14/library/os.html#os.sched_setscheduler), [`sched_yield()`](https://docs.python.org/3.14/library/os.html#os.sched_yield),

- Fresh functions for managing the file system:

  - [`posix_fadvise()`](https://docs.python.org/3.14/library/os.html#os.posix_fadvise): Declares that data will be reached in some particular pattern, which lets the kernel apply optimizations.

  - [`posix_fallocate()`](https://docs.python.org/3.14/library/os.html#os.posix_fallocate): Guarantees that sufficient disk space gets reserved for a file.

  - [`sync()`](https://docs.python.org/3.14/library/os.html#os.sync): Force write of everything to disk.

- More new posix functions:

  - [`lockf()`](https://docs.python.org/3.14/library/os.html#os.lockf): Place, query, or release a POSIX lock against an open file descriptor.

  -

[`pread()`](https://docs.python.org/3.14/library/os.html#os.pread): Pull bytes out of a file descriptor at the given offset while keeping the descriptor's own position untouched.

  - [`pwrite()`](https://docs.python.org/3.14/library/os.html#os.pwrite): Push bytes into a file descriptor starting at the given offset, again without disturbing the descriptor's position.

  - [`readv()`](https://docs.python.org/3.14/library/os.html#os.readv): Pull bytes out of a file descriptor and spread them across several writable buffers.

  - [`truncate()`](https://docs.python.org/3.14/library/os.html#os.truncate): Shrink the file sitting at *path* until its size is no greater than *length* bytes.

  - [`waitid()`](https://docs.python.org/3.14/library/os.html#os.waitid): Block until one or more of the child processes have finished.

  - [`writev()`](https://docs.python.org/3.14/library/os.html#os.writev): Emit every buffer drawn from *buffers* into a file descriptor, with *buffers* being any sequence of buffers you supply.

  - [`getgrouplist()`](https://docs.python.org/3.14/library/os.html#os.getgrouplist) ([bpo-9344](https://bugs.python.org/issue?@action=redirect&bpo=9344)): Return list of group ids that specified user belongs to.

- [`times()`](https://docs.python.org/3.14/library/os.html#os.times) and [`uname()`](https://docs.python.org/3.14/library/os.html#os.uname): The returned value switched from a plain tuple to a tuple-like object carrying named attributes.

- A handful of platforms gain extra constants for the [`lseek()`](https://docs.python.org/3.14/library/os.html#os.lseek) function, including `os.SEEK_HOLE` and `os.SEEK_DATA`.

- Fresh constants [`RTLD_LAZY`](https://docs.python.org/3.14/library/os.html#os.RTLD_LAZY), [`RTLD_NOW`](https://docs.python.org/3.14/library/os.html#os.RTLD_NOW), [`RTLD_GLOBAL`](https://docs.python.org/3.14/library/os.html#os.RTLD_GLOBAL), [`RTLD_LOCAL`](https://docs.python.org/3.14/library/os.html#os.RTLD_LOCAL), [`RTLD_NODELETE`](https://docs.python.org/3.14/library/os.html#os.RTLD_NODELETE), [`RTLD_NOLOAD`](https://docs.python.org/3.14/library/os.html#os.RTLD_NOLOAD), and [`RTLD_DEEPBIND`](https://docs.python.org/3.14/library/os.html#os.RTLD_DEEPBIND) show up on whichever platforms can support them. They serve the [`sys.setdlopenflags()`](https://docs.python.org/3.14/library/sys.html#sys.setdlopenflags) function and take the place of the comparable constants formerly found in [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes) and `DLFCN`. (Contributed by Victor Stinner in [bpo-13226](https://bugs.python.org/issue?@action=redirect&bpo=13226).)

- On platforms other than Windows, [`os.symlink()`](https://docs.python.org/3.14/library/os.html#os.symlink) now tolerates (and quietly drops) the `target_is_directory` keyword argument, smoothing over cross-platform code.

[Subject index](INDEX.md) · [Previous source section](nntplib.md) · [Release/subject declaration](summary-release-highlights.md) · [Next source section](pdb.md)
