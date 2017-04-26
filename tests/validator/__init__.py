

class ConfigSetup(object):

    def setUp(self):
        self.no_name_config = {}
        self.wrong_name_config = {
            'name': 'wrong_n@me',
        }
        self.good_config = {
            'name': 'goodname'
        }
