import tkinter as tk
from tkinter import Canvas, Scrollbar
from PIL import Image, ImageTk

class PanelProductos(tk.Frame):
    def __init__(self, parent, productos):
        super().__init__(parent)
        self.productos = productos
        self.configure(bg="#d6c9b1")

        # Configuración del canvas y scrollbar
        self.canvas = Canvas(self, bg="#d6c9b1")
        self.scrollable_frame = tk.Frame(self.canvas, bg="#d6c9b1")
        
        self.scrollbar = Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Título del panel
        title_label = tk.Label(self.scrollable_frame, text="Lista de Productos", font=("Arial", 16), bg="#d6c9b1")
        title_label.pack(pady=10)

        # Marco para los productos
        self.productos_frame = tk.Frame(self.scrollable_frame, bg="#d6c9b1")
        self.productos_frame.pack(expand=True, fill="both")

        # Mostrar los productos
        self.mostrar_productos()

    def mostrar_productos(self):
        """
        Muestra los productos como cajas estilo web y los centra dinámicamente.
        """
        for widget in self.productos_frame.winfo_children():
            widget.destroy()

        columnas = 3  # Número de columnas
        espacio_columna = 20  # Espacio entre columnas
        max_width = self.winfo_toplevel().winfo_width()  # Ancho de la ventana principal
        tarjeta_width = 200  # Ancho estimado de cada tarjeta
        total_width = columnas * (tarjeta_width + espacio_columna)  # Ancho ocupado por las tarjetas y espacios

        # Calcular el padding para centrar las tarjetas
        padding_left = max((max_width - total_width) // 2, 10)

        self.productos_frame.grid_columnconfigure(0, minsize=padding_left)  # Espaciado a la izquierda
        for col in range(1, columnas + 1):
            self.productos_frame.grid_columnconfigure(col, weight=1, minsize=tarjeta_width)

        for index, producto in enumerate(self.productos):
            row = index // columnas + 1
            col = index % columnas + 1

            # Crear una "caja" para el producto
            caja = tk.Frame(self.productos_frame, bg="#ffffff", borderwidth=2, relief="ridge", padx=10, pady=10)
            caja.grid(row=row, column=col, padx=10, pady=10)
              # Agregar eventos para el efecto hover
            caja.bind("<Enter>", lambda e, widget=caja: self.hover_entrar(widget))
            caja.bind("<Leave>", lambda e, widget=caja: self.hover_salir(widget))

            # Cargar la imagen del producto
            if producto.imagen_path:
                try:
                    img = Image.open(producto.imagen_path)
                    img = img.resize((120, 120))
                    img = ImageTk.PhotoImage(img)

                    imagen_label = tk.Label(caja, image=img, bg="#ffffff")
                    imagen_label.image = img  # Evitar que Python elimine la imagen
                    imagen_label.pack(pady=5)
                except Exception:
                    tk.Label(caja, text="Error al cargar imagen", bg="#ffffff", font=("Arial", 10)).pack(pady=5)
            else:
                tk.Label(caja, text="Sin imagen", bg="#ffffff", font=("Arial", 10)).pack(pady=5)

            # Información del producto
            tk.Label(caja, text=producto.nombre, font=("Arial", 12, "bold"), bg="#ffffff").pack(pady=5)
            tk.Label(caja, text=f"Precio: ${producto.precio:.2f}", font=("Arial", 10), bg="#ffffff").pack()
            tk.Label(caja, text=f"Stock: {producto.fechatentativa}", font=("Arial", 10), bg="#ffffff").pack()
            tk.Label(caja, text=producto.descripcion, font=("Arial", 10), bg="#ffffff", wraplength=150).pack(pady=5)
            # Botón "Comprar"
            comprar_btn = tk.Button(
                caja, 
                text="Comprar", 
                font=("Arial", 10, "bold"), 
                bg="#4CAF50", 
                fg="white", 
                command=lambda p=producto: self.comprar_producto(p)
            )
            comprar_btn.pack(pady=10)
            comprar_btn.bind("<Enter>", lambda e, btn=comprar_btn: btn.configure(bg="#e08167"))
            comprar_btn.bind("<Leave>", lambda e, btn=comprar_btn: btn.configure(bg="#4CAF50"))


    def hover_entrar(self, widget):
         widget.configure(bg="#f5e6c9", borderwidth=4)  # Cambia el color de fondo y el grosor del borde

    def hover_salir(self, widget):
        
        widget.configure(bg="#ffffff", borderwidth=2)
    def comprar_producto(self, producto):
        """
        Acción al hacer clic en el botón "Comprar".
        """
        # Aquí puedes implementar la lógica para agregar el producto al carrito o realizar una compra
        print(f"Producto comprado: {producto.nombre}")
        tk.messagebox.showinfo("Compra exitosa", f"Has comprado {producto.nombre} por ${producto.precio:.2f}")    

