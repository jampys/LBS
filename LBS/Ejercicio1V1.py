__author__ = 'Titan'

import Clases



def metodo(ciudad, anio):

    s.write("\nTemperaturas "+Clases.Calculos().ciudadATexto(ciudad)+" año "+Clases.Calculos().anioATexto(anio)+"\n\n")

    for i in range(1, 13): #recorre de 1 a 12
        if(i<10):
            mes="0"+str(i)
        else:
            mes=str(i)

        f=open("../../datos/"+ciudad+"/"+ciudad+"-"+mes+"-"+anio+".txt")
        it=(line for i,line in enumerate(f) if i>=1) #coloca en it todas las lineas del archivo, a excepcion de la 1ra
        #lines=f.readlines()

        suma_medias=0
        temp_min=99
        temp_max=-99
        cant_lineas=0 #variable que cuenta la cantidad de lineas de cada archivo

        for line in it:
            cant_lineas=cant_lineas+1
            palabras=line.split()
            #print(palabras[1]+"   "+palabras[2]+"   "+palabras[3])
            #print("---------------------------------")
            suma_medias=suma_medias+float(palabras[1])
            if(float(palabras[3])<temp_min):
                temp_min=float(palabras[3])
            if(float(palabras[2])>temp_max):
                temp_max=float(palabras[2])

        mesTexto=Clases.Calculos().mesATexto(mes)

        s.write(mesTexto+" Media "+Clases.Calculos().formatoSalida(str(round(suma_medias/cant_lineas, 2)))
                        +"   Maxima "+Clases.Calculos().formatoSalida(str(temp_max))
                        +"   Minima "+Clases.Calculos().formatoSalida(str(temp_min)+"\n"))





def ejercicioUno():
        global s
        KEYWORDS = ["11", "12", "13"]
        print("Programa que muestra las temperaturas medias, maximas y minimas por cada mes durante el año ingresado "
              "para las ciudades de Comodoro Rivadavia y Cordoba")
        while True:
            anio_ingresado=input("Ingrese el año 11, 12 o 13. Para salir presione 0 >> ")
            if(anio_ingresado in KEYWORDS):
                #break
                #return anio_ingresado
                s=open("../../salidas/ReporteUnoCR-CO-"+anio_ingresado+".txt", "w")
                metodo("CR", anio_ingresado)
                metodo("CO", anio_ingresado)
                break
            if(anio_ingresado=="0"):
                break



ejercicioUno()