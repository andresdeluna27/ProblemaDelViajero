import sys
from Ciudad import *
import random
import math
import time
file = open("solucion.txt","w")
gen=1

class Nodo(object):
    
    def __init__(self,lista):
        global gen
        self.distancia=0
        self.ciudades=[]
        self.acomodo=[]
        self.generacion=None
        self.cromosoma=0
        i=1
        while (i<26):
            self.acomodo.append(i)
            i+=1
        random.shuffle(self.acomodo)
        ind=self.acomodo.index(1)
        aux=self.acomodo[0]
        self.acomodo[0]=1
        self.acomodo[ind]=aux
        #print(self.acomodo)
        #print(len(lista))
        i=0
        while (i<25):
            #print(i)
            self.ciudades.append(lista[(self.acomodo[i])-1])
            self.generacion=gen
            i+=1
        self.longitud()
    
    def longitud(self):
        i=0
        while (i<24):
            self.distancia+=self.ciudades[i].distancia(self.ciudades[(i+1)])
            i+=1
        self.distancia+=self.ciudades[24].distancia(self.ciudades[0])
        return self.distancia

    def getDist(self):
        return str(self.distancia)

    def getList(self):
        i=0
        cad="coordenadas"
        while i<25:
            cad+=str(str(i)+" "+self.ciudades[i].impr()+" ")
            i+=1
        print(cad)

    def printOrden(self):
        aux=self.acomodo
        aux.append(1)
        return aux
        #file.write(""+str(aux))
        #file.write("\n")
        #print('distancia:  '+lista.getDist())
        #file.write('distancia:  '+lista.getDist())   
        #file.write("\n")
        #self.getList()
            
            
nodos=[]
i=1
while (i<26):
    nodos.append(Ciudad(i))
    i+=1
lista=[]
i=0
file.write("{:<12} {:<65} {:<57} {:<150}".format('Generacion','Cromosoma','Lista','Distancia'))
file.write("\n")
while (i<100):
    lista.append(Nodo(nodos))
    lista[i].cromosoma=i+1
    time.sleep(0.03)
    file.write("{:<15} {:<15} {:<100} {:<150}".format(str(lista[i].generacion),str(lista[i].cromosoma),str(lista[i].printOrden()),str(lista[i].getDist())))
    file.write("\n")
    #print('distancia:  '+lista[i].getDist())
    i+=1

lista = sorted(lista, key=lambda nodo: nodo.distancia)
i=0
#print("----------------ordenados")
while (i<100):
    #lista[i].printOrden(lista[i])
    #print('distancia:  '+lista[i].getDist())
    i+=1
file.close();
