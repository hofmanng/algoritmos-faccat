#
# Escreva um algoritmo para ler 10 numeros. Todos os numeros lidos
# com valor inferior a 40 devem ser somados. Escreva o valor final
# da soma efetuada.
#

# Declaracao das variaveis
soma = 0

# Processamento
for num in range(1, 11):
    num = int(input("Insira um valor: "))

    if num < 40:
        soma = soma + num

# Saida de dados
print "A soma dos valores menores que 40 eh igual a", soma
