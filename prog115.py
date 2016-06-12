#
# Faca um programa que leia e valide as seguintes informacoes:
#
#   a) Nome: maior que 3 caracteres
#   b) Salario maior que zero
#   c) Sexo: "f" ou "m"
#

# Declaracao de variaveis e entrada de dados
nome = raw_input("Insira o nome: ")
salario = float(input("Insira o salario: "))
sexo = raw_input("Insira o sexo (f/m): ")

# Teste condicional
if (len(nome) < 3) or (salario < 0) or ((sexo != 'f') and (sexo != 'm')):
    if len(nome) < 3:
        print "Nome invalido"
    if salario < 0:
        print "Salario invalido."
    if (sexo != 'f') and (sexo != 'm'):
        print "Sexo invalido."
else:
    print "Os dados sao validos."

