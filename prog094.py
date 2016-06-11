#
# Melhore o exercicio 93 para aceitar somente valor maior ou igual a
# zero para o numero lido e tambem para testar se o numero for igual a
# zero. O fatorial de zero e 1(0!=1).
#

# Declaracao das variaveis e entrada de dados
n = int(input("Insira um valor: "))
mlt = 1

# Testes condicionais e loop
if n >= 0:
    if n == 0:
        mlt = 1
        print " = ", mlt
    else:
        for num in range(1, n + 1):
            print num,
            if num < n:
                print "x",
            mlt = mlt * num
        else:
            # Saida de dados
            print " = ",mlt
else:
    # Mensagem de erro
    print("Valor invalido.")

