import csv

import numpy as np
from ClaseContrato import Contrato
from ManejadorEquipo import Equipo
from ManejadorJugador import Jugador
class ManContrato:
    __Arr=[]
    __Inc=1
    __Cant=0
    def __init__(self):
        self.__Arr=np.empty(0,dtype=Contrato)
    def CrearContrato(self,Contrato):
        self.__Arr=np.append(self.__Arr,Contrato)
    def Mostrar(self):
        for fila in self.__Arr:
            print(fila)
    def Buscar(self,DNI):
        Band=False
        for fila in self.__Arr:
            if fila.GetDNI()==DNI:
                print(fila.Mostrar())
                Band=True
        return Band
    def Listar(self,Nom):
        for fila in self.__Arr:
            if Nom == fila.GetEqui():
                Fech=fila.GetFechF()
                AuxFech=''.join(filter(str.isalnum, Fech))
                if (30112022 < int(AuxFech)) and (int(AuxFech)<=31122022):
                    print("{}".format(fila.GetJugador()))

    def CalImp(self,Nom):
        Acum=0
        for fila in self.__Arr:
            if Nom == fila.GetEqui():
                Acum=fila.GetImp()+Acum
        print("El importe total es: {}".format(Acum))

    def GuardarContrato(self):
        Archivo=open("ArchivoGenerado.csv","w",newline="")
        writer=csv.writer(Archivo,delimiter=";")
        ListaAux=[]
        for fila in self.__Arr:
            Aux=[fila.GetDNI(),fila.GetEqui(),fila.GetFechI(),fila.GetImp()]
            ListaAux.append(Aux)
        writer.writerows(ListaAux)
