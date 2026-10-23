# unittest.mock - Using side_effect to return per file content

### Using side_effect to return per file content

[`mock_open()`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.mock_open) serves to patch the [`open()`](https://docs.python.org/3.14/library/functions.html#open) method. [`side_effect`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock.side_effect) can hand back a fresh Mock object on each call. That lets you deliver distinct contents per file held in a dictionary:

```python
DEFAULT = "default"
data_dict = {"file1": "data1",
             "file2": "data2"}

def open_side_effect(name):
    return mock_open(read_data=data_dict.get(name, DEFAULT))()

with patch("builtins.open", side_effect=open_side_effect):
    with open("file1") as file1:
        assert file1.read() == "data1"

    with open("file2") as file2:
        assert file2.read() == "data2"

    with open("file3") as file2:
        assert file2.read() == "default"

```

[Subject index](INDEX.md) · [Previous](creating-a-mock-from-an-existing-object.md) · [Continue](patch-decorators-section-introduction-and-initial-examples.md) · [Owning module, declaration or section: unittest.mock](mock-patching-methods.md)
