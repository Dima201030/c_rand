import random

def rand(x):
    random.number = random.randint(1, x)
    rand = 0
    while rand != random.number:
        rand = int(input(f"какое число загадал компютер от 1 до {x}:"))
        if rand < random.number:
            print("не то, слишком мало")
        elif rand > random.number:
            print("ай ай ай, слишком много")
        elif rand == random.number:
            print(f"уху, молодец угадал {random.number}")
rand(10)

