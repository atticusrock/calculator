# -*- coding: utf-8 -*-

from math import ceil #будем округлять значения в большую сторону

print('Тип рассчета: \n1. Калькулятор расхода топлива \n'
      '2. Калькулятор расхода топлива на 100км \n')

while True:                                                 #бесокнечный цикл
    function_name = int (input('Выберите тип расчета: '))

    if function_name == 1:
        average_fuel = float(input('Средний расход топлива: '))
        distance = int(input('Пройденое расстояние: '))
        fuel_price = float(input('Цена топлива за литр: '))
        n = distance / 100
        spent = n * average_fuel  # расход топлива в литрах
        money = spent * fuel_price  # расход денег на бензин
        print('\n')
        print('Расход топлива: ' + str(ceil(spent)) + 'л')
        print('Израсходовано денег на топливо: ' + str(ceil(money)) + 'р')

        # запись результата в файл
        f = open('result.txt', 'w')
        f.write('Израсходовано денег на бензин: ' + str(ceil(money)) + 'р' + '\n' + 'Расход бензина: ' + str(
            ceil(spent)) + 'л')
        f.close()

    elif function_name == 2:
        rashod = float (input('Всего израсходовано: '))  #общий расход топлива
        distance2 = int (input('Пройденое расстояние: '))
        fuel_price2 = float (input('Цена топлива за литр: '))
        math = rashod * 100 / distance2
        money2 = rashod * fuel_price2
        print('\n')
        print('Средний расход топлива л/100км: ' + str(math))
        print('Израсходовано денег на топливо: ' + str(ceil(money2)) + 'р')

        #запись результата в файл
        f = open('result.txt', 'w')
        f.write('Израсходовано денег на бензин: ' + str(ceil(money2)) + 'р' + '\n' + 'Расход бензина на 100км: ' + str(math) + 'л')
        f.close()

#результаты вычислений будут записаны в файл result.txt
#файл быдет создан автоматически в корневой директории