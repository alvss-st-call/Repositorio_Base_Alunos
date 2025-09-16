import random

print("🌟 Bem-vindo ao jogo de Adivinhação! 🌟")

segredo = random.randint(1, 10)
palpite = 0
tentativas = 0

while palpite != segredo:
    try:
        palpite = int(input("Tente adivinhar o número de 1 a 10: "))
        tentativas += 1
        if palpite < segredo:
            print("🔼 É mais!")
        elif palpite > segredo:
            print("🔽 É menos!")
    except ValueError:
        print("Por favor, digite um número válido.")

print(f"🎉 Parabéns! Você acertou o número {segredo} em {tentativas} tentativa(s)!")