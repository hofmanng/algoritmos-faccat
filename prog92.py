#
# Melhore o exercicio 91 para aceitar somente valores maiores que
# zero para o numero lido.
#

# Declaracao das variaveis e entrada de dados
n = int(input("Insira um valor: "))
soma = 0

# Processamento
if n > 0:
    for a in range(1, n + 1):
        soma = soma + a
        print a,
        if a < n:
            print "+",
    else:
        # Saida de dados
        print "=",soma
else:
    # Mensagem de erro
    print "Insira um valor maior que zero"
