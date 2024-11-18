import tkinter as tk
from tkinter import PhotoImage
from modelo.Compra import Compra
class PanelMostrarCompras(tk.Frame):
    def __init__(self, parent, compras, usuario):
        super().__init__(parent)
        self.compras = compras
        self.usuario = usuario
        self.configure(bg="#f4f4f9")

        # Título del panel
        title_label = tk.Label(self, text="Compras Realizadas", font=("Arial", 16, "bold"), bg="#d6c9b1", padx=20, pady=10)
        title_label.pack(pady=10)

        # Mostrar solo las compras según el rol del usuario
        if self.usuario.rol == 1:  # Si es admin, mostrar todas las compras
            compras_a_mostrar = self.compras
        else:  # Si es usuario normal, mostrar solo sus compras
            compras_a_mostrar = [compra for compra in self.compras if compra.usuario == self.usuario]

        # Mostrar las compras filtradas
        if compras_a_mostrar:
            for compra in compras_a_mostrar:
                tk.Label(self, text=f"Producto: {compra.producto.nombre}, Cantidad: {compra.cant}, Precio: ${compra.producto.precio * compra.cant:.2f}, Dirección: {compra.usuario.direccion}", bg="#d6c9b1").pack(pady=5)
        else:
            tk.Label(self, text="No tienes compras.", bg="#d6c9b1").pack(pady=5)    

        # Contenedor para las compras
        self.compras_frame = tk.Frame(self, bg="#d6c9b1")
        self.compras_frame.pack(expand=True, fill="both", padx=10, pady=10)

        # Crear encabezados de las columnas
        columnas = ["Imagen", "Usuario", "Producto", "Cantidad", "Precio Total", "Estado Envío", "Dirección Envío"]
        for col_num, columna in enumerate(columnas):
            label = tk.Label(self.compras_frame, text=columna, font=("Arial", 12, "bold"), bg="#d6c9b1", anchor="w", width=20)
            label.grid(row=0, column=col_num, padx=5, pady=10, sticky="w")

        # Mostrar las compras
        self.mostrar_compras()

    def mostrar_compras(self):
        """
        Muestra todas las compras en formato de filas y columnas con más detalles.
        """
        # Limpiar las filas previas
        for widget in self.compras_frame.winfo_children():
            if widget.grid_info().get("row") > 0:
                widget.destroy()

        # Mostrar cada compra
        for row_num, compra in enumerate(self.compras, start=1):
            usuario_nombre = compra.get_usuario().nombre
            producto_nombre = compra.get_producto().nombre
            cantidad = compra.get_cant()
            precio_total = compra.get_producto().precio * cantidad
            estado_envio = compra.get_edoEnvio()
            imagen_path = compra.get_producto().imagen_path
            direccion_envio = compra.get_usuario().direccion  # Aquí obtenemos la nueva dirección

            # Agregar la imagen del producto
            if imagen_path:
                try:
                    img = PhotoImage(file=imagen_path)  # Usar una imagen en formato compatible con Tkinter
                    imagen_label = tk.Label(self.compras_frame, image=img, bg="#d6c9b1")
                    imagen_label.image = img  # Necesario para que no se pierda la referencia
                    imagen_label.grid(row=row_num, column=0, padx=10, pady=5)
                except Exception:
                    imagen_label = tk.Label(self.compras_frame, text="Imagen no disponible", bg="#d6c9b1", width=15, height=4)
                    imagen_label.grid(row=row_num, column=0, padx=10, pady=5)
            else:
                imagen_label = tk.Label(self.compras_frame, text="Sin imagen", bg="#d6c9b1", width=15, height=4)
                imagen_label.grid(row=row_num, column=0, padx=10, pady=5)

            # Mostrar los datos de la compra
            tk.Label(self.compras_frame, text=usuario_nombre, font=("Arial", 12), bg="#d6c9b1", anchor="w").grid(row=row_num, column=1, padx=10, pady=5, sticky="w")
            tk.Label(self.compras_frame, text=producto_nombre, font=("Arial", 12), bg="#d6c9b1", anchor="w").grid(row=row_num, column=2, padx=10, pady=5, sticky="w")
            tk.Label(self.compras_frame, text=cantidad, font=("Arial", 12), bg="#d6c9b1").grid(row=row_num, column=3, padx=10, pady=5)
            tk.Label(self.compras_frame, text=f"${precio_total:.2f}", font=("Arial", 12), bg="#d6c9b1").grid(row=row_num, column=4, padx=10, pady=5)
            tk.Label(self.compras_frame, text=estado_envio, font=("Arial", 12), bg="#d6c9b1").grid(row=row_num, column=5, padx=10, pady=5)
            tk.Label(self.compras_frame, text=direccion_envio, font=("Arial", 12), bg="#d6c9b1").grid(row=row_num, column=6, padx=10, pady=5)  # Mostrar la dirección
