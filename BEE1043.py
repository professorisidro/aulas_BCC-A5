#entrada
TA,TB,TC = input("").split()
A = float(TA)
B = float(TB)
C = float(TC)

if A + B > C and A + C > B and B + C > A:
    PER = A + B + C
    print("Perimetro = %.1f" % PER)
else:
    ARE = (A + B)*C / 2
    print("Area = %.1f" % ARE)
    
