#
# O mesmo exercicio anterior, mas agora o programa deve validar a
# leitura do valor, ou seja, deve aceitar somente valores positivos.
#

# Declaracao das variaveis
cont = 1

# Processamento
while cont <= 10:
    # Entrada de dados
    valor = int(input("Insira um valor: "))

    #Testes condicionais
    if valor >= 0:
        if cont == 1:
            maior = valor
        else:
            if maior < valor:
                maior = valor
        cont = cont + 1
    else:
        print "Valor negativo. Insira novamente."

# Saida de dados
print "Maior valor:",maior
