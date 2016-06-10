#
# Uma loja esta levantando o valor total de todas as mercadorias 
# em estoque. Escreva um algoritmo que permita a entrada das 
# seguintes informacoes:
#   
#   a) Numero total de mercadorias no estoque
#   b) Valor de cada mercadoria
#
# Ao final imprimir o valor total do estoque e a media das 
# mercadorias.
#

# Declaracao de variaveis e entrada de dados
num_mercadorias = int(input("Insira o numero de mercadorias em estoque: "))
valor_total = 0

# Processamento
for num in range(1, num_mercadorias + 1):
    valor = int(input("Insira o valor da mercadoria: "))
    valor_total = valor_total + valor

media_mercadorias = valor_total / num_mercadorias

# Saida de dados
print "Valor total do estoque:",valor_total
print "Media das mercadorias:",media_mercadorias
