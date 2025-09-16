nome = input("digite seu nome")
primeira_nota = float (input("receber nota"))
segunda_nota = float (input("receber nota "))
terceira_nota = float(input("receber nota"))
calcular_media = (primeira_nota + segunda_nota + terceira_nota) / 3 
if calcular_media >=7:
   print ("aprovado")
elif calcular_media >=4:
    print ("recuperação")
else:
     print ("reprovado")