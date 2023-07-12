import random
dose = []
a = 0
b = 0 
while a != 6:
    dose.append(a)
    a=random.randint(1 , 6)
    b += 1
    if a == 6 :
        print(f"Good job {b}")
        break
    else :
        print(f"Number{b} is :", a)
l = sum(dose) 
print(l + 6)