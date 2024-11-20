import tkinter as tk
from tkinter import messagebox

from principal.panelProductos import PanelProductos
class PanelCuentaUsuario(tk.Frame):
    def __init__(self, parent, usuario_logueado):
        super().__init__(parent)
        self.usuario_logueado = usuario_logueado
        self.configure(bg="#d6c9b1") 

        tk.Label(self, text="Mi Cuenta", font=("Arial", 16), bg="#d6c9b1").pack(pady=10)

        tk.Label(self, text=f"Nombre: {self.usuario_logueado.nombre}", bg="#d6c9b1").pack(anchor="w", padx=10)
        tk.Label(self, text=f"Dirección: {self.usuario_logueado.direccion}", bg="#d6c9b1").pack(anchor="w", padx=10)
        
        tk.Label(self, text=f"Número de tarjeta: {self.usuario_logueado.numero_tarjeta}", bg="#d6c9b1").pack(anchor="w", padx=10)
        tk.Label(self, text=f"Fecha de vencimiento: {self.usuario_logueado.fecha_vencimiento}", bg="#d6c9b1").pack(anchor="w", padx=10)
        
       
        btn_volver = tk.Button(self, text="Volver", command=self.volver)
        btn_volver.pack(pady=10)

    
    def volver(self):
        self.master.show_panel(PanelProductos)

