def int_func():
    for word in input("Введите слова на английском через пробел (все с маленькой буквы): ").split():
        sum = 0
        for i in word:
            if 97 <= ord(i) <= 122:
                sum += 1
        print(word.title() if sum == len(word) else "В слове должны быть только маленькие латинские символы")

int_func()