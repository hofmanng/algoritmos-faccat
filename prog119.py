#
# Faca um programa que peca para n pessoas a sua idade. Ao final,
# o programa devera verificar se a media de idade da turma varia 
# entre 0 e 25, 26 e 60 e maior que 60 e entao dizer se a turma 
# e jovem, adulta ou idosa, conforme a media calculada.
#

# Declaracao das variaveis
idade = 0
ac_idade = 0
cont = 0

# Processamento
while idade != -1:
    # Entrada de dados
    idade = int(input("Insira a idade (-1 para encerrar): "))
    # Teste condicional
    if idade != -1:
        # Acumulador
        ac_idade = ac_idade + idade
        # Contador
        cont = cont + 1
# Calculo da media
media_idade = ac_idade / cont

# Teste condicional
if (media_idade > 0) and (media_idade < 25):
    print "Turma jovem"
else:
    if (media_idade >= 26) and (media_idade < 60):
        print "Turma adulta"
    else:
        if (media_idade >= 60):
            print "Turma idosa"
