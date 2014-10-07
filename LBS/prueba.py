__author__ = 'Titan'

import Clases



def metodo(ciudad, anio):

    print("\nTemperaturas "+Clases.Calculos().ciudadATexto(ciudad)+" año "+Clases.Calculos().anioATexto(anio)+"\n")
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

        for line in it:
            palabras=line.split()
            #print(palabras[1]+"   "+palabras[2]+"   "+palabras[3])
            #print("---------------------------------")
            suma_medias=suma_medias+float(palabras[1])
            if(float(palabras[3])<temp_min):
                temp_min=float(palabras[3])
            if(float(palabras[2])>temp_max):
                temp_max=float(palabras[2])
        cant_lineas=len(open("../../datos/CR/CR-"+mes+"-"+anio+".txt").readlines())-1 #cantidad de lineas del archivo
        mesTexto=Clases.Calculos().mesATexto(mes)

        print(mesTexto+" Media "+str(round(suma_medias/cant_lineas, 2))
                      +" Minima "+str(temp_min)
                      +" Maxima "+str(temp_max)
        )
        s.write(mesTexto+" Media "+str(round(suma_medias/cant_lineas, 2))
                        +" Minima "+str(temp_min)
                        +" Maxima "+str(temp_max)+"\n")





def ejercicioUno():
        global s
        KEYWORDS = ["11", "12", "13"]
        print("Programa que muestra las temperaturas medias, maximas y minimas por cada mes durante el año ingresado"
              "para las ciudades de Comodoro Rivadavia y Caleta Olivia")
        while True:
            anio_ingresado=input("Ingrese los años 11, 12 o 13. Para salir presione 0 >> ")
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