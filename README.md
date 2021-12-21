skelcd-control-MicroOS
===================

[![Workflow Status](https://github.com/yast/skelcd-control-MicroOS/workflows/CI/badge.svg?branch=master)](
https://github.com/yast/skelcd-control-MicroOS/actions?query=branch%3Amaster)

Installation control file for openSUSE MicroOS

See also the [documentation for the `control.xml` file][1].


## Building openSUSE Tumbleweed XML

Run `rake build` to build the final `control/control.TWMicroOS.xml` file. By
default it uses the base openSUSE Tumbleweed XML file from the
`skelcd-control-openSUSE` package.

That can be changed via the `OPENSUSE_CONTROL` environment variable to point to a Git
checkout directly:
``` shell
OPENSUSE_CONTROL=../../skelcd-control-openSUSE/control/control.openSUSE.xml rake build
```

*Note: A relative path needs to be relative to the `control` subdirectory.*

## Validation

Run `rake test:validation` to validate the built XML file. It uses `jing` for
XML validation, if that is not installed it fallbacks to `xmllint` (which
unfortunately has a worse error reporting).

You can use the `OPENSUSE_CONTROL` environment variable to set the base XML path,
see above.


[1]: https://github.com/yast/yast-installation/blob/master/doc/control-file.md
