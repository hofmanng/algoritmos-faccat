#
# Altere o exercicio 90 para exibir na tela os numeros que 
# estao sendo somados, conforme o exemplo do exercicio 90.
#

# Declaracao das variaveis e entrada de dados
n = int(input("Insira um valor: "))
soma = 0

# Processamento
for a in range(1, n + 1):
    soma = soma + a
    print a,
    if a < n:
        print "+",
else:
    # Saida de dados
    print "=",soma

# Saida de dados
print "O resultado da soma eh",soma

