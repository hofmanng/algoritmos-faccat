# 
# Ler 10 valores, calcular e escrever a media aritmetica desses 
# valores lidos.
#

# Declaracao das variaveis
soma = 0
cont = 0

# Processamento
for num in range(1, 11):
    # Entrada de dados
    valor = int(input("Insira um valor: "))
    soma = soma + valor

    cont = cont + 1

# Saida de dados
print "O media aritmetica dos valores inseridos eh",(soma / cont)
