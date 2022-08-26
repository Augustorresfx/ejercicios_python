# Pedimos que el usuario ingrese el n° de horas mediante un input, la funcion int() convierte el valor a un número entero
horas_por_mes = int(input("Ingrese las horas que trabaja por mes: "))

# Entrada estándar para el valor de cáda hora
valor_hora = int(input("Ahora el valor de cada hora: ")) 

# Calculamos x_horas * x_valor
calcular_sueldo = (horas_por_mes) * (valor_hora)

# Salida estándar que muestra el valor del sueldo, usé la funcion str(calcular_sueldo) para poder concatenarlo con otro string
mostrar_sueldo = print("Su sueldo por mes es de: $" + str(calcular_sueldo))