'''
Напишите функцию, которая возвращает произведение чисел в
указанном диапазоне. Границы диапазона передаются в
качестве параметров. Если границы диапазона перепутаны
(например, 5 - верхняя граница; 25 - нижняя граница), их нужно
поменять местами.
'''
def nums():
    num1 = int(input('Введите первое число:\n'))
    num2 = int(input('Введите второе число:\n'))
    if num1<num2:
        nums_list=[]
        for i in range(num1, num2 + 1):
            nums_list.append(i)
        print(nums_list)
        proiz=1
        for i in nums_list:
            proiz*=i
        print(proiz)
    elif num1>num2:
        nums_list = []
        for i in range(num2, num1 + 1):
            nums_list.append(i)
        print(nums_list)
        proiz = 1
        for i in nums_list:
            proiz *= i
        print(proiz)
    else:
        print('Числа должны быть разные для создания диапазона')
nums()