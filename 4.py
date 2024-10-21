'''
Напишите функцию, которая возвращает минимальное из
пяти чисел. Числа передаются в качестве параметров.
'''

def nums_min():
    nums_list=[]
    for i in range(5):
        num=(input('Напишите число:\n'))
        nums_list.append(num)
    print(nums_list)
    print('Минимальное число',min(nums_list))
nums_min()