
class Logger(object):
    """
    """
    ERROR = '__AVA__PLUGIN__ERROR__'
    IMPORT = '__AVA__PLUGIN__IMPORT__'
    REQUEST = '__AVA__PLUGIN__REQUEST__'
    RESPONSE = '__AVA__PLUGIN__RESPONSE__'
    DELIMITER = '__AVA__PLUGIN__DELIMITER__'

    @staticmethod
    def log_error():
        print(Logger.ERROR)
        print(Logger.DELIMITER)

    @staticmethod
    def log_import():
        print(Logger.IMPORT)
        print(Logger.DELIMITER)

    @staticmethod
    def log_request():
        print(Logger.REQUEST)
        print(Logger.DELIMITER)

    @staticmethod
    def log_response():
        print(Logger.RESPONSE)
        print(Logger.DELIMITER)

    @staticmethod
    def unexpected_error(self):
        return 'An unexpected error occured with the {0}. The error has been print.'.format(self.__class__.__name__)
