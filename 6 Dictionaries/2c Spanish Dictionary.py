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
    numberFormat = "Count in Spanish: {one}, {two}, {three}, ..."
    withSubstitutions = numberFormat.format(**dictionary)
    print(withSubstitutions)
    print("Spanish colors: {red}, {blue}, {green}, ...".format(**dictionary))

##    numberFormat = 'Count in Spanish: {one}, {two}, {three}, ...'
##    withSubstitutions = numberFormat.format(one='uno', two='dos', three='tres')
##    print(withSubstitutions)    

main()
