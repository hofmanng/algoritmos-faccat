#
# Escreva um algoritmo que pergunte ao usuario um numero e apos, escreva
# na tela o fatorial do numero lido. Exemplo: 1*2*3*4*5 = 120.
#

# Declaracao de variaveis e entrada de dados
n = int(input("Insira um valor: "))
mlt = 1

# Processamento
for num in range(1, n + 1):
    print num,
    if num < n:
        print "x",
    mlt = mlt * num
else:
    # Saida de dados
    print "=",mlt


