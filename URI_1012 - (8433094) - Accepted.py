Arr = input().split( )
A=Arr[0]
B=Arr[1]
C=Arr[2]

TRIANGULO = (float(A) * float(C))/2
print("TRIANGULO: {:.3f}".format(TRIANGULO))
pi = 3.14159
CIRCULO= float(C)*float(C) * pi
print("CIRCULO: {:.3f}".format(CIRCULO))
TRAPEZIO = ((float(A)+float(B))*float(C))/2
print("TRAPEZIO: {:.3f}".format(TRAPEZIO))
QUADRADO= float(B)*float(B)
print("QUADRADO: {:.3f}".format(QUADRADO))
RETANGULO= float(A)*float(B)
print("RETANGULO: {:.3f}".format(RETANGULO))