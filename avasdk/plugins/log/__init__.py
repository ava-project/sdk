ERROR = '######## ERROR ########'

IMPORT = '######## IMPORT ########'

REQUEST = '######## REQUEST ########'

RESPONSE = '######## RESPONSE ########'

DELIMITER = '######## DELIMITER ########'

def log(response=False, request=False, importing=False, error=False):
    if error:
        print(ERROR)
    elif importing:
        print(IMPORT)
    elif request:
        print(REQUEST)
    elif response:
        print(RESPONSE)
    print(DELIMITER)

__all__ = ['log', 'ERROR', 'IMPORT', 'REQUEST', 'RESPONSE', 'DELIMITER']
