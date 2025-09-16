import time

print("-------------------------------")
print("MERCADO LIVRE")
print("--------------------------------")
usuario = input("digite seu usario:")
senha = input("digite sua senha ")

print("carregando.........")
time.sleep(3)
if usuario == "aluno" and senha == "12345678":
    print("✅login bem-sucedido!!!!!!✅")
    print(f"bem vindo{usuario}")
else:
    print ("❌ usuario ou senha incorreta ❌")