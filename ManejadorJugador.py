import csv
from Clasejugador import Jugador
class ManJugador:
    __List=None
    def __init__(self):
        self.__List=[]
    def CargaArchivo(self):
        Archivo=open("Jugadores.csv","r",encoding="utf-8")
        Reader=csv.reader(Archivo,delimiter=";")
        for fila in Reader:
            NuevoJugador=Jugador(fila[0],fila[1],fila[2],fila[3],fila[4])
            self.__List.append(NuevoJugador)
        Archivo.close()
    def Mostrar(self):
        for Fila in self.__List:
            print(Fila)
    def BuscarJugador(self,Nom):
        Band=-1
        for Jug in self.__List:
            if Jug.GetNom()==Nom:
                Band=Jug
        return Band
