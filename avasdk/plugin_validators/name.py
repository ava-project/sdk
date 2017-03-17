import re

from ..exception import ValidationError

def name_validator(config):
    """
    Take a config file and validate the name
    """
    name = config.get('name')
    if not name:
        raise ValidateException('A plugin must contain a name ')
    pattern = re.compile(r'^[-a-zA-Z0-9_]+\Z')
    if not pattern.match(name):
        raise ValidateException('Plugin name can consist of only letters, numbers, underscores or hyphens')
