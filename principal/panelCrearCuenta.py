import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
from modelo.Usuario import Usuario
from principal.panelProductos import PanelProductos
class PanelCrearCuenta(tk.Frame):
    def __init__(self, parent, usuarios):
        super().__init__(parent)
        self.usuarios = usuarios 

        
        title_label = tk.Label(self, text="Registra tu cuenta", font=("Arial", 16))
        title_label.pack(pady=10)
        self.configure(bg="#d6c9b1") 

        
        tk.Label(self, text="Nombre:").pack(anchor="w", padx=10)
        self.cajaNombre = tk.Entry(self)
        self.cajaNombre.pack(fill="x", padx=10, pady=5)

        
        tk.Label(self, text="Contraseña:").pack(anchor="w", padx=10)
        self.cajaContrasena = tk.Entry(self, show="*")
        self.cajaContrasena.pack(fill="x", padx=10, pady=5)

   
        tk.Label(self, text="Dirección:").pack(anchor="w", padx=10)
        self.cajaDireccion = tk.Entry(self)
        self.cajaDireccion.pack(fill="x", padx=10, pady=5)

        # Tarjeta: Número
        tk.Label(self, text="Número de Tarjeta:").pack(anchor="w", padx=10)
        self.cajaNumeroTarjeta = tk.Entry(self)
        self.cajaNumeroTarjeta.pack(fill="x", padx=10, pady=5)

        tk.Label(self, text="Fecha de Vencimiento:").pack(anchor="w", padx=10)
        self.cajaFechaVencimiento = DateEntry(self, date_pattern="dd/MM/yyyy", width=12)
        self.cajaFechaVencimiento.pack(fill="x", padx=10, pady=5)

        # Tarjeta: CVV
        tk.Label(self, text="CVV:").pack(anchor="w", padx=10)
        self.cajaCVV = tk.Entry(self, show="*")
        self.cajaCVV.pack(fill="x", padx=10, pady=5)
   
        btn_registrar = tk.Button(self, text="Registrar", command=self.registrar_usuario)
        btn_registrar.pack(pady=20)

        btn_Continuar = tk.Button(self, text="Vaciar cajas de texto", command=self.ConContinuarRegistrandoUsuarios)
        btn_Continuar.pack(pady=21)
        
        btn_Cancelar = tk.Button(self, text="Volver", command=self.Cancelar)
        btn_Cancelar.pack(pady=22)
        

    def registrar_usuario(self):
      
        nombre = self.cajaNombre.get()
        contraseña = self.cajaContrasena.get()
        direccion = self.cajaDireccion.get()
        numero_tarjeta = self.cajaNumeroTarjeta.get()
        fecha_vencimiento_completa = self.cajaFechaVencimiento.get_date()
        fecha_vencimiento = fecha_vencimiento_completa.strftime("%m/%y")

     
        cvv = self.cajaCVV.get()

        rol = 0

      
        if not nombre or not contraseña or not direccion  or not numero_tarjeta or not fecha_vencimiento or not cvv:
            messagebox.showwarning("Campos vacíos", "Todos los campos son obligatorios.")
            return

        if len(numero_tarjeta) != 16 or not numero_tarjeta.isdigit():
            messagebox.showerror("Error de validación", "El número de tarjeta incorrecto, debe conterner al menos 16 digitos.")
            return

        if len(cvv) != 3 or not cvv.isdigit():
            messagebox.showerror("Error de validación", "Cvv incorrecto, debe tener al menos 3 digitos.")
            return
        nuevo_usuario = Usuario(nombre, contraseña, direccion,numero_tarjeta, fecha_vencimiento, cvv,500, rol=rol)
        self.usuarios.append(nuevo_usuario)
        messagebox.showinfo("Usuario registrado", f"Usuario {nombre} registrado exitosamente.")

      
        self.cajaNombre.delete(0, tk.END)
        self.cajaContrasena.delete(0, tk.END)
        self.cajaDireccion.delete(0, tk.END)
        self.cajaCVV.delete(0, tk.END)
        self.cajaNumeroTarjeta.delete(0, tk.END)
        
        from principal.panelLogin import PanelLogin
        self.master.show_panel(PanelLogin)  
        
    def ConContinuarRegistrandoUsuarios(self):


        
        self.cajaNombre.delete(0, tk.END)
        self.cajaContrasena.delete(0, tk.END)
        self.cajaDireccion.delete(0, tk.END)
        self.rol_var.set(0)
    
    def Cancelar(self) :
        
        from principal.panelLogin import PanelLogin
        self.master.show_panel(PanelLogin)  
        