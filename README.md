# hotswap
Automatic replacement of imported Python modules.

The hotswap module watches the source files of imported modules which are replaced by its new version when the respective source files change. The need for a program restart during development of long-running programs like GUI applications for example is reduced.

Additionally this module can be called as a wrapper script: hotswap.py [OPTIONS] <module.py> [args]

In this case module.py is imported as module and the function module.main() is called. Hotswapping is enabled so that changes in the source code take effect without restarting the program.

