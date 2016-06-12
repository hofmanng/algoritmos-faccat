#
# Escreva um algoritmo para ler 3 numeros e escrever a soma
# total dos 3 numeros lidos (usando a estrutura de repeticao
# for).
#

# Declaracao das variaveis
ac_num = 0

# Processamento
for n in range(1, 3 + 1):
    # Entrada de dados
    num = int(input("Insira um valor: "))
    # Acumulador
    ac_num = ac_num + num
# Saida de dados
print "A soma dos valores lidos e",ac_num
