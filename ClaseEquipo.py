from ClaseContrato import Contrato
class Equipo:
    __Nombre=None
    __Ciudad=None
    __Contratos=None
    def __init__(self,Nom,Ciu):
        self.__Nombre=Nom
        self.__Ciudad=Ciu
        self.__Contratos=[]
    def __str__(self):
        return "{:0} {:15}".format(self.__Nombre,self.__Ciudad)
    def GetNom(self):
        return self.__Nombre
    def AgregarContrato(self,Jugador,FechI,FechF,Pago):
        ContratoTemp=Contrato(Jugador,self,FechI,FechF,Pago)
        self.__Contratos.append(ContratoTemp)
        return ContratoTemp
