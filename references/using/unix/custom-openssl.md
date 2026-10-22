# 2.5. Custom OpenSSL

### 2.5. Custom OpenSSL

1.

If you wish to lean on your vendor's OpenSSL setup and the system trust store, track down the directory holding the `openssl.cnf` file or its symlink beneath `/etc`. Across most distributions that file sits in either `/etc/ssl` or `/etc/pki/tls`. That same directory ought to carry a `cert.pem` file, a `certs` directory, or both.

```shell
$ find /etc/ -name openssl.cnf -printf "%h\n"
/etc/ssl

```

2.

Fetch, compile, and install OpenSSL. Be certain to invoke `install_sw` rather than `install`. The `install_sw` target leaves `openssl.cnf` untouched.

```shell
$ curl -O https://www.openssl.org/source/openssl-VERSION.tar.gz
$ tar xzf openssl-VERSION
$ pushd openssl-VERSION
$ ./config \
    --prefix=/usr/local/custom-openssl \
    --libdir=lib \
    --openssldir=/etc/ssl
$ make -j1 depend
$ make -j8
$ make install_sw
$ popd

```

3.

Compile Python against your custom OpenSSL (consult the configure flags `--with-openssl` and `--with-openssl-rpath`)

```shell
$ pushd python-3.x.x
$ ./configure -C \
    --with-openssl=/usr/local/custom-openssl \
    --with-openssl-rpath=auto \
    --prefix=/usr/local/python-3.x.x
$ make -j8
$ make altinstall

```

Note

OpenSSL patch releases keep a backwards-compatible ABI, so refreshing OpenSSL does not force you to rebuild Python. Swapping the custom OpenSSL install for a newer build is all it takes.

[Subject index](INDEX.md) · [Previous source section](miscellaneous.md)
