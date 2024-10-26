alpha = float(input("informe alpha:"))
x = float(input("informe X: "))
if alpha > 0.1:
    print('valor inválido para alpha')
else:
    if x < 0:
        print(alpha * x)
    else:
        print(x)

#acertei 