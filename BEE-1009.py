# entrada
VENDEDOR=input("")
SALARIO=float(input(""))
VENDAS=float(input(""))

# processamento
SALARIO_FINAL = SALARIO + VENDAS * 0.15 # ou VENDAS * 15 / 100

# saida
print("TOTAL = R$ %.2f" % SALARIO_FINAL)