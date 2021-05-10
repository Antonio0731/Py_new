def my_f(arg1, arg2, arg3):

    my_l = [arg1,arg2,arg3]
    try:
        my_l.remove(min(my_l))
        return sum(my_l)
    except TypeError:
        return "Введите числа!"
    except ValueError:
        return "Введите числа!"

print(my_f(5,7,6))

