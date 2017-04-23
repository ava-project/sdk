# sdk

[![Build Status](https://travis-ci.org/ava-project/sdk.svg?branch=master)](https://travis-ci.org/ava-project/sdk)

Useful function for AVA project

## Install

You can install it with pip :

```bash
$ sudo python3 -m pip install --upgrade git+https://github.com/ava-project/sdk
```

## Run tests

```bash
$ ./runtests.sh
```

## Usage

#### Config file

You can validate a plugin config file with

```python
from avasdk.validate_plugin import validate_plugin

validate_plugin(config)
```

`config` is a dictionary
