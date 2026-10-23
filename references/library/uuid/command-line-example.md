# uuid - Command-Line Example

### Command-Line Example

Below are a few examples showing how the `uuid` command-line interface is commonly used:

```shell
# generate a random UUID - by default uuid4() is used
$ python -m uuid

# generate a UUID using uuid1()
$ python -m uuid -u uuid1

# generate a UUID using uuid5
$ python -m uuid -u uuid5 -n @url -N example.com

# generate 42 random UUIDs
$ python -m uuid -C 42

```

[Subject index](INDEX.md) · [Previous](example.md) · [Owning module, declaration or section: uuid](uuid-safeuuid-class.md)
