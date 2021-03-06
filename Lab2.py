# Задані дійсні числа x, y. Визначити, чи належить точка з координатами (x, y) заштрихованій частині площини.
x = float(input("Введіть координату х:")) #Координата х
y = float(input("Введіть координату у:")) #Координата у
r = 3 #Радіус кола
doesnt_belong_area = "Точка не належить заштрихованій частині"


if (x**2+y**2 > r**2):  # Ознака неналежності колу
    if x > 0 or y < 0:  # Ознака неналежності другій чверті 
        if x < r and x > -r and y < r and y > -r:  # Ознака належності квадрату
            print("Точка належить заштрихованій частині")
        else:
            print(doesnt_belong_area)
    else:
        print(doesnt_belong_area)
else:
    print(doesnt_belong_area)


# Приклади контрольних точок:
# (1;1) - точка лежить в межах кола => Не належить заштрихованій частині
# (4;-2) - точка лежить за межами квадрату => Не належить заштрихованій частині
# (-3;3) - точка лежить у другій чверті => Не належить заштрихованій частині
# (2,8;2,8) - точка не лежить в колі, не лежить у другій чверті, лежить в межах квадрата => Належить заштрихованій частині

