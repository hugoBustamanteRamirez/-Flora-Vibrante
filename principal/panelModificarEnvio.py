import tkinter as tk
from tkinter import messagebox, ttk,simpledialog
from modelo.Compra import Compra 

class PanelModificarEstadoEnvio(tk.Frame):
    def __init__(self, parent, compras, usuario):
        super().__init__(parent)
        self.compras = compras
        self.usuario = usuario

        self.configure(bg="#f4f4f9")

        title_label = tk.Label(self, text="Modificar Estado de Envío", font=("Arial", 16, "bold"), bg="#d6c9b1", padx=20, pady=10)
        title_label.pack(pady=10)
        
        # Contenedor con Canvas y Scrollbar
        container = tk.Frame(self)
        container.pack(expand=True, fill="both", padx=10, pady=10)

        # Crear el Canvas y el Scrollbar
        self.canvas = tk.Canvas(container, bg="#d6c9b1")
        self.canvas.pack(side="top", fill="both", expand=True)

        scrollbar_horizontal = tk.Scrollbar(container, orient="horizontal", command=self.canvas.xview)
        scrollbar_horizontal.pack(side="bottom", fill="x")  # Coloca el scroll en la parte inferior

        # Frame interno dentro del Canvas
        self.compras_frame = tk.Frame(self.canvas, bg="#d6c9b1")
        self.compras_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # Vincular el Canvas al Frame
        self.canvas.create_window((0, 0), window=self.compras_frame, anchor="nw")
        self.canvas.configure(xscrollcommand=scrollbar_horizontal.set)  # Conexión al scroll horizontal

        columnas = ["Usuario", "Producto", "Cantidad", "Precio Total", "Estado Envío", "Modificar Estado"]
        for col_num, columna in enumerate(columnas):
            label = tk.Label(self.compras_frame, text=columna, font=("Arial", 12, "bold"), bg="#d6c9b1", anchor="w", width=20)
            label.grid(row=0, column=col_num, padx=5, pady=10, sticky="w")


        self.mostrar_compras()

    def mostrar_compras(self):
        """
        Muestra todas las compras en formato de filas y columnas con más detalles.
        """
        for widget in self.compras_frame.winfo_children():
            if widget.grid_info().get("row") > 0:
                widget.destroy()

        if self.usuario.rol == 1:  # Si es admin, mostrar todas las compras
            compras_a_mostrar = self.compras
        else:  # Si es usuario normal, mostrar solo sus compras
            compras_a_mostrar = [compra for compra in self.compras if compra.usuario == self.usuario]

        # Mostrar las compras
        for row_num, compra in enumerate(compras_a_mostrar, start=1):
            usuario_nombre = compra.get_usuario().nombre
            producto_nombre = compra.get_producto().nombre
            cantidad = compra.get_cant()
            precio_total = compra.get_producto().precio * cantidad
            estado_envio = compra.get_edoEnvio()

            # Mostrar los datos de la compra
            tk.Label(self.compras_frame, text=usuario_nombre, font=("Arial", 12), bg="#d6c9b1", anchor="w").grid(row=row_num, column=0, padx=10, pady=5, sticky="w")
            tk.Label(self.compras_frame, text=producto_nombre, font=("Arial", 12), bg="#d6c9b1", anchor="w").grid(row=row_num, column=1, padx=10, pady=5, sticky="w")
            tk.Label(self.compras_frame, text=cantidad, font=("Arial", 12), bg="#d6c9b1").grid(row=row_num, column=2, padx=10, pady=5)
            tk.Label(self.compras_frame, text=f"${precio_total:.2f}", font=("Arial", 12), bg="#d6c9b1").grid(row=row_num, column=3, padx=10, pady=5)
            tk.Label(self.compras_frame, text=estado_envio, font=("Arial", 12), bg="#d6c9b1").grid(row=row_num, column=4, padx=10, pady=5)
            # Modificar estado de envío
            if self.usuario.rol == 1:  # Si es admin, puede cambiar el estado
                estado_combobox = ttk.Combobox(self.compras_frame, values=["En proceso de envío","Pago REcibido","etc", "Enviado", "Entregado"], state="readonly")
                estado_combobox.set(estado_envio)  # Establecer el valor actual
                estado_combobox.grid(row=row_num, column=5, padx=10, pady=5)
                button = tk.Button(self.compras_frame, text="Actualizar", command=lambda compra=compra, estado_combobox=estado_combobox: self.actualizar_estado(compra, estado_combobox))
                button.grid(row=row_num, column=6, padx=10, pady=5)
            else:
                # Si no es admin, mostrar solo el estado
                tk.Label(self.compras_frame, text="No editable", font=("Arial", 12), bg="#d6c9b1").grid(row=row_num, column=5, padx=10, pady=5)

    def actualizar_estado(self, compra, estado_combobox):
        """Actualiza el estado de envío de la compra"""
        nuevo_estado = estado_combobox.get()

        # Si el estado seleccionado es "Entregado", pedir confirmación
        if nuevo_estado == "Entregado":
            confirmar = simpledialog.askstring("Confirmar estado", "¿Quién recibió el paquete?")
            
            if confirmar:  # Si el usuario ingresó un nombre
                compra.set_edoEnvio(nuevo_estado+"Recibido por "+confirmar)  # Actualizar el estado de envío

                #compra.set_quien_recibio(confirmar)  # Guardar el nombre de la persona que recibió el paquete

                messagebox.showinfo("Estado actualizado", f"La compra ha sido marcada como entregada. Recibido por: {confirmar}")
            else:
                messagebox.showwarning("Entrada requerida", "Debes ingresar el nombre de la persona que recibió el paquete.")
                estado_combobox.set(compra.get_edoEnvio())  # Volver a establecer el estado original
        else:
            compra.set_edoEnvio(nuevo_estado)  # Actualizar el estado de envío
            messagebox.showinfo("Estado actualizado", f"El estado de envío de {compra.get_producto().nombre} ha sido actualizado a {nuevo_estado}.")
