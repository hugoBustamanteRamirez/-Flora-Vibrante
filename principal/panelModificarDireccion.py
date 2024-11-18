import tkinter as tk
from tkinter import messagebox


class PanelModificarDireccion(tk.Frame):
    def __init__(self, parent, compras, usuario):
        super().__init__(parent)
        self.compras = compras
        self.usuario = usuario

        self.configure(bg="#f4f4f9")

        tk.Label(self, text="Modificar Dirección de Envío", font=("Arial", 16, "bold"), bg="#d6c9b1").pack(pady=10)

        if self.usuario.rol == 1:  # Admin
            self.usuario_seleccionado_var = tk.StringVar()
            tk.Label(self, text="Selecciona un usuario", bg="#d6c9b1").pack(pady=5)

            self.lista_usuarios = [compra.usuario.nombre for compra in self.compras]
            self.lista_usuarios.append(self.usuario.nombre)  # Para incluir al admin

            self.usuario_seleccionado = tk.OptionMenu(self, self.usuario_seleccionado_var, *self.lista_usuarios)
            self.usuario_seleccionado.pack(pady=5)
        else:
            self.usuario_seleccionado_var = tk.StringVar(value=self.usuario.nombre)  # Usuario solo puede ver su nombre
            tk.Label(self, text=f"Tu dirección de envío: {self.usuario.direccion}", bg="#d6c9b1").pack(pady=5)

        tk.Label(self, text="Nueva Dirección de Envío:", bg="#d6c9b1").pack(pady=5)
        self.entry_direccion = tk.Entry(self, width=40)
        self.entry_direccion.pack(pady=5)

        tk.Button(self, text="Confirmar", command=self.modificar_direccion).pack(pady=10)
        tk.Button(self, text="Cancelar", command=self.cancelar_modificacion).pack(pady=5)

    def modificar_direccion(self):
        nuevaDireccion = self.entry_direccion.get()

        if not nuevaDireccion:
            messagebox.showerror("Dirección faltante", "Por favor ingresa una dirección.")
            return

        # Si es admin, cambiar la dirección del usuario seleccionado
        if self.usuario.rol == 1:
            usuario_seleccionado = self.usuario_seleccionado_var.get()
            
            for compra in self.compras:
                if compra.usuario.nombre == usuario_seleccionado:
                    compra.usuario.set_nuevaDireccion(nuevaDireccion)
                    break
            messagebox.showinfo("Dirección modificada", f"La dirección de {usuario_seleccionado} ha sido modificada.")
        else:
            # Si no es admin, cambiar solo la dirección de ese usuario
            self.usuario.set_direc(nuevaDireccion)
            messagebox.showinfo("Dirección modificada", "Tu dirección de envío ha sido modificada.")

        from principal.panelMostrarCompras import PanelMostrarCompras
       
        self.master.show_panel(PanelMostrarCompras, self.compras, self.usuario)

    def cancelar_modificacion(self):
        """Cancelar la modificación y volver al panel anterior."""
        
        from principal.panelMostrarCompras import PanelMostrarCompras
        self.master.show_panel(PanelMostrarCompras, self.usuario)
