import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from modelo.Producto import Producto

class PanelRegistrarProducto(tk.Frame):
    def __init__(self, parent, productos):
        super().__init__(parent)
        self.productos = productos  
        
        title_label = tk.Label(self, text="Registrar Nuevo Producto", font=("Arial", 16))
        title_label.pack(pady=10)
        self.configure(bg="#d6c9b1") 

        tk.Label(self, text="Nombre del producto:").pack(anchor="w", padx=10)
        self.cajaNombre = tk.Entry(self)
        self.cajaNombre.pack(fill="x", padx=10, pady=5)

        tk.Label(self, text="Descripción del producto:").pack(anchor="w", padx=10)
        self.cajaDescripcion = tk.Entry(self)
        self.cajaDescripcion.pack(fill="x", padx=10, pady=5)

        tk.Label(self, text="Precio del producto:").pack(anchor="w", padx=10)
        self.cajaPrecio = tk.Entry(self)
        self.cajaPrecio.pack(fill="x", padx=10, pady=5)

        tk.Label(self, text="Fecha de entrega:").pack(anchor="w", padx=10)
        self.cajaFechaEntrega = tk.Entry(self)
        self.cajaFechaEntrega.pack(fill="x", padx=10, pady=5)

        self.imagen_path = None  
        self.btnSeleccionarImagen = tk.Button(self, text="Seleccionar Imagen", command=self.seleccionar_imagen)
        self.btnSeleccionarImagen.pack(pady=10)

        self.lblImagen = tk.Label(self, text="No se ha seleccionado imagen")
        self.lblImagen.pack(pady=5)

        btn_registrar = tk.Button(self, text="Registrar Producto", command=self.registrar_producto)
        btn_registrar.pack(pady=20)

        btn_cancelar = tk.Button(self, text="Cancelar", command=self.cancelar)
        btn_cancelar.pack(pady=5)

    def seleccionar_imagen(self):
        """
        Abre un cuadro de diálogo para seleccionar una imagen.
        """
        self.imagen_path = filedialog.askopenfilename(filetypes=[("Archivos de imagen", "*.jpg;*.jpeg;*.png;*.gif")])
        if self.imagen_path:
            self.lblImagen.config(text=f"Imagen seleccionada: {self.imagen_path}")
        else:
            self.lblImagen.config(text="No se ha seleccionado imagen")

    def registrar_producto(self):
        """
        Registra un nuevo producto con los datos ingresados.
        """
        nombre = self.cajaNombre.get()
        descripcion = self.cajaDescripcion.get()
        fechatentativa=self.cajaFechaEntrega.get()
        
        try:
            precio = float(self.cajaPrecio.get())
        except ValueError:
            messagebox.showwarning("Error en el precio", "El precio debe ser un número válido.")
            return

      

        if not nombre or not descripcion or not self.imagen_path:
            messagebox.showwarning("Campos vacíos", "Todos los campos son obligatorios.")
            return

        nuevo_producto = Producto(id_producto=len(self.productos) + 1, 
                                  nombre=nombre, 
                                  descripcion=descripcion, 
                                  precio=precio, 
                                  fechatentativa=fechatentativa, 
                                  imagen_path=self.imagen_path)
        self.productos.append(nuevo_producto)
        
        messagebox.showinfo("Producto registrado", f"Producto {nombre} registrado exitosamente.")

        self.cajaNombre.delete(0, tk.END)
        self.cajaDescripcion.delete(0, tk.END)
        self.cajaPrecio.delete(0, tk.END)
        self.cajaFechaEntrega.delete(0, tk.END)
        self.lblImagen.config(text="No se ha seleccionado imagen")

    def cancelar(self):
        """
        Cancela el registro y limpia los campos.
        """
        self.cajaNombre.delete(0, tk.END)
        self.cajaDescripcion.delete(0, tk.END)
        self.cajaPrecio.delete(0, tk.END)
        self.cajaFechaEntrega.delete(0, tk.END)
        self.lblImagen.config(text="No se ha seleccionado imagen")
        from principal.panelProductos import PanelProductos
        self.master.show_panel(PanelProductos) 
