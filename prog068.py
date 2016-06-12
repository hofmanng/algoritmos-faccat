#
# Escreva um algoritmo para ler 2 valores e se o segundo valor informado
# for ZERO, deve ser lido um novo valor, ou seja, para o segundo valor lido
# nao pode ser aceito o valor zero. APos ler os 2 valores, imprimir o 
# resultado da divisao do primeiro valor lido pelo segundo valor lido.
#

# Declaracao de variaveis e entrada de dados
num1 = float(input("Insira o primeiro valor: "))
num2 = float(input("Insira o segundo valor: "))

# Processamento
while num2 == 0:
    num2 = int(input("Insira o segundo valor: "))

# Saida de dados 
print "A divisao dos dois valores eh",(num1 / num2)
