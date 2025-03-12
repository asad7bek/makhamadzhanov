film_name = input()
cinema_name = input()
time = input()

print(f'Билет на "{film_name}" в "{cinema_name}" на {time} забронирован.')




# Программа для расчета премии за работу в выходные дни

salary_per_month = int(input("Зарплата за месяц:\n>>> ")) # Ввод месячной зарплаты

weekend_hours = int(input("Количество отработанных в выходные часов:\n>>> ")) # Ввод количества часов

# Расчет размера премии: 1% от зарплаты за каждый отработанный час в выходной
bonus = salary_per_month * (0.01 * weekend_hours)

print("Размер премии:", bonus) # Вывод размера премии







amount = int(input("Введите сумму:\n>>> "))

thousands = amount // 1000
amount %= 1000

hundreds = amount // 100
amount %= 100

tens = amount // 10
amount %= 10

ones = amount

print(f"{ones} - по 1р")
print(f"{tens} - по 10р")
print(f"{hundreds} - по 100р")
print(f"{thousands} - по 1000р")





#  прога для анализа отзывов об развлекательном комплексе

otziv_polzovatelya = input("Оцените развлекательный комплекс:\n>>> ") #  ну типа юзер пишет отзыв

otziv_malenkimi_bukvami = otziv_polzovatelya.lower() #  делаю все буквы маленькими, шоб не париться

skolko_veselo = otziv_malenkimi_bukvami.count("весело") #  ищу слово "весело" и считаем сколько раз

skolko_uvlekatelno = otziv_malenkimi_bukvami.count("увлекательно") #  ищу слово "увлекательно" и считаем сколько раз

skolko_razvlecheniya = otziv_malenkimi_bukvami.count("развлечения") #  ищу слово "развлечения" и считаем сколько раз

itog = f"{skolko_veselo} {skolko_uvlekatelno} {skolko_razvlecheniya}" #  складываем все в одну строку

print(f"Результат анализа: {itog}") #  вывод на экран, что получилось









#  прога для вывода буквы из слова, по заданным правилам
vvedennoe_slovo = input() #  прошу пользователя ввести слово

dlina = len(vvedennoe_slovo) #  узнаю скока букав в слове

if dlina % 2 != 0: #  если число букав нечетное

    srednyaya_bukovka = vvedennoe_slovo[dlina // 2] #  наход букавку посередине

    print(srednyaya_bukovka) #  показываю пользователю

else: #  если число букав четное
    poslednyaya_bukva_pervoy_chasti = vvedennoe_slovo[dlina // 2 - 1] #  берем последнюю букавку из первой половины слова
    print(poslednyaya_bukva_pervoy_chasti) #  показываю  пользователю










import re
# Прога, чтобы найти имена в отзыве и склеить их

otziv_polzovatelya = input("Введите отзыв:\n") # Вводим отзыв

найденные_имена = re.findall(r"[А-Я][а-я]+", otziv_polzovatelya) # Ищем имена
# Склеиваем имена через слэш, как просили
итог = "/".join(найденные_имена)
print(итог) # Выводим результат
otziv = 'Алиса и Вася, большое спасибо за теплый приём!'
#  находим имя Алиса
ima1 = otziv[0:5]
#  находим имя Вася
ima2 = otziv[8:12]

print(ima1)
print(ima2)




# Программа для циклического вывода букв английского алфавита

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Инициализация алфавита
index = int(input("Введите номер буквы (1-26):\n"))  # Получение номера буквы от пользователя
result = ""  # Инициализация строки результата
for i in range(4):  # Цикл для формирования строки из 4 букв
    letter_index = (index - 1 + i) % 26  # Вычисление индекса буквы с учетом циклического повторения
    result += alphabet[letter_index]  # Добавление буквы в строку результата

print(result)  # Вывод результата




#  Работа со списками - основные операции

#  1. Создание списка
my_list = []  #  пустой список
print("Создали пустой список:", my_list)

#  2. Добавление элементов
my_list.append(10)  #  добавляем в конец
my_list.insert(0, 5)  #  вставляем 5 в начало
print("Добавили элементы:", my_list)

#  3. Удаление элемента
my_list.remove(10)  #  удаляем первое вхождение 10
print("Удалили элемент:", my_list)

#  4. Срез списка
my_slice = my_list[0:1]  #  берем часть списка с 0 по 1 (не включая 1)
print("Сделали срез:", my_slice)

#  5. Переворот списка
#  Способ 1: с помощью reversed()
reversed_list = list(reversed(my_list))  #  создаем новый перевернутый список
print("Перевернули список (reversed):", reversed_list)

#  Способ 2: с помощью среза с шагом -1
reversed_list2 = my_list[::-1]  #  еще один способ перевернуть список
print("Перевернули список (срез):", reversed_list2)

#  6. Двумерный список
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  #  матрица 3x3
print("Создали двумерный список (матрицу):", matrix)

#  7. Индексация двумерного списка
element = matrix[1][2]  #  берем элемент из 2-й строки и 3-го столбца
print("Элемент из двумерного списка:", element)

#  8. Очистка списка
my_list.clear()  #  удаляем все элементы из списка
print("Очистили список:", my_list)






#  делаем кортежи

#  1. пустой кортеж
kortej_pustoy = ()  #  вот так
print("Пустой кортеж:", kortej_pustoy)

#  2. кортеж с данными
kortej_s_dannymi = (1, 2, "привет")  #  тут всякое
print("Кортеж с данными:", kortej_s_dannymi)










#  работаем с множествами, типа

#  1. делаем пустое множество
mnozhestvo_pustoe = set()  #  вот так вот
print("Пустое множество:", mnozhestvo_pustoe)

#  2. делаем множество с чем-то
mnozhestvo_s_elementami = {1, 2, 3}  #  тут уже не пусто
print("Множество с элементами:", mnozhestvo_s_elementami)

#  3. добавляем в пустое множество
mnozhestvo_pustoe.add(5)  #  добавляем пятерку
mnozhestvo_pustoe.add(10)  #  добавляем десятку
print("Добавили в пустое:", mnozhestvo_pustoe)

#  4. операции с множествами, ну там всякое
mnozhestvo1 = {1, 2, 3}
mnozhestvo2 = {3, 4, 5}

obedinenie = mnozhestvo1 | mnozhestvo2  #  склеиваем множества
print("Объединение:", obedinenie)

peresechenie = mnozhestvo1 & mnozhestvo2  #  ищем, что есть у обоих
print("Пересечение:", peresechenie)

raznost = mnozhestvo1 - mnozhestvo2  #  что есть в первом, но нет во втором
print("Разность:", raznost)

simmetricnaya_raznost = mnozhestvo1 ^ mnozhestvo2  #  что есть только в одном из множеств
print("Симметричная разность:", simmetricnaya_raznost)









#  типа работаем со словарями

#  1. делаем пустой словарь
slovarik_pustoy = {}  #  вот так
print("Пустой словарик:", slovarik_pustoy)

#  2. делаем словарик с данными
slovarik_s_dannymi = {"имя": "Петя", "возраст": 14}  #  тут имя и возраст
print("Словарик с данными:", slovarik_s_dannymi)

#  3. добавляем инфу
slovarik_pustoy["город"] = "Питер"  #  добавляем город
print("Добавили инфу:", slovarik_pustoy)

#  4. убираем инфу
del slovarik_pustoy["город"]  #  убираем город
print("Убрали инфу:", slovarik_pustoy)

#  5. меняем инфу
slovarik_s_dannymi["возраст"] = 15  #  меняем возраст
print("Поменяли инфу:", slovarik_s_dannymi)

























