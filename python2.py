running_total = 0
num_of_friends = 4
appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21

running_total = appetizers + main_courses + desserts + drinks

print("Total bill so far:", running_total)

# Calcular la propina del 25%
tip = running_total * 0.25
print("Tip amount:", tip)

# Agregar la propina al total usando el operador +=
running_total += tip
print("Total with tip:", running_total)

# Dividir el total entre el número de amigos
final_bill = running_total / num_of_friends

# Redondear a dos decimales
each_pays = round(final_bill, 2)

# Mostrar cuánto paga cada persona con dos decimales
print("Each person pays:", each_pays)