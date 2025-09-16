nome = input("digite nome")
peso = float (input("digite peso"))
altura = float (input("digite altura"))

imc = peso / (altura**2)                                     
if imc < 18.5:
 print ("abaixo do peso")
elif imc < 24.9:
  print ("peso normal ") 
elif imc < 29.9:
  print ("sobre peso ")
elif imc < 34.9:
   print ("obesidade grau 1")
elif imc < 39.9:
   print ("obesidade grau 2")
else:
   print ("obesidade grau 3")
print (F"O IMC DO PACIENTE {nome} É {imc:.2F}")
 
 