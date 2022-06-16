import csv
from ClaseEquipo import Equipo
import numpy as np

class ManEquipo:
    __Dim=0
    __Inc=1
    __Cant=0
    def __init__(self):
        self.__Dim=ManEquipo.CalcDim()
        self.__Arr=np.empty(self.__Dim,dtype=Equipo)
    def CargaArchivo(self):
        Archivo=open("Equipos.csv","r",encoding="utf-8")
        Reader=csv.reader(Archivo,delimiter=",")
        Ban=True
        for fila in Reader:
            if Ban==True:
                Ban=False
            else:
                if self.__Cant == self.__Dim:
                    self.__Dim=self.__Dim+self.__Inc
                    self.__Arr.resize(self.__Dim)
                NuevoEquipo=Equipo(fila[0],fila[1])
                self.__Arr[self.__Cant]=NuevoEquipo
                self.__Cant=self.__Cant+1
        Archivo.close()

    def Mostrar(self):
        for Fila in self.__Arr:
            print(Fila)

    def BuscarEquipo(self,Nom):
        aux=-1
        for Equi in self.__Arr:
            if Equi.GetNom()==Nom:
                aux=Equi
        return aux

    @classmethod
    def CalcDim(cls):
        Archi=open("Equipos.csv","r",encoding="utf-8")
        Reader=csv.reader(Archi,delimiter=",")
        Fila=next(Reader)
        return int(Fila[0])

