#
# Escreva um algoritmo para ler as notas da 1a. e 2a. avaliacoes de um
# aluno, calcular e imprimir a media (simples) desse aluno. So devem 
# ser aceitos valores validos durante a leitura de cada nota (notas 
# validas: 0.0 a 10.0).
#

# Declaracao das variaveis e entrada de dados
num1 = float(input("Insira a primeira nota: "))
num2 = float(input("Insira a segunda nota: "))

# Processamento
while (num1 < 0 or num1 > 10) or (num2 < 0 or num2 > 10):
    # Testes condicionais
    if (num1 < 0 or num1 > 10):
        # Entrada de dados
        print "Primeira nota invalida"
        num1 = float(input("Insira a primeira nota: "))
    
    if (num2 < 0 or num2 > 10):
        # Entrada de dados
        print "Segunda nota invalida"
        num2 = float(input("Insira a segunda nota: "))
media = (num1 + num2) / 2
# Saida de dados
print "Media: ",media
