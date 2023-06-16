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

    if option == 1:
        print("")
        print("RESULTADO: La suma de",n1,"+",n2,"es igual a",n1+n2)
    else:
        print("Opción incorrecta")