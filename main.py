import random
input("загадай число, готов:" )
def c_rand(x):
    мин = 1
    макс = x
    загад_число = ''
    while загад_число != 'c':
        rand = random.randint(мин, макс)
        загад_число = input(f'если {rand} слишком большое напиши (H), маленькое  (L), или правильное (eng) (C)?? ').lower()
        if загад_число == 'h':
            high = rand - 1
        elif загад_число == 'l':
            low = rand + 1

    print(f'правильно!компютер угадал твоё чсило, {rand}, првильное!')


c_rand(10)

