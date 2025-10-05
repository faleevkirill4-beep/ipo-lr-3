import math

x = int(input("Введите x: "))#значение по x
y = int(input("Введите y: "))#значение по y
R = int(input("Введите радиус: "))#значение радиуса 

distance = math.sqrt(pow(x,2)+pow(y,2))

if R > distance or R == distance:
    print("точка попадает в окружность")
else :
    print("точка не попадает в окружность")
   


