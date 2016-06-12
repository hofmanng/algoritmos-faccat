#
# Modifique o exercicio anterior para aceitar somente valores maiores que 
# 0 para N. Caso o valor informado (para N) nao seja maior que 0, devera 
# ser lido um novo valor para N ate que ele seja maior que 0.
#

# Declaracao de variaveis e entrada de dados
n = int(input("Insira um valor para N: "))

# Teste condicional
if n < 0:
    # Laco
    while n < 0:
        # Entrada de dados
        n = int(input("Insira um valor para N: "))
# Laco
for i in range(1, n + 1):
    # Saida de dados
    print i
