import math

a = int(input("Ведите число a: "))
b = int(input("Ведите число b: "))
c = int(input("Ведите число c: "))

D = pow(b,2) - 4*a*c

if D > 0 :
 print("Уравнение имеет 2 корня: ")
 x1 = (-b + math.sqrt(D)) / 2*a
 x2 = (-b - math.sqrt(D)) / 2*a
 print("x1 = ",x1)
 print("x2 = ",x2)
elif D < 0 :
 print("Нет корней")
elif D == 0 :
 print("Уравнение имеет 1 корень: ") 
 x1 = (-b + math.sqrt(D)) / 2*a
 