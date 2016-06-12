#
# Escreva um algoritmo para ler um valor entre 1 (inclusive) e 10 (inclusive). 
# Se o valor lido nao estiver entre 1 (inclusive) e 10 (inclusive), deve ser 
# lido um novo valor.
#

# Declaracao de variaveis e entrada de dados
num = int(input("Insira um valor: "))

# Processamento
while (num < 1) or (num > 10):
    num = int(input("Insira um valor: "))

print "Programa encerrado."
