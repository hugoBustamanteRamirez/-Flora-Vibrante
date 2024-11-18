import tkinter as tk
from tkinter import messagebox, ttk
from modelo.Producto import Producto

class PanelModificarProducto(tk.Frame):
    def __init__(self, parent, productos):
        super().__init__(parent)
        self.productos = productos  # Lista de productos que se modificarán
        self.selected_product = None  # Producto seleccionado para modificar
        self.configure(bg="#d6c9b1") 


        # Título del panel
        title_label = tk.Label(self, text="Modificar Producto", font=("Arial", 16))
        title_label.pack(pady=10)

        # ComboBox para seleccionar el producto a modificar
        self.producto_var = tk.StringVar()
        self.combo_producto = ttk.Combobox(self, textvariable=self.producto_var, width=40)
        self.combo_producto['values'] = [producto.nombre for producto in self.productos]
        self.combo_producto.pack(pady=10)
        
        # Botón para cargar los datos del producto seleccionado
        btn_cargar = tk.Button(self, text="Cargar Producto", command=self.cargar_producto)
        btn_cargar.pack(pady=5)

        # Campo de nombre
        tk.Label(self, text="Nombre:").pack(anchor="w", padx=10)
        self.cajaNombre = tk.Entry(self)
        self.cajaNombre.pack(fill="x", padx=10, pady=5)

        # Campo de precio
        tk.Label(self, text="Precio:").pack(anchor="w", padx=10)
        self.cajaPrecio = tk.Entry(self)
        self.cajaPrecio.pack(fill="x", padx=10, pady=5)

        # Campo de fechatentativa
        tk.Label(self, text="Fecha tentativa de entrega:").pack(anchor="w", padx=10)
        self.cajaCantidad = tk.Entry(self)
        self.cajaCantidad.pack(fill="x", padx=10, pady=5)

        # Botón de guardar cambios
        btn_guardar = tk.Button(self, text="Guardar Cambios", command=self.guardar_cambios)
        btn_guardar.pack(pady=20)

        # Botón para cancelar y volver
        btn_cancelar = tk.Button(self, text="Cancelar", command=self.cancelar)
        btn_cancelar.pack(pady=5)

    def cargar_producto(self):
        """
        Carga los detalles del producto seleccionado para que pueda ser modificado.
        """
        selected_name = self.producto_var.get()

        # Buscar el producto en la lista
        for producto in self.productos:
            if producto.nombre == selected_name:
                self.selected_product = producto
                # Cargar los valores del producto en los campos
                self.cajaNombre.delete(0, tk.END)
                self.cajaNombre.insert(0, producto.nombre)

                self.cajaPrecio.delete(0, tk.END)
                self.cajaPrecio.insert(0, str(producto.precio))

                self.cajaCantidad.delete(0, tk.END)
                self.cajaCantidad.insert(0, str(producto.fechatentativa))
                break

    def guardar_cambios(self):
        """
        Guarda los cambios realizados en el producto seleccionado.
        """
        if self.selected_product:
            # Obtener los nuevos valores del formulario
            nuevo_nombre = self.cajaNombre.get()
            nuevo_precio = self.cajaPrecio.get()
            nueva_fechatentativa = self.cajaCantidad.get()

            # Validar datos
            if not nuevo_nombre or not nuevo_precio or not nueva_fechatentativa:
                messagebox.showwarning("Campos vacíos", "Todos los campos son obligatorios.")
                return

            # Actualizar el producto
            self.selected_product.nombre = nuevo_nombre
            self.selected_product.precio = float(nuevo_precio)
            self.selected_product.fechatentativa = nueva_fechatentativa

            messagebox.showinfo("Producto modificado", f"Producto {nuevo_nombre} modificado exitosamente.")
            
            # Limpiar campos
            self.cajaNombre.delete(0, tk.END)
            self.cajaPrecio.delete(0, tk.END)
            self.cajaCantidad.delete(0, tk.END)

            # Actualizar ComboBox
            self.combo_producto['values'] = [producto.nombre for producto in self.productos]

        else:
            messagebox.showwarning("Error", "No se ha seleccionado un producto.")

    def cancelar(self):
        """
        Cancela la modificación y vuelve al panel anterior.
        """
        from principal.panelProductos import PanelProductos
        self.master.show_panel(PanelProductos, self.productos)  # Vuelve al panel de productos
