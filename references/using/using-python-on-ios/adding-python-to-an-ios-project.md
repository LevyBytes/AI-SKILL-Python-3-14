# 7.2.2. Adding Python to an iOS project

### 7.2.2. Adding Python to an iOS project

You can bring Python into any iOS project whether it uses Swift or Objective C. The examples below stick with Objective C; for Swift, a library such as [PythonKit](https://github.com/pvieito/PythonKit) may prove useful.

To add Python to an iOS Xcode project:

1.

Either build or acquire a Python `XCFramework`. For specifics on how to build a Python `XCFramework`, refer to [Apple/iOS/README.md](https://github.com/python/cpython/tree/3.14/Apple/iOS/README.md), found inside the CPython source distribution. The bare minimum is a build covering `arm64-apple-ios` together with one of `arm64-apple-ios-simulator` or `x86_64-apple-ios-simulator`.

2.

Drag the `XCframework` into your iOS project. Throughout the steps that follow, we'll take it that the `XCframework` landed at your project's root; even so, any other spot works fine as long as you adjust the paths accordingly.

3.

Add your application code as a folder in your Xcode project. Throughout the steps that follow, we'll take it that your user code sits in a folder called `app` at your project's root; any other spot is fine if you adjust the paths to match. Be sure this folder is tied to your app target.

4.

Pick the app target: click your Xcode project's root node, and from the sidebar that opens, choose the target name.

5.

Within the “General” settings, beneath “Frameworks, Libraries and Embedded Content”, add `Python.xcframework` and choose “Embed & Sign” for it.

6.

In the “Build Settings” tab, modify the following:

  - Build Options

    - User Script Sandboxing: No

    - Enable Testability: Yes

  - Search Paths

    - Framework Search Paths: `$(PROJECT_DIR)`

    - Header Search Paths: `"$(BUILT_PRODUCTS_DIR)/Python.framework/Headers"`

  - Apple Clang - Warnings - All languages

    - Quoted Include In Framework Header: No

[Subject index](INDEX.md) · [Previous source section](tools-for-building-ios-apps.md) · [Following source section](ios-library-installation-and-interpreter-configuration.md) · [iOS prerequisites](tools-for-building-ios-apps.md) · [Build phase and interpreter setup](ios-library-installation-and-interpreter-configuration.md)
