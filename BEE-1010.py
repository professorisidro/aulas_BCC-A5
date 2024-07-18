# entrada
# neste caso a entrada é mais chata pois precisamos fazer a atribuição
# do que foi digitado com espaços em branco para as diferentes variáveis
# por isso inicialmente leremos tudo como TEXTO, separados por espaços
# isso vai ser possível com a funcionlidade split() do input()
# em seguida, fazemos as conversoes
TC1, TQ1, TP1 = input().split()
C1 = int(TC1)
Q1 = int(TQ1)
P1 = float(TP1)
TC2, TQ2, TP2 = input().split()
C2 = int(TC2)
Q2 = int(TQ2)
P2 = float(TP2)

# processamento - calcular o valor total da fatura
TOTAL = Q1 * P1 + Q2 * P2

# saída - imprimir de acordo com o formato especificado
print("VALOR A PAGAR: R$ %.2f"% TOTAL)