import cv2
import numpy as np

# Carregue a imagem
imagem = cv2.imread('Documentos/fluorescencia_ma/02_07_25_2.jpg')

# Separe os canais BGR
b_canal, g_canal, r_canal = cv2.split(imagem)

# Crie o canal amarelo (RYB)
y_canal = np.clip((r_canal + g_canal) / 2, 0, 255).astype(np.uint8)

# Crie o canal verde (RYB)
g_canal = np.clip((y_canal + b_canal) / 2, 0, 255).astype(np.uint8)

# Exiba os canais RYB (usando as funções do OpenCV que esperam BGR)
cv2.imshow('Vermelho (RYB)', r_canal)
cv2.imshow('Amarelo (RYB)', y_canal)
cv2.imshow('Azul (RYB)', b_canal)
cv2.imshow('Verde (RYB)', g_canal)

# Aguarde uma tecla para fechar as janelas
cv2.waitKey(0)
cv2.destroyAllWindows()

