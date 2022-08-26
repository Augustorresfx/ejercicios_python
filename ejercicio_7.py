persona_1_edad = int(input("ingrese la edad de la primer persona: "))

persona_2_edad = int(input("ingrese la edad de la segunda persona: "))

if persona_1_edad >= 18 and persona_2_edad < 18 : 
    promedio = (persona_1_edad + persona_2_edad) / 2
    print(promedio)
else:
    print(str(persona_1_edad) + " " + str(persona_2_edad))