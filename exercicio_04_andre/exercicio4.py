import cv2 as cv
from matplotlib.colors import Colormap
import numpy as np
import matplotlib.pyplot as plt
import argparse
import rgb2hsi

#Ler a imagem

imgOrig = cv.imread('imag.jpg')

# Questão 01 - RGB para tons de cinza (Avaliar se foi realizada a média das camadas)

imgOrigRGB = cv.cvtColor(imgOrig, cv.COLOR_BGR2RGB) #Conversão de BGR para RGB

(R,G,B) = imgOrigRGB[100,100] #Extração dos Valores de R, G e B

print('Quantidade de Vermelho: ',R)
print('Quantidade de Verde: ',G)
print('Quantidade de Azul: ',B)

imgEC = cv.cvtColor(imgOrigRGB, cv.COLOR_RGB2GRAY)

c = (0.3*R)+(0.6*G)+(0.10*B) #Equação usada para conversão

TC= imgEC[100,100]

print(TC)

# Resposta Q1:

# Foi verificado que não foi utilizada a média para a convesão de RGB para tons de cinza.
# A forma que foi feita a conversão foi a partir da equação: C = 0.3R + 0.6G + 0.10B

#Questão 02 - COnversão de RGB para HSI

imgHSI = cv.cvtColor(imgOrigRGB,cv.COLOR_RGB2HSV_FULL)


plt.figure(1)
plt.imshow(imgHSI, cmap='gray'), plt.title('Imagem HSI'), plt.autoscale(tight='both'), plt.axis('off')
plt.savefig('HSI.jpg')

# Q3 e Q4 - Identificação de cores e Objetos

#Definindo o limite das cores

def azul_hsv():

    lower_hsv_1 = np.array([90,50,70])
    higher_hsv_1 = np.array([128,255,255])
    
    mask= cv.inRange(imgHSI, lower_hsv_1,higher_hsv_1)
    
    return mask

def vermelho_hsv():

    lower_hsv= np.array([70,50,0])
    higher_hsv= np.array([255,255,9])

    mask = cv.inRange(imgHSI, lower_hsv,higher_hsv)
    

    return mask

def cor3_hsv():

    lower_hsv= np.array([0,0,0])
    higher_hsv= np.array([51,45,48])

    mask = cv.inRange(imgHSI, lower_hsv,higher_hsv)
    
    return mask

mask = vermelho_hsv()

detected_img = cv.bitwise_and(imgOrig,imgOrig,mask=mask)

cv.imshow("IMg", detected_img)
cv.waitKey(0)
cv.destroyAllWindows

#Essa da pra fazer até a 4, nesse final das definições eu chutei uns números e deu muito certo, mas aí perdi depois.
#O que vai faltar é só a parte da intensidade pra apresentar a mudança de contraste
