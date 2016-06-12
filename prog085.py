#
# Ler um valor inteiro (aceitar somente valores entre 1 e 10) e escrever
# a tabuada de 1 a 10 do valor da frase lida em cada linha, ou seja, uma
# letra por linha.
#

# Declaracao das variaveis e entrada de dados
num = int(input("Insira um valor: "))

# Processamento
for n in range(1, 11):
    # Saida de dados
    print num,"x",n,"=",num * n
