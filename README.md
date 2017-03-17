# sdk

[![Build Status](https://travis-ci.org/ava-project/sdk.svg?branch=master)](https://travis-ci.org/ava-project/sdk)

Useful function for AVA project

## Install

You can install it with pip :

```bash
$ pip install --upgrade git+git://github.com/ava-project/sdk.git
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
