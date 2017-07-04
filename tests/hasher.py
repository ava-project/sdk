import unittest
import os

from avasdk.plugins.hasher import hash_plugin


dir_path = os.path.dirname(os.path.realpath(__file__))


class TestNameValidatorConfing(unittest.TestCase):

    def test_hash(self):
        expected_result = '2f419968f63073ad15448ff4174c798fd353fde709afc7eb623fbd3028d559ba'
        self.assertEqual(hash_plugin('{}/random_file.txt'.format(dir_path)), expected_result)

    def test_hash_big_file(self):
        expected_result = 'd0596c81fe4aca1ca3067fd420d6051587771a3c4e7580efc1bbde83281d7c13'
        self.assertEqual(hash_plugin('{}/long_random_file.txt'.format(dir_path)), expected_result)
