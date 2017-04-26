import unittest

from avasdk.exceptions import ValidationError
from avasdk.plugin_validators import name_validator

from . import ConfigSetup

class TestNameValidatorConfing(ConfigSetup, unittest.TestCase):

    def test_has_name(self):
        with self.assertRaises(ValidationError):
            name_validator(self.no_name_config)

    def test_wrong_name(self):
        with self.assertRaises(ValidationError):
            name_validator(self.wrong_name_config)

    def test_corect_name(self):
        # should not raise exception
        name_validator(self.good_config)
