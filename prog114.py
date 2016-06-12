#
# A prefeitura de uma cidade deseja fazer uma pesquisa entre seus
# habitantes. Faca um algoritmo para coletar dados sobre o salario
# e numero de filhos de cada habitante e apos as leituras, escrever:
#
# a) media do salario da populacao
# b) media do numero de filhos
# c) maior salario dos habitantes
# d) percentual de pessoas com salario menor que RS 150,00
#
# Observacao:
#
# O final das leituras dos dados se dara com a entrada de um salario
# negativo.
#

# Declaracao das variaveis
ac_salario = 0
ac_salario_menor = 0
ac_filhos = 0
cont_pop = 0
maior_salario = 0
salario = 0

# Processamento
while salario >= 0:
    # Entrada de dados
    salario = float(input("Insira o salario: "))
    # Teste condicional
    if salario >= 0:
        ac_salario = ac_salario + salario
        filhos = float(input("Insira o numero de filhos: "))
        ac_filhos = ac_filhos + filhos
        # Teste condicional
        if cont_pop == 1:
            maior_salario = salario
        else:
            if salario > maior_salario:
                maior_salario = salario
        # Teste condicional
        if salario < 150:
            ac_salario_menor = ac_salario_menor + 1
        # Contador
        cont_pop = cont_pop + 1
# Saida de dados
print "A media salarial da populacao e",(ac_salario / cont_pop)
print "A media do numero de filhos e",(ac_filhos / cont_pop)
print "O maior salario entre os habitantes e",maior_salario
print "O percentual de pessoas com salario menor que RS 150 e",
print ((ac_salario_menor * 100) / cont_pop),"%"
