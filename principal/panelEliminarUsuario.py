import tkinter as tk
from tkinter import ttk, messagebox

class PanelEliminarUsuario(tk.Frame):
    def __init__(self, parent, usuarios):
        super().__init__(parent)
        self.usuarios = usuarios  # Lista de usuarios
        self.configure(bg="#d6c9b1") 


        # Crear la tabla (Treeview) para mostrar los usuarios
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

        # Llenar la tabla con los usuarios
        self.refresh_table()

        # Empaquetar la tabla
        self.tree.pack(expand=True, fill="both", padx=10, pady=10)

        # Botón de eliminar
        btn_eliminar = tk.Button(self, text="Eliminar Usuario", command=self.eliminar_usuario)
        btn_eliminar.pack(pady=20)

    def refresh_table(self):
        """Actualiza la tabla con los usuarios actuales"""
        # Limpiar la tabla antes de agregar los nuevos elementos
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insertar usuarios en la tabla
        for usuario in self.usuarios:
            rol = "Administrador" if usuario.get_rol() == 1 else "Usuario"
            self.tree.insert("", "end", values=(usuario.get_nombre(), usuario.get_contraseña(), rol, usuario.get_direc()))

    def eliminar_usuario(self):
        """Elimina el usuario seleccionado"""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Selección inválida", "Por favor selecciona un usuario para eliminar.")
            return
        
        # Obtener el nombre del usuario seleccionado
        nombre_usuario = self.tree.item(selected_item, "values")[0]

        # Buscar el usuario en la lista de usuarios y eliminarlo
        usuario_a_eliminar = None
        for usuario in self.usuarios:
            if usuario.get_nombre() == nombre_usuario:
                usuario_a_eliminar = usuario
                break

        if usuario_a_eliminar:
            self.usuarios.remove(usuario_a_eliminar)
            messagebox.showinfo("Usuario eliminado", f"El usuario {nombre_usuario} ha sido eliminado.")
            self.refresh_table()  # Actualizar la tabla
        else:
            messagebox.showerror("Error", "No se encontró el usuario para eliminar.")
