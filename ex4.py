peso = float(input("Digite seu peso!(kg): "))
altura = float(input("Digite sua altura!(m): "))
imc = peso / (altura**2)

print(f"Seu imc é: {imc}")
if imc<18.5:
    print("Esta abaixo do peso!")
elif 18.5<=imc<25:
    print("Peso normal!")
else:
    print("Acima do peso!") 
