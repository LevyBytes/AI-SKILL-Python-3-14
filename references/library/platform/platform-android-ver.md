# platform — Android platform

### Android platform

 platform.android_ver(*release=''*, *api_level=0*, *manufacturer=''*, *model=''*, *device=''*, *is_emulator=False*)

Collects Android device details. Hands back a [`namedtuple()`](https://docs.python.org/3.14/library/collections.html#collections.namedtuple) bearing the attributes below. Any value that cannot be worked out takes the default supplied through its parameter.

- `release` - the Android version written as a string (for example `"14"`).

- `api_level` - the API level of the device in use, given as an integer (for instance `34` for Android 14). For the API level Python itself was built against, consult [`sys.getandroidapilevel()`](https://docs.python.org/3.14/library/sys.html#sys.getandroidapilevel).

- `manufacturer` - the [Manufacturer name](https://developer.android.com/reference/android/os/Build#MANUFACTURER).

- `model` - the [Model name](https://developer.android.com/reference/android/os/Build#MODEL) – generally the marketing name or the model number.

- `device` - the [Device name](https://developer.android.com/reference/android/os/Build#DEVICE) – generally the model number or a codename.

- `is_emulator` - `True` when the device is an emulator; `False` when it is real hardware.

A [list of known model and device names](https://storage.googleapis.com/play_public/supported_devices.html) is kept up to date by Google.

Added in version 3.13.

[Subject index](INDEX.md) · [Previous](platform-freedesktop-os-release.md) · [Continue](command-line-usage.md) · [Owning module, declaration or section: platform](platform-access-to-underlying-platform-s-identifying-data.md)
