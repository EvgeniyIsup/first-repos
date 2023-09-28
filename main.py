# def ploshad(a, b):
#     return a*b
# a = int(input("Введите высоту прямоугольника>>"))
# b = int(input("Введите ширину прямоугольника>>"))
# print(f"Площадь прямоугольника = {ploshad(a, b)}")



# import math
# def ploshad (r):
#     return math.pi * r**2
#
#
# r = int(input("Введите радиус "))
# print(f"Площадь круга = {ploshad(r)}")


# import math
# def ploshad(a, b, r):
#     result = {}
#     areaCircle = math.pi * r**2
#     areaSquare = a * b
#     result.update({"Площадь квадрата": areaSquare})
#     result.update({"Площадь круга": areaCircle})
#     return result
#
# a = int(input("Введите высоту прямоугольника>>"))
# b = int(input("Введите ширину прямоугольника>>"))
# r = int(input("Введите радиус>>"))
# for key, item in ploshad(a,b,r,).items():
#     print(f"{key}: {item}")



# import random
# def getHealth (player, enemy):
#     player = 100
#     enemy = 100
# kickPlayer = random.randint(1,20)
# kickEnemy = random.randint(1,20)
# if kickPlayer > kickEnemy:
#     enemy-=20
# elif kickPlayer < kickEnemy:
#     player-=20



import random as r
def getHealth():
    health = 100
    while True:
        a = r.randint(1,20)
        b = r.randint(1,20)
        if a>b:
            health-=20
        if health <= 0:
            print("Здоровье закончилось")
            break
getHealth()








