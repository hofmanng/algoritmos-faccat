#
# Numa eleicao existem tres candidatos. Faca um programa que peca o
# numero total de eleitores. Peca para cada eleitor votar e ao final
# mostrar o numero de votos de cada candidato.
#

# Declaracao de variaveis e entrada de dados
num_eleitores = int(input("Insira o numero de eleitores: "))
cand1 = 0
cand2 = 0
cand3 = 0

# Processamento
for n in range(1, num_eleitores + 1):
    # Entrada de dados
    voto = raw_input("Escolha um candidato (A,B,C): ")
    
    # Teste condicional
    if voto == 'A' or voto == 'B' or voto == 'C':
        if voto == 'A':
            cand1 = cand1 + 1
        else:
            if voto == 'B':
                cand2 = cand2 + 1
            else:
                if voto == 'C':
                    cand3 = cand3 + 1
    else:
        print "Voto invalido."
# Saida de dados
print "Votos para o candidato A: ",cand1
print "Votos para o candidato B: ",cand2
print "Votos para o candidato C: ",cand3
