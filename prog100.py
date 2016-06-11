#
# Ler o numero de alunos existentes em uma turma e, apos isto,
# ler as notas destes alunos, calcular e escrever a media 
# aritmetica dessas notas lidas.
#

# Declaracao das variaveis e entrada de dados
num_alunos = int(input("Insira o numero de alunos existentes: "))
soma = 0

# Processamento
for num in range(1,num_alunos+1):
    nota = int(input("Insira a nota do aluno: "))
    soma = soma + nota

# Saida de dados
print "A media aritmetica da turma eh",(soma / num_alunos)

