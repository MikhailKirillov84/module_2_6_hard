
#В первом поле камни с числом менялись постоянно (от 3 до 20) случайным образом, а второе было всегда пустым.
#Во вторую вставку нужно было написать те пары чисел друг за другом, чтобы число из первой вставки было кратно(делилось без остатка) сумме их значений.
#Составьте алгоритм, используя циклы, чтобы в независимости от введённого числа n (от 3 до 20) программа выдавала нужный пароль result, для одного введённого числа.


# range(start, stop) — возвращает все целые числа в промежутке от start (включая) до stop (не включая).


n = int(input("Введите число от 3 до 20: "))
result_password_1 = ""
for i in range(1, n):           #принимаем переборкой(for) первую переменную(i), в диапазоне(range) от(start "1"), до(stop "n")
    for j in range(1, n):       # принимаем вторую переменную(j), в диапазоне(range) от(start "1"), до(stop "n")
        if j <= i:              # если условие (j) меньше или равно (i) выполняется тогда, учитывается оператор(continue)
                                # и возвращаемся к условию(for j...)
            continue
                                # если условие не выполняется тогда, вычисляем следуещее условие
        if n % (i + j) == 0:    # если условие выполняется, результат записывается в переменную(result_password_1),
                                # если не выполняется, переходим к условию(for j...), где принимаем переменную(j)
                                # следующим числом в диапазоне(range) от(start "1"), до(stop "n")

            result_password_1 += str(i) + str(j)

print("Пароль: ", result_password_1)

#16 - 1317115262143531341251161079
#1317115262143531341251161079
#9 - 1218273645
#1218273645