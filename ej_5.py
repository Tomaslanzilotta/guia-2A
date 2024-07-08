edad = int(input("ingrese su edad: "))

if edad >= 18:
    print("usted es mayor")
elif edad > 13 and edad <=17:
    print("usted es adolecente")
elif edad >=10 and edad <=13:
    print("usted es pre-adolecente")
else:
    print("usted es niño/a")
