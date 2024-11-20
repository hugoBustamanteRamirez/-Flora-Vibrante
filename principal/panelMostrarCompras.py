import tkinter as tk
from tkinter import PhotoImage
from modelo.Compra import Compra
from PIL import Image, ImageTk 
class PanelMostrarCompras(tk.Frame):
    def __init__(self, parent, compras, usuario):
        super().__init__(parent)
        self.compras = compras
        self.usuario = usuario
        self.configure(bg="#f4f4f9")

        title_label = tk.Label(self, text="Compras Realizadas", font=("Arial", 16, "bold"), bg="#d6c9b1", padx=20, pady=10)
        title_label.pack(pady=10)

          # Contenedor con Canvas y Scrollbar
        container = tk.Frame(self)
        container.pack(expand=True, fill="both", padx=10, pady=10)

        canvas = tk.Canvas(container, bg="#d6c9b1")
        canvas.pack(side="top", fill="both", expand=True)

        scrollbar_horizontal = tk.Scrollbar(container, orient="horizontal", command=canvas.xview)
        scrollbar_horizontal.pack(side="bottom", fill="x")  # Coloca el scroll en la parte inferior

        # Frame interno dentro del Canvas
        self.compras_frame = tk.Frame(canvas, bg="#d6c9b1")
        self.compras_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Vincular el Canvas al Frame
        canvas.create_window((0, 0), window=self.compras_frame, anchor="nw")
        canvas.configure(xscrollcommand=scrollbar_horizontal.set)  # Conexión al scroll horizontal



        columnas = ["Imagen", "Usuario", "Producto", "Cantidad", "Precio Total", "Estado Envío", "Dirección Envío"]
        for col_num, columna in enumerate(columnas):
            label = tk.Label(self.compras_frame, text=columna, font=("Arial", 12, "bold"), bg="#d6c9b1", anchor="w", width=20)
            label.grid(row=0, column=col_num, padx=5, pady=10, sticky="w")

        self.mostrar_compras()

    def mostrar_compras(self):
        for widget in self.compras_frame.winfo_children():
            if widget.grid_info().get("row") > 0:
                widget.destroy()

        if self.usuario.rol == 1:
            compras_a_mostrar = self.compras
        else:
            compras_a_mostrar = [compra for compra in self.compras if compra.usuario == self.usuario]

        for row_num, compra in enumerate(compras_a_mostrar, start=1):
            usuario_nombre = compra.get_usuario().nombre
            producto_nombre = compra.get_producto().nombre
            cantidad = compra.get_cant()
            precio_total = compra.get_producto().precio * cantidad
            estado_envio = compra.get_edoEnvio()
            imagen_path = compra.get_producto().imagen_path
            direccion_envio = compra.get_nuevaDireccion()

            if imagen_path:
                try:
                    img = Image.open(imagen_path)  # Cargar la imagen con Pillow
                    img = img.resize((100, 100),  Image.Resampling.LANCZOS)  # Redimensionar la imagen si es necesario
                    img_tk = ImageTk.PhotoImage(img)  # Convertirla a un objeto compatible con Tkinter
                    imagen_label = tk.Label(self.compras_frame, image=img_tk, bg="#d6c9b1")
                    imagen_label.image = img_tk  # Guardar referencia para evitar garbage collection
                    imagen_label.grid(row=row_num, column=0, padx=10, pady=5)
                except Exception as e:
                    print(f"Error cargando imagen: {e}")
                    tk.Label(self.compras_frame, text="Imagen no disponible", bg="#d6c9b1", width=15, height=4).grid(row=row_num, column=0, padx=10, pady=5)
            else:
                tk.Label(self.compras_frame, text="Sin imagen", bg="#d6c9b1", width=15, height=4).grid(row=row_num, column=0, padx=10, pady=5)
            tk.Label(self.compras_frame, text=usuario_nombre, font=("Arial", 12), bg="#d6c9b1", anchor="w").grid(row=row_num, column=1, padx=10, pady=5, sticky="w")
            tk.Label(self.compras_frame, text=producto_nombre, font=("Arial", 12), bg="#d6c9b1", anchor="w").grid(row=row_num, column=2, padx=10, pady=5, sticky="w")
            tk.Label(self.compras_frame, text=cantidad, font=("Arial", 12), bg="#d6c9b1").grid(row=row_num, column=3, padx=10, pady=5)
            tk.Label(self.compras_frame, text=f"${precio_total:.2f}", font=("Arial", 12), bg="#d6c9b1").grid(row=row_num, column=4, padx=10, pady=5)
            tk.Label(self.compras_frame, text=estado_envio, font=("Arial", 12), bg="#d6c9b1").grid(row=row_num, column=5, padx=10, pady=5)
            tk.Label(self.compras_frame, text=direccion_envio, font=("Arial", 12), bg="#d6c9b1").grid(row=row_num, column=6, padx=10, pady=5)
