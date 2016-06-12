# 
# Ler um valor N e imprimir todos os valores inteiros entre 1 (inclusive)
# e N (inclusive). Considere que o N sera sempre maior que ZERO.
#

# Declaracao de variaveis e entrada de dados
valor = int(input("Insira um valor: "))

# Processamento
for n in range(1, valor + 1):
    # Saida de dados
    print n
