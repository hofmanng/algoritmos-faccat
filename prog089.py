# 
# Escreva um algoritmo que pergunte ao usuario quantos
# numeros ele quer digitar. Apos isto, o algoritmo deve
# ir lendo os numeros que o usuario digitar e armazenar 
# a soma total dos numeros lidos. Apos a leitura dos 
# numeros, escrever na tela a soma calculada. 
#

# Declaracao das variaveis e entrada de dados
n = int(input("Insira o numero de valores que devem ser lidos: "))
soma = 0

# Processamento
for x in range(n):
    num = int(input("Insira um valor: "))
    soma = soma + num
# Saida de dados
print "A soma total dos valores inseridos eh",soma
