import tkinter as tk
from tkinter import messagebox
from modelo.Producto import Producto

class PanelEliminarProducto(tk.Frame):
    def __init__(self, parent, productos):
        super().__init__(parent)
        self.productos = productos  
        self.parent = parent  
        self.configure(bg="#d6c9b1") 


       
        title_label = tk.Label(self, text="Eliminar Producto", font=("Arial", 16))
        title_label.pack(pady=10)

        
        self.lista_productos_frame = tk.Frame(self)
        self.lista_productos_frame.pack(expand=True, fill="both")

        
        self.lista_productos = tk.Listbox(self.lista_productos_frame, height=10, width=50, font=("Arial", 12))
        self.lista_productos.pack(padx=10, pady=10)

        
        self.mostrar_productos()

       
        btn_eliminar_producto = tk.Button(self, text="Eliminar Producto", command=self.eliminar_producto)
        btn_eliminar_producto.pack(pady=20)

        
        btn_cancelar = tk.Button(self, text="Volver", command=self.cancelar)
        btn_cancelar.pack(pady=10)

    def mostrar_productos(self):
        """
        Muestra los productos en el Listbox.
        """
        
        self.lista_productos.delete(0, tk.END)

        
        for producto in self.productos:
            self.lista_productos.insert(tk.END, f"{producto.nombre} - ${producto.precio:.2f}")

    def eliminar_producto(self):
        """
        Elimina el producto seleccionado del Listbox.
        """
        try:
          
            seleccion = self.lista_productos.curselection()

            if not seleccion:
                messagebox.showwarning("Selección inválida", "Debe seleccionar un producto para eliminar.")
                return

            
            producto_seleccionado = self.lista_productos.get(seleccion[0])

            
            nombre_producto = producto_seleccionado.split(" - ")[0]  # Extraemos solo el nombre
            producto_a_eliminar = None

            for producto in self.productos:
                if producto.nombre == nombre_producto:
                    producto_a_eliminar = producto
                    break

            
            if producto_a_eliminar:
                self.productos.remove(producto_a_eliminar)
                messagebox.showinfo("Producto Eliminado", f"Producto {producto_a_eliminar.nombre} eliminado exitosamente.")
                self.mostrar_productos()  
            else:
                messagebox.showerror("Error", "No se pudo encontrar el producto seleccionado.")
        
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")

    def cancelar(self):
        """
        Vuelve al panel anterior (en este caso, al panel de productos).
        """
        from principal.panelProductos import PanelProductos
        self.master.show_panel(PanelProductos, self.productos)
