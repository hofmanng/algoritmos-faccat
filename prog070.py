#
# Escreva um algoritmo para pedir que a pessoa digite "f" para 
# feminino ou "m" para masculino. O algoritmo deve aceitar somente
# as letras "f" ou "m". Se o usuario digitar outra letra, o algoritmo
# nao deve aceitar e pedir para digitar novamente, informando ao 
# usuario "Resposta errada! Digite "F" ou "M".
#

# Declaracao das variaveis e entrada de dados
sexo = raw_input("Digite o sexo da pessoa (F/M): ")

# Processamento
while sexo != 'M' and  sexo != 'F':
    print "Resposta errada! Digite 'F' ou 'M'"
    sexo = raw_input("Digite o sexo da pessoa (F/M): ")
