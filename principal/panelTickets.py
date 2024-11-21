import os
import tkinter as tk
from tkinter import scrolledtext
#lo mismo que en los otros paneles,etiqutas,prpoeidades y mas
#que pararmetros recbe ,pues el usuario,vayana Main y en la funcion show_panel() en el elif panleTickets noten que 
#le pamos el usario_logueado, y esta clase recibe ese usaurio,asi funcionan todos los paneles.
#recibe el usuario y unadireccion, una carpeta pues
class PanelTickets(tk.Frame):
    def __init__(self, master, usuario, ticket_dir="tickets"):
        super().__init__(master)
        self.usuario = usuario 
        self.label_tickets = tk.Label(self, text=f"Tickets de {self.usuario.nombre}") #mostramos con esta etquta el usuario que esta logueado
        self.label_tickets.pack()

        # Texto para mostrar los tickets,uso de un textarea, osea se un area gigante de texto con las propiedades width,height,largo y ancho
        #wrap=tk.WORD ajusta el texto a nuestro text area,en caso de que sea demasiado grnade la line de texto
        self.text_area = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=80, height=20)
        self.text_area.pack(padx=10, pady=10, expand=True, fill="both")

        # Botón para cerrar la ventana
        tk.Button(self, text="Cerrar", command=self.cancelar).pack(pady=10)

        # Mostrar tickets
        self.mostrar_tickets(usuario, ticket_dir)

    def cancelar(self):
        from principal.panelProductos import PanelProductos
        self.master.show_panel(PanelProductos,self.usuario)   

    def mostrar_tickets(self, usuario, ticket_dir):
        #si no existe lo crea, otra validacion a tomar en cuenta cuando se trabaja con archivos,siempre se valida si exsita y si no lo cree
        if not os.path.exists(ticket_dir):
            self.text_area.insert(tk.END, "No hay tickets disponibles.\n")
            return

        # Filtrar archivos del usuario buscando el nombre dentro del contenido del archivo
        user_tickets = [
            f for f in os.listdir(ticket_dir) 
            if self.usuario.nombre in open(os.path.join(ticket_dir, f), 'r', encoding='utf-8').read()
        ]
        
        if not user_tickets:
            self.text_area.insert(tk.END, f"No se encontraron tickets para {usuario.nombre}.\n")
            return

        # Mostrar contenido de los tickets
        for ticket_file in user_tickets:
            ticket_path = os.path.join(ticket_dir, ticket_file)
            with open(ticket_path, "r", encoding="utf-8") as file:
                self.text_area.insert(tk.END, f"--- {ticket_file} ---\n")
                self.text_area.insert(tk.END, file.read())
                self.text_area.insert(tk.END, "\n\n")
