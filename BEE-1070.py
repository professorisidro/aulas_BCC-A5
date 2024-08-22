# entrada
NUM = int(input())

if NUM % 2 == 0:  # ele é par?
   INICIO = NUM + 1
else:
   INICIO = NUM
   
for cont in range(0,6):
    print(INICIO)
    INICIO = INICIO + 2