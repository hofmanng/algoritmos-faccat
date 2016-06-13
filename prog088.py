#
# Escreva um algoritmo para pedir que o usuario digite
# numeros positivos, ou seja, ele pode digitar quantos
# numeros positivos ele quiser. Para parar de digitar 
# numeros, ele deve digitar -1. Apos o usuario digitar 
# -1, o programa deve escrever na tela quantos numeros 
# o usuario digitou (a quantidade de numeros lidos) e a 
# soma total dos numeros que ele digitou. Observacao: 
# Neste exercicio voce pode usar a estrutura de repeticao
# while.
#

# Entrada de dados e declaracao das variaveis
num = int(input("Insira um valor positivo (-1 para sair): "))
cont = 0
soma = 0

# Loop
while num != -1:
    # Teste condicional
    if num >= 0:
        cont = cont + 1
        soma = soma + num
    # Entrada de dados
    num = int(input("Insira um valor positivo (-1 para sair): "))

# Saida de dados
print "O numero de valores positivos inseridos foi ",cont
print "A soma total dos valores inserido e ",soma

