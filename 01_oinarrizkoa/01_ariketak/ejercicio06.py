cars = 10
space_in_a_car = 5
drivers = 8
passengers = 7

cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car

media_pasajeros = passengers / cars_driven

print("El número de coches disponibles: ", cars)
print("El número de conductores disponibles: ", drivers)
print("El número de coches sin conductor: ", cars_not_driven)
print("El número de personas que podemos transportar: ", carpool_capacity)
print("El número de pasajeros que podrán viajar hoy: ", passengers)
print("Media de pasajeros por coche: ", media_pasajeros)