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
        tk.Label(self, text=f"Saldo actual: ${self.usuario_logueado.balance:.2f}", bg="#d6c9b1").pack(anchor="w", padx=10)

        tk.Label(self, text="Monto a depositar:", bg="#d6c9b1").pack(anchor="w", padx=10, pady=(10, 0))
        self.caja_deposito = tk.Entry(self)
        self.caja_deposito.pack(fill="x", padx=10, pady=5)

        btn_depositar = tk.Button(self, text="Depositar", command=self.realizar_deposito)
        btn_depositar.pack(pady=10)

        btn_volver = tk.Button(self, text="Volver", command=self.volver)
        btn_volver.pack(pady=10)

    def realizar_deposito(self):
        try:
            monto = float(self.caja_deposito.get())
            if monto <= 0:
                raise ValueError("El monto debe ser mayor a 0.")
            
            self.usuario_logueado.balance += monto
            messagebox.showinfo("Depósito exitoso", f"Se ha depositado ${monto:.2f} en su cuenta.")
            
            for widget in self.winfo_children():
                if widget.cget("text").startswith("Saldo actual:"):
                    widget.config(text=f"Saldo actual: ${self.usuario_logueado.balance:.2f}")
            
            self.caja_deposito.delete(0, tk.END)
            self.master.show_panel(PanelProductos)

        except ValueError as e:
            messagebox.showerror("Error", f"Por favor ingrese un monto válido. {e}")

    def volver(self):
        self.master.show_panel(PanelProductos)

