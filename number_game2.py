import random
player =0

number = int(input("Enter number : "))
number_2 = random.randint(0, 100)
while True:
    if number_2 == number :
        print(f"computer:{number_2}","you win")
        player += 1
        break
    elif number_2 > number:
        print(f"computer:{number_2}", "go down")
        number_2 == 100
        number_2 = random.randint(0, 100)
    else:
        print(f"computer:{number_2}", "go up")
        player = number_2
        number_2 = random.randint(player, 100)
