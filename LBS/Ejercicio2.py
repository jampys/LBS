__author__ = 'Titan'

import Clases
import numpy as np
import matplotlib.pyplot as plt


def metodo(ciudad, anio):

    matriz= np.zeros((12, 3)) #inicializo la matriz de 12x3 con ceros

    for i in range(1, 13): #recorre de 1 a 12 inclusive
        if(i<10):
            mes="0"+str(i)
        else:
            mes=str(i)

        f=open("../../datos/"+ciudad+"/"+ciudad+"-"+mes+"-"+anio+".txt")
        it=(line for i,line in enumerate(f) if i>=1) #coloca en it todas las lineas del archivo, a excepcion de la 1ra

        suma_medias=0
        temp_min=99
        temp_max=-99
        cant_lineas=0 #variable que cuenta la cantidad de lineas de cada archivo

        for line in it:
            cant_lineas=cant_lineas+1
            palabras=line.split()

            suma_medias=suma_medias+float(palabras[1])
            if(float(palabras[3])<temp_min):
                temp_min=float(palabras[3])
            if(float(palabras[2])>temp_max):
                temp_max=float(palabras[2])


        matriz[i-1][0]=str(round(suma_medias/cant_lineas, 2)) #porque i corre de 1 a 12 inclusive
        matriz[i-1][1]=str(temp_max)
        matriz[i-1][2]=str(temp_min)

    return matriz



def graficar(anio):
    matriz_variacion=matriz_cr-matriz_co
    #print(matriz_variacion)
    #print("-----------------------------")
    for i in range(12):  #hago todas las diferencias positivas
        for j in range(3):
            if (matriz_variacion[i][j]<0):
                matriz_variacion[i][j]=matriz_variacion[i][j]*-1

    #print(matriz_variacion)


    #plt.figure(figsize=(10, 10))
    n_groups=12 #cantidad de grupos

    maximas = matriz_variacion[:,1] #devuelve la columna 1 (temperaturas maximas)
    # M[1,:] # fila 1
    #M[:,1] # columna 1
    minimas = matriz_variacion[:,2] #devuelve la columna 2 (temperaturas minimas)

    fig, ax = plt.subplots()

    index = np.arange(n_groups)
    bar_width = 0.35 #ancho de cada barra

    opacity = 0.4
    error_config = {'ecolor': '0.3'}

    plt.bar(index, maximas, bar_width,
                 alpha=opacity,
                 color='b',
                 error_kw=error_config,
                 label='Maxima')

    plt.bar(index + bar_width, minimas, bar_width,
                 alpha=opacity,
                 color='r',
                 error_kw=error_config,
                 label='Minima')

    plt.xlabel('Mes') #etiqueta eje x
    plt.ylabel('Variacion') #etiqueta eje y
    plt.title('Variacion temperaturas por mes CR-CO año 20'+anio) #titulo del grafico
    plt.xticks(index + bar_width, ('Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sept', 'Oct', 'Nov', 'Dic'))
    plt.legend()

    plt.tight_layout()
    plt.show()



def ejercicioDos():
        global matriz_cr
        global matriz_co
        KEYWORDS = ["11", "12", "13"]
        print("Programa que grafica la variacion de temperaturas maximas y minimas por cada mes durante el año ingresado "
              "para las ciudades de Comodoro Rivadavia y Cordoba")
        while True:
            anio_ingresado=input("Ingrese el año 11, 12 o 13. Para salir presione 0 >> ")
            if(anio_ingresado in KEYWORDS):
                matriz_cr=metodo("CR", anio_ingresado)
                #print(matriz_cr)
                #print("-----------------------------")
                matriz_co=metodo("CO", anio_ingresado)
                #print(matriz_co)
                #print("-----------------------------")
                graficar(anio_ingresado)
                #break
            if(anio_ingresado=="0"):
                break



ejercicioDos()