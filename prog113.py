#
# Faca um algoritmo para ler o codigo e o preco de 15 produtos, 
# calcular e escrever:
#
# - o maior preco lido
# - a media aritmetica dos precos dos produtos
#

# Declaracao das variaveis
soma = 0

# Processamento
for n in range(1, 15 + 1):
    valor = int(input("Insira o valor: "))
    # Testes condicionais
    if n == 1:
        maior = valor
    else:
        if valor > maior:
            maior = valor
    # Acumulador
    soma = soma + valor
# Saida de dados
print "O maior preco lido foi",maior
print "A media aritmetica dos precos e",(soma / 15)
