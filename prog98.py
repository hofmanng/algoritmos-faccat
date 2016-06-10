#
# Ler 10 valores e escrever quantos desses valores lidos estao no intervalo
# [10, 20] (incluindo os valores 10 e 20 no intervalo e quantos deles estao
# fora do intervalo.
#

# Declaracao das variaveis
cont_fora = 0
cont_dentro = 0

# Processamento
for num in range(1, 11):
    num = int(input("Insira um valor: "))

    if (num >= 10) and (num <= 20):
        cont_dentro = cont_dentro + 1
    else:
        cont_fora = cont_fora + 1

# Saida de dados
print "Foram inseridos",cont_dentro,"dentro do intervalo 10 e 20"
print "Foram inseridos",cont_fora,"fora do intervalo 10 e 20"

