linha = intput().split()
c1 = int(linha[0])
n1 = int(linha[1])
v1 = float(linha[2])

linha2 = intput().split()
c2 = int(linha2[0])
n2 = int(linha[1])
v2 = float(linha[2])

vt = n1*v1 + n2*v2

print("valor para pagar: R$", '{:.2f''.}'.format(vt))