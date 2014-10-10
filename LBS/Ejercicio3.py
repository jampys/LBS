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
    plt.rcParams['figure.figsize'] = 14, 7
    n_groups=12 #cantidad de grupos

    media_cr = matriz_cr[:,0] #devuelve la columna 0 (temperaturas medias CR)
    # M[1,:] # fila 1
    #M[:,1] # columna 1
    media_co = matriz_co[:,0] #devuelve la columna 0 (temperaturas medias CO)

    fig, ax = plt.subplots()

    index = np.arange(n_groups)
    bar_width = 0.35 #ancho de cada barra

    opacity = 0.4
    error_config = {'ecolor': '0.3'}

    plt.bar(index, media_cr, bar_width,
                 alpha=opacity,
                 color='b',
                 error_kw=error_config,
                 label='CR')

    plt.bar(index + bar_width, media_co, bar_width,
                 alpha=opacity,
                 color='r',
                 error_kw=error_config,
                 label='CO')

    plt.xlabel('Mes') #etiqueta eje x
    plt.ylabel('Temperatura media') #etiqueta eje y
    plt.title('Temperatura media mensual C. Rivadavia -  Córdoba año 20'+anio) #titulo del grafico
    plt.xticks(index + bar_width, ('Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sept', 'Oct', 'Nov', 'Dic'))
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    #plt.tight_layout()
    plt.show()




def ejercicioDos():
        global matriz_cr
        global matriz_co
        KEYWORDS = ["11", "12", "13"]
        print("Programa que grafica la temperatura media mensual durante el año ingresado "
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