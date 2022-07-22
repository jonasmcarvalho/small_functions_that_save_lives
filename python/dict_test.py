""" txt = ['teste   de     inversão de texto?']

txt = ''.join(reversed(txt[0]))


print(txt)
 """
# teste = 'ola'.


dict_test = {
    'nome': 'Jonas',
    'sobrenome': 'Carvalho',
    'idade': 35,
    'est_civil': '',
    'carro': {
        'modelo': 'onix',
        'portas': 4
    }
}


new_dict = dict_test.fromkeys(dict_test, '1')

print(new_dict)
