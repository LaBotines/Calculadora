#prueba para método división

def division(num1, num2):
    try:
        num1 / num2
    except ZeroDivisionError:
        print("!!Error, no se puede dividir entre 0!!")
    else:
        return num1 / num2

#test division

resultado_1 = division(num1 = 2, num2 = 0)

resultado_2 = division(num1 = 4000, num2 = 2)

resultado_3 = division(num1 = 25, num2 = 4)

print(f'El resultado de la división 1 es: {resultado_1}')
print(f'El resultado de la división 2 es: {resultado_2}')
print(f'El resultado de la división 3 es: {resultado_3}')

