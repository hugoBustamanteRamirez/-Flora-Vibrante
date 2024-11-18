import tkinter as tk
from tkinter import ttk

class PanelUsuarios(tk.Frame):
    def __init__(self, parent, usuarios):
        super().__init__(parent)
        self.usuarios = usuarios  
        self.configure(bg="#d6c9b1") 

        # Crear la tabla (Treeview)
        self.tree = ttk.Treeview(self, columns=("nombre", "contraseña", "rol", "direccion"), show="headings")
        
        # Definir encabezados de la tabla
        self.tree.heading("nombre", text="Nombre")
        self.tree.heading("contraseña", text="Contraseña")
        self.tree.heading("rol", text="Rol")
        self.tree.heading("direccion", text="Dirección")
        
        # Ajustar el ancho de las columnas
        self.tree.column("nombre", width=100)
        self.tree.column("contraseña", width=100)
        self.tree.column("rol", width=80)
        self.tree.column("direccion", width=150)

        # Llenar la tabla con los datos de usuarios
        for usuario in self.usuarios:
            rol = "Administrador" if usuario.get_rol() == 1 else "Usuario"
            self.tree.insert("", "end", values=(usuario.get_nombre(), usuario.get_contraseña(), rol, usuario.get_direc()))

        # Empaquetar la tabla
        self.tree.pack(expand=True, fill="both")
