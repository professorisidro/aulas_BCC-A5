# como eu resolvo um problema desses?
# eu sei fazer algo exatamente 5 vezes?
# sei - posso usar o FOR com o RANGE
# para cada uma das vezes
# eu sei se um numero é par/impar? SEI
# eu sei determinar quando um numero é positivo/negativo? SEI
positivos = 0
negativos = 0
pares = 0
impares = 0

for contador in range(0,5):
    valor = int(input())
    if  valor > 0 :
        positivos = positivos + 1
    elif valor < 0 :
        negativos = negativos + 1
    if valor % 2 == 0:
        pares = pares + 1
    else :
        impares = impares + 1
        
print(pares,"valor(es) par(es)")
print(impares,"valor(es) impar(es)")
print(positivos,"valor(es) positivo(s)")
print(negativos,"valor(es) negativo(s)")