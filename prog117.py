#
# Faca um programa que peca dois numeros, base e expoente, calcule e
# mostre o primeiro numero elevado ao segundo numero. Nao utilize a 
# funcao de potencia da linguagem.
#

# Declaracao de variaveis e entrada de dados
base = int(input("Insira a base: "))
exp = int(input("Insira o expoente: "))
mult = 1

# Processamento
for n in range(1, exp + 1):
    mult = mult * base

# Saida de dados
print mult
    
