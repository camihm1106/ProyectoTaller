import tkinter as tk
import pickle
from tkinter import simpledialog
from tkinter import ttk

print ("\033c", end="")

root = tk.Tk()
root.geometry("800x600")

def agen():
    # elimina todos los widgets de la interfaz
    for widget in root.winfo_children():
         widget.destroy()
    # llama a la función que crea nuevos widgets
    agenda_completa()

def exi():
    # elimina todos los widgets de la interfaz
    for widget in root.winfo_children():
         widget.destroy()
    # llama a la función que crea nuevos widgets
    archivo_e()

inicio = tk.Label(root, text="Bienvenido al TextToSpeech para Sesiones de Órganos Colegiados")
inicio.place(x=20, y=5)
inicio.config(font=("Courier", 15), bg="gray")

nuevo_button = tk.Button(root, text="Proyecto Nuevo", command=agen)
nuevo_button.place(x=100,y=180)
nuevo_button.config(font=("Courier", 15), bg="gray")
existente_button = tk.Button(root, text="Proyecto Existente", command=exi)
existente_button.place(x=400,y=180)
existente_button.config(font=("Courier", 15), bg="gray")


def agenda_completa():
    # Variables para almacenar la agenda
    agenda = {}
    apartados = set()

    # Función para agregar un apartado y sus puntos a la agenda
    def agregar_apartado():
        apartado = apartado_entry.get()
        puntos = puntos_entry.get("1.0", "end-1c").split("\n")
        if apartado not in apartados:
            apartados.add(apartado)
            agenda[apartado] = puntos
            apartado_entry.delete(0, "end")
            puntos_entry.delete("1.0", "end")
        
    # Función para mostrar la tabla con toda la agenda
    def mostrar_agenda():
        global tabla
        # elimina todos los widgets de la interfaz
        tabla = ttk.Treeview(root, columns=("apartado", "puntos"), show="headings")
        tabla.heading("#1", text="Apartado", anchor=tk.CENTER)
        tabla.heading("#2", text="Puntos", anchor=tk.CENTER)
        for apartado, puntos in agenda.items():
            tabla.insert("", "end", values=(apartado, ", ".join(puntos)))
        tabla.place(x=180, y=220)

    def eliminar_apartado(tabla, agenda, apartados):
        seleccion = tabla.focus()
        if seleccion:
            apartado = tabla.item(seleccion, "values")[0]
            del agenda[apartado]
            apartados.remove(apartado)
            tabla.delete(seleccion)

    def modificar_apartado(tabla, agenda, apartados):
        seleccion = tabla.focus()
        if seleccion:
            apartado = tabla.item(seleccion, "values")[0]
            puntos = agenda[apartado]
            respuesta = simpledialog.askstring("Modificar apartado", f"Modificar el apartado {apartado}:", parent=root)
            if respuesta:
                agenda[respuesta] = puntos
                apartados.add(respuesta)
                del agenda[apartado]
                apartados.remove(apartado)
                apartado_entry.delete(0, "end")
                apartado_entry.insert(0, respuesta)
                respuesta = simpledialog.askstring("Modificar puntos", f"Modificar los puntos del apartado {puntos}:", parent=root)
                if respuesta:
                    puntos = respuesta.split(", ")
                    puntos_entry.delete("1.0", "end")
                    puntos_entry.insert("1.0", ", ".join(puntos))
                    tabla.item(seleccion, values=(respuesta, ", ".join(puntos)))
    
    def limpiar_pantalla():
        # elimina todos los widgets de la interfaz
        for widget in root.winfo_children():
            widget.destroy()
        # llama a la función que crea nuevos widgets
        todo_parti()

    # Interfaz para agregar la agenda
    apartado_label = tk.Label(root, text="Apartado:")
    apartado_entry = tk.Entry(root)
    puntos_label = tk.Label(root, text="Puntos:")
    puntos_entry = tk.Text(root, height=5)
    agregar_button = tk.Button(root, text="Agregar agenda", command=agregar_apartado)
    agregar_button.place(x=100,y=180)
    finalizar_button = tk.Button(root, text="Finalizar", command=mostrar_agenda)
    finalizar_button.place(x=250,y=180)
    eliminar_button = tk.Button(root, text="Eliminar", command=lambda: eliminar_apartado(tabla, agenda, apartados))
    eliminar_button.place(x=380,y=180)
    modificar_button = tk.Button(root, text="Modificar", command=lambda: modificar_apartado(tabla, agenda, apartados))
    modificar_button.place(x=490,y=180)
    # crea el botón "Limpiar"
    boton_limpiar = tk.Button(root, text="Participantes", command=limpiar_pantalla)
    boton_limpiar.place(x=600,y=180)


    apartado_label.pack()
    apartado_entry.pack()
    puntos_label.pack()
    puntos_entry.pack()

def todo_parti():
    tabla_participantes = ttk.Treeview(root, columns=("Nombre",))
    tabla_participantes.heading("#0", text="Índice")
    tabla_participantes.heading("Nombre", text="Nombre")
    tabla_participantes.pack(padx=10, pady=10)

    def actualizar_tabla_participantes(conjunto_participantes):
        # Limpiar tabla
        tabla_participantes.delete(*tabla_participantes.get_children())

        # Agregar participantes a la tabla
        for indice, participante in enumerate(conjunto_participantes, start=1):
            tabla_participantes.insert("", "end", text=indice, values=(participante,))

    def participantes():
        """Función que pregunta los nombres de los participantes."""
        lista_nombres = []
        nombre = simpledialog.askstring("Nombres de participantes", "Digite el nombre completo del participante:")
        while nombre:
            lista_nombres.append(nombre)
            nombre = simpledialog.askstring("Nombres de participantes", "Digite el nombre completo del participante (o presione Cancelar para terminar):")

        conjunto_participantes = set(lista_nombres)
        actualizar_tabla_participantes(conjunto_participantes)

    def modificar_participante():
        seleccionado = tabla_participantes.selection()
        if seleccionado:
            nombre_actual = tabla_participantes.item(seleccionado, "values")[0]
            nuevo_nombre = simpledialog.askstring("Modificar participante", f"Nombre actual: {nombre_actual}", initialvalue=nombre_actual)
            if nuevo_nombre and nuevo_nombre != nombre_actual:
                tabla_participantes.set(seleccionado, "Nombre", nuevo_nombre)   
                
    def eliminar_participante():
        seleccionado = tabla_participantes.selection()
        if seleccionado:
            tabla_participantes.delete(seleccionado)

    # Botón para agregar participantes
    boton_agregar = tk.Button(root, text="Agregar participantes", command=participantes)
    boton_agregar.pack(padx=10, pady=10)

    # Botones para modificar y eliminar participantes
    boton_modificar = tk.Button(root, text="Modificar participante", command=modificar_participante)
    boton_modificar.pack(padx=10, pady=10)

    boton_eliminar = tk.Button(root, text="Eliminar participante", command=eliminar_participante)
    boton_eliminar.pack(padx=10, pady=10)

def archivo_e():
    global archivo_e
    with open('datos.pkl', 'rb') as archivo:
        grabaciones_reconocidas = pickle.load(archivo)

root.mainloop()
