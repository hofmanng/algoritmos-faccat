#
# Faca um algoritmo que leia 10 valores quaisquer, ou seja, nao
# se sabe quais valores serao lidos. Podem ser positivos ou 
# negativos. Escreva o maior valor lido.
#

# Processamento
for num in range (1, 10 + 1):
    # Entrada de dados
    valor = int(input("Insira um valor: "))
    # Testes condicionais
    if num == 1:
        maior = valor
        menor = valor
    else:
        if valor > maior:
            maior = valor
# Saida de dados
print "Maior valor:",maior
