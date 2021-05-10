name = str(input("Введите ваше имя: "))
surname = str(input("Введите вашу фамилию: "))
year = int(input("Введите год рождения: "))
city = str(input("Введите город вашего проживания: "))
email = str(input("Введите ваш e-mail: "))
mobile = str(input("Введите ваш номер мобильного телефона: "))
def my_f(arg1, arg2 , arg3, arg4, arg5, arg6):
    print(f"Имя: {arg1}, Фамилия: {arg2}, Год рождения: {arg3}, Город проживания: {arg4}, E-mail: {arg5}, Мобильный: {arg6}")
my_f(arg1 = name, arg2 = surname, arg3 = year, arg4 = city, arg5 = email, arg6 = mobile)