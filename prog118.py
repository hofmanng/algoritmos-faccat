#
# Faca um programa que peca 10 numeros inteiros, calcule e mostre
# a quantidade de numeros pares e a quantidade de numeros impares.
#

# Declaracao de variaveis
cont_par = 0
cont_impar = 0

# Processamento
for n in range(1, 10 + 1):
    num = int(input("Insira um numero inteiro: "))

    if (num % 2) == 0:
        cont_par = cont_par + 1
    else:
        cont_impar = cont_impar + 1
# Saidade de dados
print "Quantidade de pares: ",cont_par
print "Quantidade de impares: ",cont_impar
