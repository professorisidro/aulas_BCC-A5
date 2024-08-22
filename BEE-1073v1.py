# entrada
N = int(input())

for valor in range(1, N+1):
    if valor % 2 == 0:
        print(valor,"^2 = ", valor**2, sep="")