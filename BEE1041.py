# entrada
TC1, TC2 = input("").split()
X = float(TC1)
Y = float(TC2)
# processamento + saida
if X > 0 and Y > 0:
    print("Q1")
elif X < 0 and Y > 0:
    print("Q2")
elif X < 0 and Y < 0:
    print("Q3")
elif X > 0 and Y < 0:
    print("Q4")
elif X == 0 and Y == 0:
    print("Origem")
elif Y == 0 and X != 0:
    print("Eixo X")
elif X == 0 and Y != 0:
    print("Eixo Y")