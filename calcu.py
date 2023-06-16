n1 = float(input("Introduce tu primer número: ") )
n2 = float(input("Introduce tu segundo número: ") )

opcion = 0
while True:
    print("""
    Dime, ¿qué quieres hacer?
    
    1) Sumar los dos números
    2) Restar los dos números
    3) Multiplicar los dos números
    4) Cambiar los números elegidos
    5) Apagar calculadora
    """)
    opcion = int(input("Elige una opción: ") )     

elif opcion == 4:
        n1 = float(input("Introduce tu primer número: ") )
        n2 = float(input("Introduce tu segundo número: ") )
    elif opcion == 5:
        break

    else:
        print("Opción incorrecta")