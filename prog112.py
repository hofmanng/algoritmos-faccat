#
# Faca um algoritmo para ler uma quantidade e a seguir ler
# esta quantidade de numeros. Depois de ler todos os numeros
# o algoritmo deve apresentar na tela o maior dos numeros lidos
# e a media dos numeros lidos.
#

# Declaracao de variaveis e entrada de dados
num = int(input("Insira a quantidade de numeros: "))
soma = 0

# Processamento
for n in range(1, num + 1):
    # Entrada de dados
    valor = int(input("Insira um valor: "))
    # Testes condicionais
    if n == 1:
        maior = valor
    else:
        if valor > maior:
            maior = valor
    # Acumulador
    soma = soma + valor

print "O maior valor lido foi",maior
print "A media dos numeros lidos eh",(soma / num)

