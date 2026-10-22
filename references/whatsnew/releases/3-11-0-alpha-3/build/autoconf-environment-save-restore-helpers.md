# Python 3.11.0 alpha 3 / build / provide autoconf helpers covering saving restoring environment variables save env

[bpo-45723](https://bugs.python.org/issue?@action=redirect&bpo=45723): Provide `autoconf` helpers covering the saving and restoring of environment variables:

  - `SAVE_ENV`: Save `$CFLAGS`, `$LDFLAGS`, `$LIBS`, and `$CPPFLAGS`.

  - `RESTORE_ENV`: Restore `$CFLAGS`, `$LDFLAGS`, `$LIBS`, and `$CPPFLAGS`.

  - `WITH_SAVE_ENV([SCRIPT])`: Run `SCRIPT` wrapped with `SAVE_ENV` and `RESTORE_ENV`.

Erlend E. Aasland supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
