# entrada - novamente ler valores separados por espaços em branco
TA, TB, TC = input().split(" ")
A = float(TA)
B = float(TB)
C = float(TC)

# processamento
# a) a área do triângulo retângulo que tem A por base e C por altura.
AT = (A * C) / 2
# b) a área do círculo de raio C. (pi = 3.14159)
AC = 3.14159 * (C ** 2)
# c) a área do trapézio que tem A e B por bases e C por altura.
ATr = (A + B)*C/2
# d) a área do quadrado que tem lado B.
AQ = B ** 2
# e) a área do retângulo que tem lados A e B.
AR = A * B

# saida
print("TRIANGULO: %.3f" % AT)
print("CIRCULO: %.3f" % AC)
print("TRAPEZIO: %.3f" % ATr)
print("QUADRADO: %.3f" % AQ)
print("RETANGULO: %.3f" % AR)
