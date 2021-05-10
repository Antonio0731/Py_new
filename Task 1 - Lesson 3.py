a = int(input("Введите 1 число: "))
b = int(input("Введите 2 число: "))
def my_f(arg_1, arg_2):
     return round(arg_1 / arg_2, 2)
try:
     print(my_f(a,b))
except ZeroDivisionError:
     print("На 0 делить нельзя!")