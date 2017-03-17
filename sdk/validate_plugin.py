"""
Function to validate plugin
"""

from .plugin_validators import (
    name_validator,
)

from .exceptions import ValidationError

validator_functions = [
    name_validator,
]

def validate_plugin(config):
    """
        Takes a plugin
    """
    errors = []
    for validator_function in validator_functions:
        try:
            validator_function(config)
        except ValidationError as error:
            errors.append(ValidationException.message)
    return errors
