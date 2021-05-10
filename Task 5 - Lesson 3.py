def my_f():
    sum = 0
    while True:
        my_l = input("Введите числа для суммирования, q для выхода из программы: ").split()
        for i in my_l:
            if i == "q":
                return sum
            else:
                try:
                    sum += int(i)
                except ValueError:
                    print("Для выхода из программы требуется нажать q")
        print(f"Сумма = {sum}")
print(my_f())