#
# Escreva um algoritmo para ler uma palavra ou uma frase e escrever na
# tela uma letra da palavra ou da frase lida em cada linha, ou seja, uma
# letra por linha.
#

# Declaracao de variaveis e entrada de dados
palavra = raw_input("Insira uma palavra ou frase: ")

# Processamento
for n in range(0, (len(palavra))):
    # Saida de dados
    print palavra[n]
