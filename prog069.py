#
# Acrescentar uma mensagem de "VALOR INVALIDO" no exercicio 68, caso
# o segundo valor informado seja ZERO.
#

# Declaracao de variaveis e entrada de dados
num1 = float(input("Insira o primeiro valor: "))
num2 = float(input("Insira o segundo valor: "))

# Processamento
while num2 == 0:
    # Teste condicional
    if num2 == 0:
        print "Valor invalido"
    # Entrada de dados
    num2 = float(input("Insira o segundo valor: "))
# Saida de dados
print "O resultado da divisao eh", (num1 / num2)

