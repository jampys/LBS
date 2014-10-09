__author__ = 'Titan'



class Calculos:

    def mesATexto(self, m):
        meses={"01":"Enero:     ", "02":"Febrero:   ", "03":"Marzo:     ", "04":"Abril:     ", "05":"Mayo:      ", "06":"Junio:     ",
               "07":"Julio:     ", "08":"Agosto:    ", "09":"Septiembre:", "10":"Octubre:   ", "11":"Noviembre: ", "12":"Diciembre: "}
        return meses[m]

    def anioATexto(self, a):
        anios={"11":"2011", "12":"2012", "13":"2013"}
        return anios[a]

    def ciudadATexto(self, c):
        ciudades={"CR":"Comodoro Rivadavia", "CO":"Cordoba"}
        return ciudades[c]


    def formatoSalida(self, p):
        #print("la longitud es "+str(len(p)))
        numero=float(p)

        if(int(numero)<10 and int(numero)>=0):
            p=" "+p

        if(len(p)<=4):
            p=p+"0"

        return ""+p



#print(Calculos().formatoSalida("17.25"))
#print(Calculos().formatoSalida("7.25"))
#print(Calculos().formatoSalida("-7.25"))
#print(Calculos().formatoSalida("10.2"))
