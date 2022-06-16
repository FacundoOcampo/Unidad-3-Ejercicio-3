class Contrato:
    __FechIni=None
    __FechFin=None
    __PagoMen=None
    __Equipo=None
    __DNIJugador=None
    def __init__(self,Jugador,Equipo,FechI,FechF,Pago):
        self.__FechIni=FechI
        self.__FechFin=FechF
        self.__PagoMen=Pago
        self.__Equipo=Equipo
        self.__DNIJugador=Jugador
    def __str__(self):
        return "     Contrado de {} en {}".format(self.__DNIJugador.GetNom(),self.__Equipo.GetNom())
    def GetDNI(self):
        return self.__DNIJugador.GetDNI()
    def Mostrar(self):
        return "     Jugador de: {} su fecha de finalizacion es: {}".format(self.__Equipo.GetNom(),self.__FechFin)
    def GetEqui(self):
        return self.__Equipo.GetNom()
    def GetJugador(self):
        return self.__DNIJugador
    def GetFechF(self):
        return self.__FechFin
    def GetImp(self):
        return int(self.__PagoMen)
    def GetFechI(self):
        return self.__FechIni
