import pyautogui
import time
import math

# Abrir o Paint
pyautogui.press("win")
time.sleep(1)
pyautogui.write("paint")
time.sleep(1)
pyautogui.press("enter")
time.sleep(3)  # Tempo para o Paint abrir

# Definir o centro do círculo e o raio
center_x, center_y = 700, 400  # Ajuste se necessário
radius = 100

# Move para o ponto inicial do círculo (lado direito)
start_x = center_x + radius
start_y = center_y
pyautogui.moveTo(start_x, start_y)
time.sleep(0.5)

# Segura o botão do mouse
pyautogui.mouseDown()

# Desenha o círculo
for angle in range(0, 361, 2):  # Mais suave com passo menor
    x = center_x + radius * math.cos(math.radians(angle))
    y = center_y + radius * math.sin(math.radians(angle))
    pyautogui.moveTo(x, y, duration=0.01)

# Solta o botão do mouse
pyautogui.mouseUp()