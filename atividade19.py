altura = float(input("Digite a sua altura (em metros): "))
peso = float(input("Digite o seu peso (em kg): "))
imc = peso / (altura ** 2)
print(f"\nSeu IMC é: {imc:.2f}")
if imc < 18.5:
        print("Classificação: Abaixo do peso")
elif 18.5 <= imc < 24.9:
        print("Classificação: Peso normal")
elif 25 <= imc < 29.9:
        print("Classificação: Sobrepeso")
else:
        print("Classificação: Obesidade")
