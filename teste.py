import calendar

""" calen = calendar.TextCalendar(calendar.SUNDAY).formatyear(2028)

print(calen)

# calen.prmonth(2024, 7)

for day in calendar.day_name:
    print(day) """


data = [

    {
        'nome': 'Jonas Carvalho',
        'sobrenome': 'teste',
        'primeiro_sobrenome': 'Marques',
        'segundo_sobrenome': 'Carvalho',
        'idade': '18',
        'cidade': 'Ariranha'
    },
    {

        'nome': 'Jonas Carvalho 1',
        'sobrenome': 'teste',
        'primeiro_sobrenome': 'Marques',
        'segundo_sobrenome': 'Carvalho',
        'idade': '18',
        'cidade': 'Ariranha'
    },
    {

        'nome': 'Jonas Carvalho 2',
        'sobrenome': 'teste',
        'primeiro_sobrenome': 'Marques',
        'segundo_sobrenome': 'Carvalho',
        'idade': '18',
        'cidade': 'Ariranha'
    },
    {

        'nome': 'Jonas Carvalho 3',
        'sobrenome': 'teste',
        'primeiro_sobrenome': 'Marques',
        'segundo_sobrenome': 'Carvalho',
        'idade': '18',
        'cidade': 'Ariranha'
    },
    {

        'nome': 'Jonas Carvalho 4',
        'sobrenome': 'teste',
        'primeiro_sobrenome': 'Marques',
        'segundo_sobrenome': 'Carvalho',
        'idade': '18',
        'cidade': 'Ariranha'
    },
    {

        'nome': 'Jonas Carvalho 5',
        'sobrenome': 'teste',
        'primeiro_sobrenome': 'Marques',
        'segundo_sobrenome': 'Carvalho',
        'idade': '18',
        'cidade': 'Ariranha'
    },
    {

        'nome': 'Jonas Carvalho 6',
        'sobrenome': 'teste',
        'primeiro_sobrenome': 'Marques',
        'segundo_sobrenome': 'Carvalho',
        'idade': '18',
        'cidade': 'Ariranha'
    },
    {

        'nome': 'Jonas Carvalho 7',
        'sobrenome': 'teste',
        'primeiro_sobrenome': 'Marques',
        'segundo_sobrenome': 'Carvalho',
        'idade': '18',
        'cidade': 'Ariranha'
    },
    {

        'nome': 'Jonas Carvalho 8',
        'sobrenome': 'teste',
        'primeiro_sobrenome': 'Marques',
        'segundo_sobrenome': 'Carvalho',
        'idade': '18',
        'cidade': 'Ariranha'
    },
    {

        'nome': 'Jonas Carvalho 9',
        'sobrenome': 'teste',
        'primeiro_sobrenome': 'Marques',
        'segundo_sobrenome': 'Carvalho',
        'idade': '18',
        'cidade': 'Ariranha'
    }
]

data = 'ULTIMO agora'


""" teste = data[9]['idade'].find('18')

print(teste) """


for index, employee in enumerate(data):

    teste = employee['nome'].find('Jonas Carvalho 15')
    print(teste)

    if teste == 0:

        print(employee)
    else:
        print(teste, 'agora')

""" data2 = ['teste', 'um', 'teste2', 'ola']

for data in data2:
    print(data) """
