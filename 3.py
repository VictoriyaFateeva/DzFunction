'''
Напишите функцию, которая отображает пустой или
заполненный квадрат из некоторого символа. Функция
принимает в качестве параметров: длину стороны квадрата,
символ и переменную логического типа:
если она равна True, квадрат заполненный;
если False, квадрат пустой.
'''
def draw():
    dlina=int(input('Напишите длину:\n'))
    symbol=(input('Напишите символ:\n'))
    filled=(input('True или False:\n'))
    if filled=='True':
        for i in range(dlina):
            print(symbol * dlina)
    else:
        print(symbol *  dlina)
        for i in range(dlina - 2):
            print(symbol + ' ' * (dlina - 2) + symbol)
        print(symbol * dlina)
draw()
