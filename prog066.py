#
# Escreva um algoritmo para ler uma idade, mas o algoritmo deve aceitar
# somente idade valida, ou seja, o algoritmo deve "validar" a leitura da
# idade. Idade valida tem que ser maior que 0 e menor que 150.
#

# Declaracao das variaveis e entrada de dados
idade = int(input("Insira a idade: "))

# Processamento
while (idade > 0) and (idade < 150):
    idade = int(input("Insira a idade: "))

