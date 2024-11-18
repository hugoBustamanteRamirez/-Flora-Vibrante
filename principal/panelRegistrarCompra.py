import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from modelo.Producto import Producto
from modelo.Compra import Compra

class PanelRegistrarCmpra(tk.Frame):

    def __init__(self, parent, productos, usuario):
        super().__init__(parent)
        self.productos = productos  
        self.usuario = usuario  
        self.selected_product = None  
        self.compras_realizadas = []
        self.configure(bg="#d6c9b1") 


        title_label = tk.Label(self, text="Productos Disponibles", font=("Arial", 16))
        title_label.pack(pady=10)

        self.product_listbox = tk.Listbox(self, height=10, width=50)
        self.product_listbox.pack(padx=10, pady=10)

        for producto in self.productos:
            self.product_listbox.insert(tk.END, f"{producto.nombre} - ${producto.precio} - Fecha de entrega: {producto.fechatentativa}")

        btn_seleccionar = tk.Button(self, text="Seleccionar Producto", command=self.seleccionar_producto)
        btn_seleccionar.pack(pady=5)

        btn_comprar = tk.Button(self, text="Comprar", command=self.comprar_producto)
        btn_comprar.pack(pady=5)



        btn_cancelar = tk.Button(self, text="Cancelar", command=self.cancelar)
        btn_cancelar.pack(pady=5)

    def seleccionar_producto(self):
        """
        Selecciona un producto de la lista para la compra.
        """
        try:
            selected_index = self.product_listbox.curselection()[0]
            self.selected_product = self.productos[selected_index]

            messagebox.showinfo("Producto Seleccionado", f"Has seleccionado {self.selected_product.nombre}.")
        except IndexError:
            messagebox.showwarning("Selección inválida", "Por favor, selecciona un producto de la lista.")

    def comprar_producto(self):
        """
        Realiza la compra del producto seleccionado.
        """
        if self.selected_product:
                
                self.selected_product.fechatentativa -= 1
                messagebox.showinfo("Compra Exitosa", f"Has comprado {self.selected_product.nombre}.")
                compra = Compra(self.usuario, self.selected_product,"En progeso") 
                self.compras_realizadas.append(compra)
                self.master.compras.append(compra) 

                
                print(f"Compra realizada por {self.usuario.nombre}. Producto: {self.selected_product.nombre}")
        else:
            messagebox.showwarning("Selección inválida", "Por favor, selecciona un producto primero.")

    def cancelar(self):
        """
        Cancela la compra y vuelve al panel anterior.
        """
        from principal.panelProductos import PanelProductos
        self.master.show_panel(PanelProductos, self.productos, self.usuario)