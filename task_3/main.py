
   
month = int(input("Введите месяц: "))
day = int(input("Введите день: "))

if day < 32 and day > 0 : #проверка на день 
 if month < 13 and month > 0  : #проверка на месяц 
  if month  == 3 or month == 4 or month == 5 :
   print("Весна")
  elif month  == 6 or month == 7 or month == 8 :
   print("Лето")
  elif month  == 9 or month == 10 or month == 11 :
   print("Осень")
  elif month  == 12 or month == 1 or month == 2 :
   print("Зима") 
 else : 
  print("введен несуществуемый месяц")
else :
 print("error")
