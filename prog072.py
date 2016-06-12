#
# Escreva um algoritmo para ler um valor positivo, ou seja, o algoritmo
# deve validar a leitura do valor para aceitar somente valores positivos.
# Se o usuario digitar um valor que nao seja positivo, deve escrever a 
# mensagem "Valor invalido, digite novamente" e repetir a leitura do valor
# ate que seja positivo. Quando o valor for positivo, o algoritmo deve 
# escrever na tela o valor lido multiplicado por 2.
#

# Declaracao das variaveis e entrada de dados
num = int(input("Insira um valor positivo: "))

# Processamento
while num < 0:
    # Teste condicional
    if num < 0:
        print "Valor invalido, digite novamente."
    # Entrada de dados
    num = int(input("Insira um valor positivo: "))
# Saida de dados
print num * 2
