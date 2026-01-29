peso = float(input("Peso: kg"))
altura = float(input("Altura: metros"))
imc = peso/altura**2

if imc < 18.5 :
   print("Bajo peso")
elif  18.5 < imc <= 24.9 :
    print("Normal")
elif 25 <= imc <= 29.9 :
    print("Sobrepeso")
else :
    print("Obesidad")
