from ManejadorJugador import ManJugador
from ManejadorEquipo import ManEquipo
from ClaseContrato import Contrato
from ManejadorContrato import ManContrato
if __name__ == '__main__':
    #____iniciacion____#
    NManJ=ManJugador()
    NManJ.CargaArchivo()
    #NManJ.Mostrar()
    NManE=ManEquipo()
    NManE.CargaArchivo()
    #NManE.Mostrar()
    NManC=ManContrato()
    #Crear un contrato para un jugador en un equipo
    i=1
    print("--Creacion de Contratos--")
    while i != 0:
        Nom=input("     Ingrese el nombre de un jugador:")
        Equi=input("     Ingrese el nombre de un equipo:")
        FechI=input("     Ingrese la fecha de inicio(formato dd/mm/aaaa):")
        FechF=input("     Ingrese la fecha de fin(formato dd/mm/aaaa):")
        Pago=float(input("     Ingrese el pago mensual:"))
        #Busqueda de equipos y jugadores
        AuxEqui=NManE.BuscarEquipo(Equi)
        while AuxEqui == -1:
            Equi=input("     Equipo no encontrado ingrese otro nombre:")
            AuxEqui=NManE.BuscarEquipo(Equi)
        AuxJug=NManJ.BuscarJugador(Nom)
        while AuxJug == -1:
            Nom=input("     Jugador no encontrado ingrese otro nombre:")
            AuxJug=NManJ.BuscarJugador(Nom)
        #Fin de la busqueda
        Contrato=AuxEqui.AgregarContrato(AuxJug,FechI,FechF,Pago)
        NManC.CrearContrato(Contrato)
        i=int(input("Para dejar de crear contratos seleccione 0\n"))
    #NManC.Mostrar()

    print("---Busqueda de jugadores contratados---")
    while i == 0:
        DNI=input("     Ingrese el DNI del jugador a buscar:")
        if NManC.Buscar(DNI) == False:
            print("     El DNI no coincide con ningun jugador con contrato")
        i=int(input("Para finalizar ingrese 1\n"))

    print("---Consultar Contratos---")
    while i == 1:
        Nom=input("     Ingrese el nombre de un equipo:")
        NManC.Listar(Nom)
        i=int(input("Ingrese 0 para finalizar\n"))

    print("---Determinar Importe de los contratos---")
    while i ==0:
        Nom=input("     Ingrese el nombre de un equipo:")
        NManC.CalImp(Nom)
        i=int(input("Para finalizar ingrese 1\n"))
    NManC.GuardarContrato()
