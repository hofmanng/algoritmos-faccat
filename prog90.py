#
# Escreva um algoritmo que pergunte ao usuario um 
# numero e apos escreva na tela a soma total de 1 
# ate o numero lido. Exemplo: 5 = 1 + 2 + 3 + 4 + 5
# = 15.
#

# Declaracao das variaveis
n = int(input("Insira um valor: "))
soma = 0

# Loop
for a in range(1, n + 1):
    soma = soma + a
    print a,
    if a < n:
        print "+",
else:
    # Saida de dados
    print "=",soma
