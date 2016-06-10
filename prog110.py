#
# Faca um programa que leia 10 valores entre 1 e 1000 (inclusive
# 1 e 1000) e no final escreva o menor valor lido. 
#

# Declaracao das variaveis
cont = 1

# Processamento
while cont <= 10:
    # Entrada de dados
    valor = int(input("Insira um valor entre 1 e 1000: "))
    # Testes condicionais
    if (valor >= 1) and (valor <= 1000):
        if cont == 1:
            menor = valor
            maior = valor
        else:
            if valor < menor:
                menor = valor
            else:
                if valor > maior:
                    maior = valor
        cont = cont + 1
    else:
        print "Valor incorreto. Insira novamente."
# Saida de dados
print "O menor valor inserido foi",menor
print "O maior valor inserido foi",maior
