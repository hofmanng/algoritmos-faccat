#
# Escreva um algoritmo para ler um salario. O algoritmo deve "validar" a 
# leitura do salario para aceitar somente um "salario valido". Voce deve
# definir o que e um salario valido.
#

# Declaracao das variaveis e entrada de dados
salario_valido = float(input("Insira um salario valido: "))
salario = float(input("Insira um salario: "))

# Processamento
while salario != salario_valido:
    salario = float(input("Insira um salario: "))

print "O salario corresponde ao salario inserido anteriormente"

