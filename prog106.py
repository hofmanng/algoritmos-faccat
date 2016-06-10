#
# Faca um programa que leia 10 valores positivos e, no final, 
# escreva o maior valor lido.
#
# Observacao: Considere que todos os valores lidos serao positivos.
#


# Processamento
for num in range(1, 10 + 1):
    #Entrada de dados
    valor = int(input("Insira um valor: "))
    # Teste condicional
    if num == 1:
        maior = valor
    else:
        if valor > maior:
            maior = valor

# Saida de dados
print "Maior:",maior

