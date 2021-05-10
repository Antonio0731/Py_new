a = input("Введите действительное положительное число: ")
b = input("Введите целое отрицательное число: ")
def my_f(x, y):
    try:
        x, y = float(x), int(y)
        if x <= 0 or y >= 0:
            return "X должен быть положительным, а Y - отрицательным"
        else:
            i = 1
            res = 1
            while i <= abs(int(y)):
                res = res * x
                i += 1
            return round(1 / res,5)
    except ValueError:
        return "Введите корректные числа"

print(my_f(a,b))