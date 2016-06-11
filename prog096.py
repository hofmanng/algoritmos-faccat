# Declaracao de variaveis e entrada de dados
n1 = int(input("Insira o primeiro valor: "))
n2 = int(input("Insira o segundo valor: "))
soma = 0

# Teste condicional e troca de valores entre variaveis
if n1 >= n2:
    print "Valores com proporcoes incorretas. Efetuando mudanca."

    aux = n1
    n1 = n2
    n2 = aux

# Laco for e acumulador
for num in range(n1, n2 + 1):
    soma = soma + num
    print num,
    if num < n2:
        print "+",
# Saida de dados
else:
    print "=", soma
