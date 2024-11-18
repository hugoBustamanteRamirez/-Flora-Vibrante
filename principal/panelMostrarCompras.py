import tkinter as tk

class PanelMostrarCompras(tk.Frame):
 
    def __init__(self, parent, compras):
        super().__init__(parent)
        self.compras = compras
        
        self.configure(bg="#d6c9b1") 

        title_label = tk.Label(self, text="Compras Realizadas", font=("Arial", 16))
        title_label.pack(pady=10)

        self.compras_frame = tk.Frame(self)
        self.compras_frame.pack(expand=True, fill="both")

        columnas = ["Usuario", "Producto", "Estado Envío"]
        for col_num, columna in enumerate(columnas):
            label = tk.Label(self.compras_frame, text=columna, font=("Arial", 12, "bold"))
            label.grid(row=0, column=col_num, padx=10, pady=5)

        self.mostrar_compras()

    def mostrar_compras(self):
        """
        Muestra todas las compras en formato de filas y columnas.
        """
        for widget in self.compras_frame.winfo_children():
            if widget.grid_info().get("row") > 0:  
                widget.destroy()

        for row_num, compra in enumerate(self.compras, start=1):
            usuario_nombre = compra.get_usuario().nombre
            producto_nombre = compra.get_producto().nombre
            compra.set_edoEnvio("En progreso")

            tk.Label(self.compras_frame, text=usuario_nombre, font=("Arial", 12)).grid(row=row_num, column=0, padx=10, pady=5)
            tk.Label(self.compras_frame, text=producto_nombre, font=("Arial", 12)).grid(row=row_num, column=1, padx=10, pady=5)
            tk.Label(self.compras_frame, text=compra.get_edoEnvio(), font=("Arial", 12)).grid(row=row_num, column=2, padx=10, pady=5)
