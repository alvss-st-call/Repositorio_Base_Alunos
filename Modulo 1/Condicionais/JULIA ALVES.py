Nome = input("digite seu nome:")

altura = float(input("digite sua altura:"))

peso = float(input("digite seu peso:"))

imc = peso / (altura**2)
if imc < 18.5:
  print ("abaixo do peso")
elif imc < 24.9:
  print ("peso normal")
elif imc < 29.9:
  print ("sobrepeso")
elif imc < 34.9:
  print ("obesidade grau 1")
elif imc < 39.9:
  print ("obesidade grau 2")
else:
  print ("obesidade grau 3")
print (f"IMC DO PACIENTE {Nome} é {imc:2f}")
