#
# O mesmo exercicio anterior, mas agora nao sera informado o
# numero de mercadorias em estoque. Entao o funcionamento 
# devera ser da seguinte forma: ler o valor da mercadoria e 
# perguntar "MAIS MERCADORIAS (S/N)?". Ao final, imprimir o
# valor total em estoque e a media de valor das mercadorias
# em estoque. 
#
# OBS.: Exercicio desenvolvido em Python 2.
#

# Declaracao das variaveis
opcao = 'S'
soma = 0
cont = 0

# Processamento
while (opcao == 'S') or (opcao == 's'):
    num = int(input("Insira o valor da mercadoria: "))
    soma = soma + num
    cont = cont + 1

    opcao = raw_input("Deseja inserir mais mercadorias (S/N)?")

# Saida de dados
print "O valor total das mercadorias eh:",soma
print "A media das mercadorias eh:",(soma / cont)
