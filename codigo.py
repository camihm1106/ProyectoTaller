import speech_recognition as sr

print ("\033c", end="")

print("Bienvenido al TextToSpeech para Sesiones de Órganos Colegiados")
print("Iniciaremos creando la agenda previa")

#esta funcion nos da todos los apartados en una lista

def agenda():
    """Esta funcion pregunta por los apartados y puntos a tratar de los apartados para almacenarlos en diferentes listas

    Returns:
        list: lista_agenda: retorna los apartados y puntos a tratar juntos
              lista_apartados: retorna solo los apartados
              lista_punto: retorna solo los puntos a tratar sin ningun apartado
    """
    apartado=str(input("Agregue un apartado: "))
    lista_agenda=[]
    lista_apartados=[]
    lista_puntos=[]
    lista_punto=[]
    cont=1 #contador para apartados
    contn=1 #contador para puntos a tratar
    apartado_2=("{}. {}".format(cont,apartado))
    lista_agenda.append(apartado_2)
    lista_apartados.append(apartado)
    ###########################################
    punto=str(input("Agregue un punto a tratar del apartado: "))
    lista_punto.append([])
    lista_punto[-1].append(punto)
    punto_2=("{}.{}. {}".format(cont,contn,punto))
    lista_puntos.append([])
    lista_puntos[-1].append(punto_2)
    puntos2=str(input("¿Desea apregar otro punto a tratar? responda 'si' o 'no': "))
    while puntos2=="si":
            punton=str(input("Agregue un punto a tratar del apartado: "))
            lista_punto[-1].append(punton)
            contn+=1
            punto_n=("{}.{}. {}".format(cont,contn,punton))
            lista_puntos[-1].append(punto_n)
            puntos2=str(input("¿Desea apregar otro punto a tratar? responda 'si' o 'no': "))
    lista_puntos='\n'.join(map(str,lista_puntos[-1]))
    lista_agenda.append(lista_puntos)
    contn=1
    apartado2=str(input("¿Desea apregar otro apartado? responda 'si' o 'no': "))
    while apartado2=="si": #Creamos un ciclo por si desean agregar mas apartados
        apartadon=str(input("Agregue el apartado: "))
        cont+=1
        apartado_2=("{}. {}".format(cont,apartadon))
        lista_agenda.append(apartado_2)
        lista_apartados.append(apartadon)
        ########################
        lista_puntos=[]
        contn=1
        punto=str(input("Digite un punto a tratar del apartado: "))
        lista_punto.append([])
        lista_punto[-1].append(punto)
        punto_2=("{}.{}. {}".format(cont,contn,punto))
        lista_puntos.append([])
        lista_puntos[-1].append(punto_2)
        puntos2=str(input("¿Desea apregar otro punto a tratar? responda 'si' o 'no': "))
        while puntos2=="si":
            punton=str(input("Agregue un punto a tratar del apartado: "))
            lista_punto[-1].append(punton)
            contn+=1
            punto_n=("{}.{}. {}".format(cont,contn,punton))
            lista_puntos[-1].append(punto_n)
            puntos2=str(input("¿Desea apregar otro punto a tratar? responda 'si' o 'no': "))
        lista_puntos='\n'.join(map(str,lista_puntos[-1]))
        lista_agenda.append(lista_puntos)
        #################################
        apartado2=str(input("¿Desea apregar otro apartado? responda 'si' o 'no': "))
    lista_agenda=('\n'.join(map(str,lista_agenda)))
    return (lista_agenda, lista_apartados, lista_punto)

lista_agenda2, lista_apartados2, lista_puntos2=agenda()
print ("\n Agenda: ")
print (lista_agenda2)

def Participantes():
    """funcion que pregunta los nombres de los participantes
    """
    lista_nombres=[]
    nombre=str(input("Digite el nombre completo del participante: "))
    cont=1
    lista_nombres.append(nombre)
    nombre=str(input("Digite el nombre completo del participante (o 'no' para terminar): "))
    while nombre!="no":
        cont+=1
        lista_nombres.append(nombre)
        nombre=str(input("Digite el nombre completo del participante (o 'no' para terminar): "))
    return(lista_nombres)

#variable que llama a la funcion
lista_participantes=Participantes()

print("Lista de los participantes:")
print('\n'.join(map(str,lista_participantes)))

print("Seguimos con el Registro de los participantes")

def reconocedor_voz():
    """Esta funcion se encarga de relacionar el texto del reconocedor de voz con el apartado, puntos a tratar, participante 
    y la hora en que se habla

    Returns:
        list: retorna todo lo dicho con el apartado, puntos a tratar y participante a lo largo de la sesion
    """
    apartado=lista_apartados2
    puntos=lista_puntos2
    participante=lista_participantes
    reconocimiento_voz=[]
    preg_iniciadora=str(input("¿Desea empezar la reunion? Responder 'si' o 'no': "))
    while preg_iniciadora=='si':
        print ("Lista de apartados: ")
        for i, item in enumerate(apartado, start=0): #Añadimos numeros a cada apartado para ser escogido por el num
            print(f"{i}. {item}")
        preg_apart=int(input("Agregue el numero del apartado que desea hablar: "))
        seleccion_apartado = apartado[preg_apart]
        reconocimiento_voz.append([])
        reconocimiento_voz[-1].append(seleccion_apartado)
        print("puntos de "+ seleccion_apartado + ": "   )
        for i, item in enumerate(puntos[preg_apart], start=0): #Añadimos numeros a cada punto para ser escogido por el num
            print(f"{i}. {item}")
        preg_punto=int(input("Agregue el numero del punto que desea hablar: "))
        seleccion_punto = puntos[preg_apart][preg_punto]
        reconocimiento_voz[-1].append(seleccion_punto)
        print("participantes: ")
        for i, item in enumerate(participante, start=0): #Añadimos numeros a cada participante para ser escogido por el num
            print(f"{i}. {item}")
        preg_participante=int(input("Agregue el numero del participante que desee hablar: "))
        seleccion_participante = participante[preg_participante]
        reconocimiento_voz[-1].append(seleccion_participante)
        import datetime
        now = datetime.datetime.now()
        horaActual = now.strftime("%H:%M:%S")
        reconocimiento_voz[-1].append(horaActual)
        import speech_recognition as sr
        r = sr.Recognizer()
        cont=0
        l=[]
        with sr.Microphone() as source:
            while cont<10:
                print ("Intervención:\n")
                print("Di algo...")
                audio = r.listen(source)
                cont=cont+1
                try:
                    print("inicia el reconocimiento...\n")
                    text = r.recognize_google(audio, language='es-ES')
                    print("Has dicho: " + text)
                    l.append(text)
                    if text=="salir":
                        break
                except sr.UnknownValueError:
                    print("No se pudo reconocer el audio.")
                except sr.RequestError as e:
                    print("No se pudo obtener respuesta desde el servicio de Google Speech Recognition: {0}".format(e))
        reconocimiento_voz[-1].append(l)
        preg_iniciadora=str(input("¿Desea seguir la reunion? Responder 'si' o 'no': "))
        while preg_iniciadora=="si":
            reconocimiento_voz.append([])
            apartn=str(input("Desea hablar del mismo tema (responda 'si' o 'no'): "))
            if apartn=="si":
                reconocimiento_voz[-1].append(seleccion_apartado)
                reconocimiento_voz[-1].append(seleccion_punto)
            else:
                print ("Lista de apartados: ")
                for i, item in enumerate(apartado, start=0): #Añadimos numeros a cada apartado para ser escogido por el num
                    print(f"{i}. {item}")
                preg_apart=int(input("Agregue el numero del apartado que desea hablar: "))
                seleccion_apartado = apartado[preg_apart]
                reconocimiento_voz[-1].append(seleccion_apartado)
                print("puntos de "+ seleccion_apartado + ": ")
                for i, item in enumerate(puntos[preg_apart], start=0): #Añadimos numeros a cada punto para ser escogido por el num
                    print(f"{i}. {item}")
                preg_punto=int(input("Agregue el numero del punto que desea hablar: "))
                seleccion_punto = puntos[preg_apart][preg_punto]
                reconocimiento_voz[-1].append(seleccion_punto)
            preg_participanten=str(input("El mismo participante va a seguir hablando (Responda 'si' o 'no'): "))
            if preg_participanten=="si":
                reconocimiento_voz[-1].append(seleccion_participante)
            else:
                print("participantes: ")
                for i, item in enumerate(participante, start=0): #Añadimos numeros a cada participante para ser escogido por el num
                    print(f"{i}. {item}")
                preg_participante=int(input("Agregue el numero del participante que desee hablar: "))
                seleccion_participante = participante[preg_participante]
                reconocimiento_voz[-1].append(seleccion_participante)
            import datetime
            now = datetime.datetime.now()
            horaActual = now.strftime("%H:%M:%S")
            reconocimiento_voz[-1].append(horaActual)
            import speech_recognition as sr
            r = sr.Recognizer()
            cont=0
            l=[]
            with sr.Microphone() as source:
                while cont<10:
                    print ("Intervención:\n")
                    print("Di algo...")
                    audio = r.listen(source)
                    cont=cont+1
                    try:
                        print("inicia el reconocimiento...\n")
                        text = r.recognize_google(audio, language='es-ES')
                        print("Has dicho: " + text)
                        l.append(text)
                        if text=="salir":
                            break
                    except sr.UnknownValueError:
                        print("No se pudo reconocer el audio.")
                    except sr.RequestError as e:
                        print("No se pudo obtener respuesta desde el servicio de Google Speech Recognition: {0}".format(e))
            reconocimiento_voz[-1].append(l)
            preg_iniciadora=str(input("¿Desea seguir la reunion? Responder 'si' o 'no': "))
        return (reconocimiento_voz)
l_reportes=reconocedor_voz()

def imprimir_conversaciones(conversaciones):
    """Se encarga de imprimir las conversaciones con su apartado, punto a tratar, participante, hora inicio y el
      texto que el reconocimiento de voz imprimio

    Args:
        conversaciones (list): lista ordenada de apartado, punto a tratar, participante, hora inicio y el texto reconocido
    """
    for conversacion in conversaciones:
        categoria, subcategoria, usuario, timestamp, mensajes = conversacion
        print(f"{categoria}:")
        print(f"{subcategoria}:")
        print(f"{usuario}: {timestamp} {', '.join(mensajes)}")


def contar_palabras_por_usuario(listaConInformación):
    """Esta funcion imprime la cantidad de palabras total que dijo un participante a lo largo de la reunion

    Args:
        listaConInformaci (list): lista ordenada de apartado, punto a tratar, participante, hora inicio y el texto reconocido
         del reconocimiento de voz
    """
    print("Se imprime de orden desendente las personas que más palabras dijeron\n")
    palabras_por_usuario = {}
    for mensaje in listaConInformación:
        usuario = mensaje[2]
        palabras = mensaje[4]
        if usuario not in palabras_por_usuario:
            palabras_por_usuario[usuario] = 0
        palabras_por_usuario[usuario] += sum([len(palabra.split()) for palabra in palabras])
    palabras_por_usuario_ordenado = sorted(palabras_por_usuario.items(), key=lambda x: x[1], reverse=True)
    for usuario, cantidad_palabras in palabras_por_usuario_ordenado:
        print(f"{usuario}: {cantidad_palabras} palabras")

def contar_intervenciones_por_punto_apartado(listaConInformación):
    """Funcion que imprime la cantidad de veces que participo una persona en cada punto a tratar del apartado

    Args:
        listaConInformaci (list): lista ordenada de apartado, punto a tratar, participante, hora inicio y el texto reconocido
         del reconocimiento de voz
    """
    intervenciones_por_punto_apartado = {}
    for mensaje in listaConInformación:
        punto = mensaje[0]
        apartado = mensaje[1]
        usuario = mensaje[2]
        if punto not in intervenciones_por_punto_apartado:
            intervenciones_por_punto_apartado[punto] = {}
        if apartado not in intervenciones_por_punto_apartado[punto]:
            intervenciones_por_punto_apartado[punto][apartado] = {}
        if usuario not in intervenciones_por_punto_apartado[punto][apartado]:
            intervenciones_por_punto_apartado[punto][apartado][usuario] = 0
        intervenciones_por_punto_apartado[punto][apartado][usuario] += 1
    for punto, apartados in intervenciones_por_punto_apartado.items():
        print(punto + ":")
        for apartado, usuarios in apartados.items():
            print("\n"+ apartado + ":\n")
            for usuario, cantidad_intervenciones in usuarios.items():
                print(f"{usuario}: {cantidad_intervenciones} intervenciones")

def reportes():
    """Funcion que pregunta que reporte desea imprimir
    """
    print("1: Reporte 1 \n 2: Reporte 2 \n 3: Reporte 3")
    
    indice=int(input("\nIngrese el índice correspondiente al reporte que desea realizar: "))
    if indice==1:
        print("\n Se realizará el reporte 1\n")
        imprimir_conversaciones(l_reportes)
    elif indice==2:
            print("\n Se realizará el reporte 2\n")
            contar_palabras_por_usuario(l_reportes)
    elif indice==3:
            print("\n Se realizará el reporte 3\n")
            contar_intervenciones_por_punto_apartado(l_reportes)


def continuar_reportes():
    """funcion que pregunta si desea imprimir algun otro reporte 
    """
    seguir_reportes=1
    while seguir_reportes==1:
        respuesta = input('¿Desea seguir imprimiendo reportes? (o no si no lo desea): ')
        if respuesta == "si":
            print("\n")
            reportes()                       
        else:
            seguir_reportes+=1
            break

reportes()
continuar_reportes()
print("\n Ha finalizado el programa")