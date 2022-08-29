ponto1 = input().split()
x1 = float(ponto[0])
y1 = float(ponto[1])

ponto2 = input().split ()
x2 = float(ponto2[0])
y2 = float(ponto2[1])

d = (( x2-x1)**(2)+ (y2-y1)**(2)) ** (1/2)
print('{:.4f}'.format(d))