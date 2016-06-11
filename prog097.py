# 
# Ler 10 valores e escrever quantos desses valores lidos sao
# negativos.
#

# Declaracao das variaveis
cont = 0

# Processamento
for num in range(1, 11):
    num = int(input("Insira um valor: "))

    if num < 0:
        cont = cont + 1

# Teste condicional e saida de dados
if cont > 0:
    print "Foram inseridos",cont,"valores negativos."
else:
    print "Nao foram inseridos valores negativos."
