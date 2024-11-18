import tkinter as tk
from tkinter import messagebox
from modelo.Producto import Producto

class PanelMostrarProductos(tk.Frame):
    def __init__(self, parent, productos):
        super().__init__(parent)
        self.productos = productos 
        self.configure(bg="#d6c9b1") 
        

        title_label = tk.Label(self, text="Lista de Productos", font=("Arial", 16))
        title_label.pack(pady=10)

        self.productos_frame = tk.Frame(self)
        self.productos_frame.pack(expand=True, fill="both")

        btn_agregar_producto = tk.Button(self, text="Agregar Producto", command=self.agregar_producto)
        btn_agregar_producto.pack(pady=20)
        
        self.mostrar_productos()

    
    def mostrar_productos(self):
        """
        Muestra todos los productos en un formato de filas y columnas.
        """
        for widget in self.productos_frame.winfo_children():
            widget.destroy()

        columnas = ["Nombre", "Descripción", "Precio", "Stock", "Imagen"]
        for col_num, columna in enumerate(columnas):
            label = tk.Label(self.productos_frame, text=columna, font=("Arial", 12, "bold"))
            label.grid(row=0, column=col_num, padx=10, pady=5)

        for row_num, producto in enumerate(self.productos, start=1):
            tk.Label(self.productos_frame, text=producto.nombre, font=("Arial", 12)).grid(row=row_num, column=0, padx=10, pady=5)
            tk.Label(self.productos_frame, text=producto.descripcion, font=("Arial", 12)).grid(row=row_num, column=1, padx=10, pady=5)
            tk.Label(self.productos_frame, text=f"${producto.precio:.2f}", font=("Arial", 12)).grid(row=row_num, column=2, padx=10, pady=5)
            tk.Label(self.productos_frame, text=producto.stock, font=("Arial", 12)).grid(row=row_num, column=3, padx=10, pady=5)
            imagen_texto = "Sin imagen"
            if producto.imagen_path:
                imagen_texto = producto.imagen_path.split("/")[-1]  
            tk.Label(self.productos_frame, text=imagen_texto, font=("Arial", 12)).grid(row=row_num, column=4, padx=10, pady=5)

    def agregar_producto(self):
        """
        Muestra un panel para agregar un nuevo producto.
        """
        #self.master.show_panel(PanelRegistrarProducto, self.productos)
