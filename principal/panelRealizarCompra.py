import tkinter as tk
from tkinter import messagebox
from modelo.Compra import Compra
#from principal.panelProductos import producto_seleccionado, usuario_actual
class PanelRealizarCompra(tk.Frame):
    def __init__(self, parent,producto, usuario,compras):
        super().__init__(parent)
        self.compras=compras
        self.producto = producto  # Asignar directamente el producto
        self.usuario = usuario  # Asignar directamente el usuario
       
        self.configure(bg="#d6c9b1")

        tk.Label(self, text="Confirmar Compra", font=("Arial", 16), bg="#d6c9b1").pack(pady=10)

        tk.Label(self, text=f"Producto: {producto.nombre}", bg="#d6c9b1").pack(pady=5)
        self.precio_label =tk.Label(self, text=f"Precio: ${producto.precio:.2f}", bg="#d6c9b1")
        self.precio_label.pack(pady=5)
        tk.Label(self, text=f"Saldo: ${usuario.balance:.2f}", bg="#d6c9b1").pack(pady=5)

          # Spinner para seleccionar la cantidad
        self.cantidad_var = tk.IntVar(value=1)  # Valor inicial
        tk.Label(self, text="Cantidad:", bg="#d6c9b1").pack(pady=5)
        self.spinbox_cantidad = tk.Spinbox(self, from_=1, to=100, textvariable=self.cantidad_var, width=5)
        self.spinbox_cantidad.pack(pady=5)

         # Caja de texto para la dirección
        self.nuevaDireccion=tk.Label(self, text="Dirección de Envío:", bg="#d6c9b1").pack(pady=5)
        self.entry_direccion = tk.Entry(self, width=40)
        self.entry_direccion.pack(pady=5)


        tk.Button(self, text="Confirmar Compra", command=self.realizar_compra).pack(pady=10)
        tk.Button(self, text="Cancelar", command=self.cancelar_compra).pack(pady=5)
        self.cantidad_var.trace("w", self.actualizar_precio)

    def actualizar_precio(self, *args):
        """Método para actualizar el precio según la cantidad seleccionada."""
        cantidad = self.cantidad_var.get()
        precio_total = self.producto.precio * cantidad
        self.precio_label.config(text=f"Precio: ${precio_total:.2f}")
    

    def realizar_compra(self):
        cantidad = self.cantidad_var.get()
        direccion = self.entry_direccion.get()
        
        if not direccion:
            messagebox.showerror("Dirección faltante", "Por favor ingrese una dirección de envío.")
            return

        self.usuario.set_direc(direccion)  # Establecer la dirección de envío del usuario
        total_precio = self.producto.precio * cantidad

        if self.usuario.balance < total_precio:
            messagebox.showerror("Saldo insuficiente", "No tienes suficiente saldo para realizar esta compra.")
            return

        # Restar el monto de la compra al saldo del usuario
        self.usuario.balance -= total_precio

        # Crear una nueva compra y agregarla a la lista de compras
        nueva_compra = Compra(self.usuario, self.producto, direccion, cantidad)
        self.compras.append(nueva_compra)  # Almacenar la compra en la lista de compras

        # Confirmar la compra y mostrar el mensaje
        messagebox.showinfo("Compra Exitosa", f"Has comprado {cantidad} unidades de {self.producto.nombre} por ${total_precio:.2f}.\nTu nuevo saldo es ${self.usuario.balance:.2f}")

        # Regresar al panel de productos
        from principal.panelProductos import PanelProductos
        self.master.show_panel(PanelProductos,self.usuario)

    def cancelar_compra(self):
        """
        Lógica para cancelar la compra y volver al panel anterior.
        """
        from principal.panelProductos import PanelProductos
        self.master.show_panel(PanelProductos,self.usuario)
