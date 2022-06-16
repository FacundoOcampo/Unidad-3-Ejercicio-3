class Jugador:
    __Nombre=None
    __Dni=None
    __CiudadNatal=None
    __PaisOrigen=None
    __FechNac=None
    def __init__(self,Nombre,DNI,Ciudad,Pais,Fech):
        self.__Nombre=Nombre
        self.__Dni=DNI
        self.__CiudadNatal=Ciudad
        self.__PaisOrigen=Pais
        self.__FechNac=Fech
    def __str__(self):
        return "{:15} {:9} {:10} {:10} {:0}".format(self.__Nombre,self.__Dni,self.__CiudadNatal,self.__PaisOrigen,self.__FechNac)
    def GetNom(self):
        return self.__Nombre
    def GetDNI(self):
        return self.__Dni
