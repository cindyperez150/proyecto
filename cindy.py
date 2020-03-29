class REGISTRO():

  def __init__(self,nombre, apellido, pais, genero, edad, dia, mes, año):
    self.nombre = ""
    self.apellido = ""
    self.pais=0
    self.genero= ""
    self.edad=0
      self.dia=0
      self.mes=0
      self.año=0
fallecidos_china = 0
descartados_china = 0
confirmados_usa = 0
recuperados_usa = 0
fallecidos_usa = 0
descartados_usa = 0
confirmados_españa = 0
recuperados_españa = 0
fallecidos_españa = 0
descartados_españa = 0
confirmados_italia = 0
recuperados_italia = 0
fallecidos_italia = 0
descartados_italia = 0
confirmados_chile = 0
recuperados_chile = 0
fallecidos_chile = 0
descartados_chile = 0
confirmados_vnzla = 0
recuperados_vnzla = 0
fallecidos_vnzla = 0
descartados_vnzla = 0
confirmados_colombia = 0
recuperados_colombia = 0
fallecidos_colombia = 0
descartados_colombia = 0
confirmados_mexico = 0
recuperados_mexico = 0
fallecidos_mexico = 0
descartados_mexico = 0
confirmados_brasil = 0
recuperados_brasil = 0
fallecidos_brasil = 0
descartados_brasil = 0
confirmados_peru = 0
recuperados_peru = 0
fallecidos_peru = 0
descartados_peru = 0

fiebre = ""
toseca = ""
difRespirar = ""
congestion = ""
dolorgarg = ""
diarrea = ""
dolorCab = ""
malestar = ""
covid_19 = ""
edadMaxmuertos = 0
edadMinmuertos = 100
nombminmuerto = ""
nombmaxmuerto = ""
apellidominmuerto = ""
apellidomaxmuerto = ""
nombmax_descartado = ""
nombmin_descartado = ""
apellidomax_descartado = ""
apellidomin_descartado = ""
edadMindescartado = 100
edadMaxdescartado = 0
nomb_maxcovid = ""
nomb_mincovid = ""
apellido_mincovid = ""
apellido_maxcovid = ""
edadMin_covid = 100
edadMax_covid = 0
Paciente = 0
muertos = 0
recuperados = 0
confirmados = 0
descartados = 0
descartado = 0
opcion = 0
opcion3 = 0
dato = REGISTRO()
while (opcion != 3):
    print("\t\t===> MENU PRINCIPAL <===\n\n")
    print("\t\t\t-1. Registrar.")
    print("\t\t\t-2. Reportes.")
    print("\t\t\t-3. SALIR.")
    opcion3 = 0
    Paciente = 0
    fiebre = ""
    toseca = ""
    difRespirar = ""
    congestion = ""
    dolorgarg = ""
    diarrea = ""
    dolorCab = ""
    malestar = ""
    covid_19 = ""
    opcion = int(input("\t\t SELECCIONE LA OPCION DE SU PREFERENCIA: "))

    if (opcion == 1):
        dato.nombre = input("\nINGRESE SU NOMBRE: ")
        dato.apellido = input("\nINGRESE SU APELLIDO: ")
        print("\nINGRESE SU FECHA DE NACIMIENTO: \n")
        dato.dia = input("DIA: ")
        dato.mes = input("MES: ")
        dato.año = input("AÑO: ")

        print("\n1-Italia.\n2-Chile.\n3-Colombia.\n4-Mexico.\n5-Peru.")
        dato.pais = input("\nDONDE RESIDE?: ")
        dato.edad = int(input("\nINGRESE SU EDAD: "))
        dato.sexo = input("\nINGRESE SU GENERO F/M: ")
        print("\nPAR DESCARTAR Y DETECTAR EL COVID19 RESPONDA LAS SIGUIENTES PREGUNTAS: \n")
        fiebre = input("PRESENTA FIEBRE? S/N: \n")
        toseca = input("PRESENTA TOS SECA? S/N: \n")
        difRespirar = input("PRESENTA DIFICULTAD PARA RESPIRAR? S/N: \n")
        congestion = input("PRESENTA CONGESTION NASAL? S/N: \n")
        dolorgarg = input("PRESENTA DOLOR DE GARGANTA? S/N: \n")
        diarrea = input("PRESENTA DIARREA? S/N: \n")
        dolorCab = input("PRESENTA DOLOR DE CABEZA? S/N: \n")
        malestar = input("PRESENTA MALESTAR GENERAL? S/N: \n")

        if (fiebre == "s" or fiebre == "S"):
            if (toseca == "s" or toseca == "S"):
                if (difRespirar == "s" or difRespirar == "S"):
                    if (congestion == "s" or congestion == "S"):
                        if (dolorgarg == "s" or dolorgarg == "S"):
                            if (diarrea == "s" or diarrea == "S"):
                                if (dolorCab == "s" or dolorCab == "S"):
                                    if (malestar == "s" or malestar == "S"):
                                        print("\n -POSITIVO PARA COVID-19-\n")
                                        covid_19 = "s"
        if (fiebre == "n" or fiebre == "N"):
            if (toseca == "n" or toseca == "N"):
                if (difRespirar == "n" or difRespirar == "N"):
                    if (congestion == "n" or congestion == "N"):
                        if (dolorgarg == "n" or dolorgarg == "N"):
                            if (diarrea == "n" or diarrea == "N"):
                                if (dolorCab == "n" or dolorCab == "N"):
                                    if (malestar == "n" or malestar == "N"):
                                        print(
                                            "\n-USTED NO POSEE COVID19, SUS SINTOMAS SON DE UN GRIPE COMUN O ALERGIA-\n")
                                        Paciente = input("\nPACIENTE \n1. VIVO \n2. MUERTO\n")
                                    else:
                                        print("\n-POSITIVO PARA COVID-19-\n")
                                        covid_19 = "s"
                                        Paciente = input("\nPACIENTE \n1. VIVO \n2. MUERTO\n")
                                else:
                                    if (malestar == "s" or malestar == "S"):
                                        print("\n-POSITIVO PARA COVID-19-\n")
                                        covid_19 = "s"
                                        Paciente = input("\nPACIENTE \n1.VIVO \n2. MUERTO\n")
                                    else:
                                        print("\n-POSITIVO PARA COVID-19-\n")
                                        covid_19 = "s"
                                        Paciente = input("\nPACIENTE \n1. VIVO \n2. MUERTO\n")
                            else:
                                if (dolorCab == "s" or dolorCab == "S"):
                                    if (malestar == "s" or malestar == "S"):
                                        print("\n-POSITIVO PARA GRIPE-\n")
                                        descartado = "s"
                                    else:
                                        print("\n-POSITIVO PARA GRIPE-\n")
                                        descartado = "s"
                                else:
                                    if (malestar == "s" or malestar == "S"):
                                        print("\n-POSITIVO PARA GRIPE-\n")
                                        descartado = "s"
                                    else:
                                        print("\n-POSITIVO PARA COVID-19-\n")
                                        covid_19 = "s"
                                        Paciente = input("\nPACIENTE \n1. VIVO \n2. MUERTO\n")
                        else:
                            if (diarrea == "s" or diarrea == "S"):
                                if (dolorCab == "s" or dolorCab == "S"):
                                    if (malestar == "s" or malestar == "S"):
                                        print("\n-POSITIVO PARA COVID-19-\n")
                                        covid_19 = "s"
                                        Paciente = input("\nPACIENTE \n1. VIVO \n2. MUERTO\n")
                                    else:
                                        print("\n-POSITIVO PARA COVID-19-\n")
                                        covid_19 = "s"
                                        Paciente = input("\nPACIENTE \n1. VIVO \n2. MUERTO\n")
                                else:
                                    if (malestar == "s" or malestar == "S"):
                                        print("\n-POSITIVO PARA COVID-19-\n")
                                        covid_19 = "s"
                                        Paciente = input("\nPACIENTE \n1. VIVO \n2. MUERTO\n")
                                    else:
                                        print("\n-POSITIVO PARA COVID-19-\n")
                                        covid_19 = "s"
                                        Paciente = input("\nPACIENTE \n1. VIVO \n2. MUERTO\n")
                            else:
                                if (dolorCab == "s" or dolorCab == "S"):
                                    if (malestar == "s" or malestar == "S"):
                                        print("\n-POSITIVO PARA GRIPE-\n")
                                        descartado = "s"
                                    else:
                                        print("\n-POSITIVO PARA GRIPE-\n")
                                        descartado = "s"
                                else:
                                    if (malestar == "s" or malestar == "S"):
                                        print("\n-POSITIVO PARA GRIPE-\n")
                                        descartado = "s"
                                    else:
                                        print("\n-POSITIVO PARA COVID-19-\n")
                                        covid_19 = "s"
                                        Paciente = input("\nPACIENTE \n1. VIVO \n2. MUERTO\n")
                    else:
                        if (dolorgarg == "s" or dolorgarg == "S"):
                            if (diarrea == "s" or diarrea == "S"):
                                if (dolorCab == "s" or dolorCab == "S"):
                                    if (malestar == "s" or malestar == "S"):
                                        print("\n-POSITIVO PARA COVID-19-\n")
                                        covid_19 = "s"
                                        Paciente = input("\nPACIENTE \n1. VIVO \n2. MUERTO\n")

                                    else:
                                        print("\n-POSITIVO PARA COVID-19-\n")
                                        covid_19 = "s"
                                        Paciente = input("\nPACIENTE \n1. VIVO \n2. MUERTO\n")
                                else:
                                    if (malestar == "s" or malestar == "S"):
                                        print("\n-POSITIVO PARA COVID-19-\n")
                                        covid_19 = "s"
                                        Paciente = input("\nPACIENTE \n1. VIVO \n2. MUERTO\n")
                                    else:
                                        print("\n-POSITIVO PARA COVID-19-\n")
                                        covid_19 = "s"
                                        Paciente = input("\nPACIENTE \n1. VIVO \n2. MUERTO\n")
                            else:
                                if (dolorCab == "s" or dolorCab == "S"):
                                    if (malestar == "s" or malestar == "S"):
                                        print("\n-POSITIVO PARA GRIPE-\n")
                                        descartado = "s"
                                    else:
                                        print("\n-POSITIVO PARA GRIPE-\n")
                                        descartado = "s"
                                else:
                                    if (malestar == "s" or malestar == "S"):
                                        print("\n-POSITIVO PARA GRIPE-\n")
                                        descartado = "s"
                                    else:
                                        print("\n-POSITIVO PARA COVID-19-\n")
                                        covid_19 = "s"
                                        Paciente = input("\nPACIENTE \n1. VIVO \n2. MUERTO\n")
                        else:
                            if (diarrea == "s" or diarrea == "S"):
                                if (dolorCab == "s" or dolorCab == "S"):
                                    if (malestar == "s" or malestar == "S"):
                                        print("\n-POSITIVO PARA COVID-19-\n")
                                        covid_19 = "s"
                                        Paciente = input("\nPACIENTE \n1. VIVO \n2. MUERTO\n")
                                    else:
                                        print("\n-POSITIVO PARA COVID-19-\n")
                                        covid_19 = "s"
                                        Paciente = input("\nPACIENTE \n1. VIVO \n2. MUERTO\n")
                                else:
                                    if (malestar == "s" or malestar == "S"):
                                        print("\n-POSITIVO PARA COVID-19-\n")
                                        covid_19 = "s"
                                        Paciente = input("\nPACIENTE \n1. VIVO \n2. MUERTO\n")
                                    else:
                                        print("\n-POSITIVO PARA COVID-19-\n")
                                        covid_19 = "s"
                                        Paciente = input("\nPACIENTE \n1. VIVO \n2. MUERTO\n")
                            else:
                                if (dolorCab == "s" or dolorCab == "S"):
                                    if (malestar == "s" or malestar == "S"):
                                        print("\n-POSITIVO PARA GRIPE-\n")
                                        descartado = "s"
                                    else:
                                        print("\n-POSITIVO PARA GRIPE-\n")
                                        descartado = "s"
                                else:
                                    if (malestar == "s" or malestar == "S"):
                                        print("\n-POSITIVO PARA GRIPE-\n")
                                        descartado = "s"
                                    else:
                                        print("\n-POSITIVO PARA COVID-19-\n")
                                        covid_19 = "s"
                                        Paciente = input("\nPACIENTE \n1. VIVO \n2. MUERTO\n")
        if (covid_19 == "s"):
            confirmados += 1
            if (dato.genero == "f" or dato.genero == "F"):
                confirmadosFemenino += 1
            else:
                confirmadosMasculino += 1
            if (Paciente == "1"):
                recuperados += 1
                if (dato.genero == "f" or dato.genero == "F"):
                    recuperadosFemenino += 1
                else:
                    recuperadosMasculino += 1
            else:
                muertos += 1
                if (dato.genero == "f" or dato.genero == "F"):
                    muertosFemenino += 1
                else:
                    muertosMasculino += 1
        else:
            if (descartado == "s"):
                descartados += 1
                if (dato.genero == "f" or dato.genero == "F"):
                    descartadosFemenino += 1
                else:
                    descartadosMasculino += 1

        # CHINA
        if (covid_19 == "s" and dato.pais == "1"):
            confirmados_china += 1
            if (Paciente == "1"):
                recuperados_china += 1
            else:
                fallecidos_china += 1
        else:
            if (descartado == "s" and dato.pais == "1"):
                descartados_china += 1
        # USA
        if (covid_19 == "s" and dato.pais == "1"):
            confirmados_usa += 1
            if (Paciente == "1"):
                recuperados_usa += 1
            else:
                fallecidos_usa += 1
        else:
            if (descartado == "s" and dato.pais == "1"):
                descartados_usa += 1
        # ESPAÑA
        if (covid_19 == "s" and dato.pais == "1"):
            confirmados_españa += 1
            if (Paciente == "1"):
                recuperados_españa += 1
            else:
                fallecidos_españa += 1
        else:
            if (descartado == "s" and dato.pais == "1"):
                descartados_españa += 1
        # ITALIA
        if (covid_19 == "s" and dato.pais == "1"):
            confirmados_italia += 1
            if (Paciente == "1"):
                recuperados_italia += 1
            else:
                fallecidos_italia += 1
        else:
            if (descartado == "s" and dato.pais == "1"):
                descartados_italia += 1
        # CHILE
        if (covid_19 == "s" and dato.pais == "2"):
            confirmados_chile += 1
            if (Paciente == "1"):
                recuperados_chile += 1
            else:
                fallecidos_chile += 1
        else:
            if (descartado == "s" and dato.pais == "2"):
                descartados_chile += 1
        # VNZLA
        if (covid_19 == "s" and dato.pais == "1"):
            confirmados_vnzla += 1
            if (Paciente == "1"):
                recuperados_vnzla += 1
            else:
                fallecidos_vnzla += 1
        else:
            if (descartado == "s" and dato.pais == "1"):
                descartados_vnzla += 1
        # COLOMBIA
        if (covid_19 == "s" and dato.pais == "3"):
            confirmados_colombia += 1
            if (Paciente == "1"):
                recuperados_colombia += 1
            else:
                fallecidos_colombia += 1
        else:
            if (descartado == "s" and dato.pais == "3"):
                descartados_colombia += 1
        # MEXICO
        if (covid_19 == "s" and dato.pais == "4"):
            confirmados_mexico += 1
            if (Paciente == "1"):
                recuperados_mexico += 1
            else:
                fallecidos_mexico += 1
        else:
            if (descartado == "s" and dato.pais == "4"):
                descartados_mexico += 1
        # BRASIL
        if (covid_19 == "s" and dato.pais == "1"):
            confirmados_brasil += 1
            if (Paciente == "1"):
                recuperados_brasil += 1
            else:
                fallecidos_brasil += 1
        else:
            if (descartado == "s" and dato.pais == "1"):
                descartados_brasil += 1
        # PERU
        if (covid_19 == "s" and dato.pais == "5"):
            confirmados_italia += 1
            if (Paciente == "1"):
                recuperados_peru += 1
            else:
                fallecidos_peru += 1
        else:
            if (descartado == "s" and dato.pais == "5"):
                descartados_peru += 1

            if (dato.edad <= edadMin_covid):
                edadMin_covid = dato.edad
                nomb_min_covid = dato.nombre
                apellido_min_covid = dato.apellido
            if (dato.edad > edadMax_covid):
                edadMax_covid = dato.edad
                nomb_max_covid = dato.nombre
                apellido_max_covid = dato.apellido
            else:
                if (dato.edad <= edadMin_descartado):
                    edadMin_descartado = dato.edad
                    nomb_min_descartado = dato.nombre
                    apellido_min_descartado = dato.apellido
            if (dato.edad > edadMax_descartado):
                edadMax_descartado = dato.edad
                nomb_max_descartado = dato.nombre
                apellido_max_descartado = dato.apellido
        if (Paciente == "2"):
            if (dato.edad <= edadMin_fallecidos):
                edadMin_fallecidos = dato.edad
                nomb_min_fallecido = dato.nombre
                apellido_max_fallecido = dato.apellido
            if (dato.edad > edadMax_fallecidos):
                edadMax_fallecidos = dato.edad
                nomb_max_fallecido = dato.nombre
                apellido_max_fallecido = dato.apellido
    if (opcion == 2):
        while (opcion3 != 3):
            print("\n\t\t-MENU-\n")
            print("\t\t1. MOSTRAR")
            print("\t\t2. MAYOR Y MENOR REGISTRADO")
            print("\t\t3. VOLVER")
            opcion3 = int(input("\t\tSELECCIONE \n"))
            if (opcion3 == 1):
                print("\nCASOS EN TOTAL")
                print("CONTAGIADOS: ", confirmados)
                print("FEMENINO: ", confirmadosFemenino)
                print("MASCULINO: ", confirmadosMasculino)
                print("\nRECUPERADOS: ", recuperados)  # Se muestra informacion general de casos, por genero
                print("FEMENINO: ", recuperadosF)  # Y por paises
                print("MASCULINO: ", recuperadosM)
                print("==================================================\n")
                print("\nMUERTOS: ", fallecidos)
                print("FEMENINO: ", fallecidosF)
                print("MASCULINO: ", fallecidosM)
                print("==================================================\n")
                print("\nDESCARTADOS: ", descartados)
                print("FEMENINO: ", descartadosF)
                print("MASCULINO: ", descartadosM)
                print("==================================================\n")
                print("\nCASOS POR PAISES:\n")
                print("==================================================\n")

                print("\nCHINA:\n")
                print("CONTAGIADOS: ", confirmados_china)
                print("RECUPERADOS: ", recuperados_china)
                print("MUERTOS: ", fallecidos_china)
                print("DESCARTADOS: ", descartados_china)
                print("\nUSA:\n")
                print("CONTAGIADOS: ", confirmados_usa)
                print("RECUPERADOS: ", recuperados_usa)
                print("MUERTOS: ", fallecidos_usa)
                print("DESCARTADOS: ", descartados_usa)
                print("\nESPAÑA:\n")
                print("CONTAGIADOS: ", confirmados_españa)
                print("RECUPERADOS: ", recuperados_españa)
                print("MUERTOS: ", fallecidos_españa)
                print("DESCARTADOS: ", descartados_españa)
                print("\nITALIA:\n")
                print("CONTAGIADOS: ", confirmados_italia)
                print("RECUPERADOS: ", recuperados_italia)
                print("MUERTOS: ", fallecidos_italia)
                print("DESCARTADOS: ", descartados_italia)
                print("\nCHILE: \n")
                print("CONTAGIADOS: ", confirmados_chile)
                print("RECUPERADOR: ", recuperados_chile)
                print("MUERTOS: ", fallecidos_chile)
                print("DESCARTADOS: ", descartados_chile)
                print("\nVENEZUELA:\n")
                print("CONTAGIADOS: ", confirmados_vnzla)
                print("RECUPERADOS: ", recuperados_vnzla)
                print("MUERTOS: ", fallecidos_vnzla)
                print("DESCARTADOS: ", descartados_vnzla)
                print("\nCOLOMBIA: \n")
                print("INFECTADOS: ", confirmados_colombia)
                print("RECUPERADOS: ", recuperados_colombia)
                print("MUERTOS: ", fallecidos_colombia)
                print("DESCARTADOS: ", descartados_colombia)
                print("\nMEXICO: \n")
                print("CONTAGIADOS: ", confirmados_mexico)
                print("RECUPERADOS: ", recuperados_mexico)
                print("MUERTOS: ", fallecidos_mexico)
                print("DESCARTADOS: ", descartados_mexico)
                print("\nBRASIL:\n")
                print("CONTAGIADOS: ", confirmados_brasil)
                print("RECUPERADOS: ", recuperados_brasil)
                print("MUERTOS: ", fallecidos_brasil)
                print("DESCARTADOS: ", descartados_brasil)
                print("\nPERU: \n")
                print("CONTAGIADOS: ", confirmados_peru)
                print("RECUPERADOS: ", recuperados_peru)
                print("MUERTOS: ", fallecidos_peru)
                print("DESCARTADOS: ", descartados_peru)
            if (opcion3 == 2):

                print("\nCONTAGIADO DE MENOR EDAD: \n")
                print("NOMBRE: ", nomb_min_covid, apellido_min_covid)
                print("EDAD: ", edadMin_covid)
                print("\nCONTAGIADO DE MAYOR EDAD: \n")
                print("NOMBRE: ", nomb_max_covid, apellido_max_covid)
                print("EDAD: ", edadMax_covid)

                print("\nDESCARTADO DE MENOR EDAD: \n")
                print("NOMBRE: ", nomb_min_descartado, apellido_min_descartado)
                print("EDAD: ", edadMin_descartado)

                print("\nDESCARTADO DE MAYOR EDAD: \n")
                print("NOMBRE: ", nomb_max_descartado, apellido_max_descartado)
                print("EDAD: ", edadMax_descartado)

                print("\nMUERTO DE MENOR EDAD: \n")
                print("\nNOMBRE: ", nomb_min_fallecido, apellido_min_fallecido)
                print("\nEDAD: ", edadMin_fallecidos)

                print("\nMUERTO DE MAYOR EDAD: \n")
                print("\nNOMBRE: ", nomb_max_fallecido, apellido_max_fallecido)
                print("\nEDAD: ", edadMax_fallecidos)
