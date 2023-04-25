import speech_recognition as sr

print ("\033c", end="")

print("Bienvenido al TextToSpeech para Sesiones de Órganos Colegiados")
print("Iniciaremos creando la agenda previa")

#esta funcion nos da todos los apartados en una lista

def agenda():
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
print ("Agenda: ")
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

def reconocedor_voz():
     apartado=lista_apartados2
     puntos=lista_puntos2
     agend=lista_agenda2
     participante=lista_participantes
     reconocimiento_voz=[]
     cont=0 #contador para los puntos
     cont2=0 #contador para el reconocimiento de voz
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
        reconocimiento_voz=('\n'.join(map(str,reconocimiento_voz)))
        return (reconocimiento_voz)
l_reportes=reconocedor_voz()
print (l_reportes)