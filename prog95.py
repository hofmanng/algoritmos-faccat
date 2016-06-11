#
# Escreva um algoritmo para ler dois numeros e escrever a soma dos
# inteiros existentes entre os dois numeros lidos (incluindo os 
# numeros lidos na soma). Exemplo: 2 e 5 = 2+3+4+5 = 14. 
# 
# Observacao:
#
# Considere que o segundo valor lido sera sempre maior que o primeiro
# valor lido.
#

# Declaracao das variaveis e entrada de dados
n1 = int(input("Insira o primeiro valor: "))
n2 = int(input("Insira o segundo valor: "))
soma = 0

# Testes condicionais e laco
if n2 >= n1:
    for num in range(n1, n2 + 1):
        soma = soma + num
        print num,
        if num < n2:
            print "+",
    else:
        # Saida de dados
        print "=",soma
else:
    # Mensagem de erro
    print("O primeiro valor eh maior que o segundo.")

