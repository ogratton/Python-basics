"""A tiny English to Spanish dictionary is created,
using the Python dictionary type dict.
"""

def createDictionary():
    spanish = dict()
    spanish['hello'] = 'hola'
    spanish['yes'] = 'si'
    spanish['one'] = 'uno'
    spanish['two'] = 'dos'
    spanish['three'] = 'tres'
    spanish['red'] = 'rojo'
    spanish['black'] = 'negro'
    spanish['green'] = 'verde'
    spanish['blue'] = 'azul'
    return spanish

def main():
    dictionary = createDictionary()
    print('Spanish numbers: ' + dictionary['one'] + ', ' +
          dictionary['two'] + ', ' +dictionary['three'] + ', ...')
    print('Spanish colours: ' + dictionary['red'] + ', ' +
          dictionary['blue'] + ', ' + dictionary['green'] + ', ...')

main()
