# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Realice una calculadora:
Dentro de un bucle se debe ingresar por línea de comando dos números
Luego se ingresará como tercera entrada al programa el símbolo de la operación
que se desea ejecutar:
- Suma (+)
- Resta (-)
- Multiplicación (*)
- División (/)
- Exponente/Potencia (**)
Se debe efectuar el cálculo correcto según la operación ingresada por consola
Imprimir en pantalla la operación realizada y el resultado

El programa se debe repetir dentro del bucle hasta que como operador
se ingrese la palabra "FIN", en ese momento debe terminar el programa

Se debe debe imprimir un cartel de error si el operador ingresado no es
alguno de lo soportados o no es la palabra "FIN".
'''

print("Mi Calculadora (^_^)")
# Empezar aquí la resolución del ejercicio

# Condiciones para los bucles "while"
cond1 = False
cond2 = False
cond3 = False


print("Ingrese dos numeros seguidos de la operacion que quiere realizar")

# Bucle "While"
while True:
    # Primer variable (x)
    x = input('Primer número (o FIN para terminar)\n')
    cond1 = x.isdigit()
    while (cond1 == False) and x != 'FIN':
        print('Caracter ingresado no válido!')
        x = input('Primer número (o FIN para terminar)\n')
        cond1 = x.isdigit()
            
    if x == 'FIN':
        print('bye!')
        break        

    # Segunda variable
    while cond2 == False:
        y = input('Segundo número\n')
        cond2 = y.isdigit()
        if cond2 == False:
            print('Caracter ingresado no válido!')

    # Selecion de Operación
    while cond3 == False:
        op = input('Operacion: Suma (+) Resta (-) Multiplicación (*) División (/) Exponente/Potencia (**)\n')
        if (op == '+') or (op == '-') or (op == '*') or (op == '/') or (op == '**'):
            cond3 = True

        elif cond3 == False:
            print('Operación ingresada no válida!')

        # Suma
        if op == '+':
            resultado = int(x) + int(y)
            print('> {} + {} = {} <'.format(x, y, resultado))

        # Resta
        elif op == '-':
            resultado = int(x) - int(y)
            print('> {} - {} = {} <'.format(x, y, resultado))

        # Multiplicación
        elif op == '*':
            resultado = int(x) * int(y)
            print('> {} * {} = {} <'.format(x, y, resultado))

        # Divición
        elif op == '/':
            resultado = int(x) / int(y)
            print('> {} / {} = {} <'.format(x, y, resultado))

        # Multiplicación
        elif op == '**':
            resultado = int(x) ** int(y)
            print('> {} ** {} = {} <'.format(x, y, resultado))

    cond1 = False
    cond2 = False
    cond3 = False

    



