def imc ():
    P = float(input("Informe seu peso em KG: "))  
    A = float(input("Informe sua altura em metros: "))  

    imc = P / (A * A)
    
    print(f"Seu IMC é: {imc:.2f}")
    if imc < 18.5:
        print("Classificação: Abaixo do peso")
    elif 18.5 <= imc < 25:
        print("Classificação: Peso normal")
    elif 25 <= imc < 30:
        print("Classificação: Sobrepeso")
    elif 30 <= imc < 35:
        print("Classificação: Obesidade grau 1")
    elif 35 <= imc < 40:
        print("Classificação: Obesidade grau 2")
    else:
        print("Classificação: Obesidade grau 3 (obesidade mórbida)")    
imc()


#acertei na construção do codigo porem cometi erros no usso de <, >, <= 