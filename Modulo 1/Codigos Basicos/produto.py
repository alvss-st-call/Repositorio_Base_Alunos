nome_produto = input("digite o nome do produto: ")
valor_produto = float (input("digite o valor do produto: "))
desconto = float (input("digite o desconto: "))
valor_desconto = valor_produto * desconto / 100
valor_final = valor_produto -  valor_desconto

print("-------------------------------------")
print(f"produto:{nome_produto}|\npreço final:{valor_final}")
print("-------------------------------------")        