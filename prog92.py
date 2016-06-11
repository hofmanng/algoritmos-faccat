n = int(input("Insira um valor: "))
soma = 0

if(n > 0):
    for a in range(1, n + 1):
        soma = soma + a

    print "A soma total eh", soma
else:
    print "Insira um valor maior que zero"

