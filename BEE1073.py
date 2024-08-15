# entrada - o limite superior N

N = int(input())
# esse "RANGE" é diferente pois além dele ter o início e o fim, ele tb tem o quanto varia a cada passo
# neste caso: range(2, N+1, 2)
#    começa no 2
#    vai até o N+1 (mas esse N+1 nao entra na contagem)
#    a cada passo varia de 2 em 2 (soma 2)
for valor in range(2,N+1,2):
    print(valor,"^2 = ",valor**2, sep="")