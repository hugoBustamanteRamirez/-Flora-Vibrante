import tkinter as tk
from tkinter import messagebox,ttk
from modelo.Compra import Compra
from tkinter import simpledialog, messagebox
import os
from datetime import datetime
#from principal.panelProductos import producto_seleccionado, usuario_actual
class PanelRealizarCompra(tk.Frame):
    def __init__(self, parent,producto, usuario,compras):
        super().__init__(parent)
        self.compras=compras
        self.producto = producto  # Asignar directamente el producto
        self.usuario = usuario  # Asignar directamente el usuario
       
        self.configure(bg="#d6c9b1")

        tk.Label(self, text="Confirmar Compra", font=("Arial", 16), bg="#d6c9b1").pack(pady=10)

        tk.Label(self, text=f"Producto: {producto.nombre}", bg="#d6c9b1").pack(pady=5)
        self.precio_label =tk.Label(self, text=f"Precio: ${producto.precio:.2f}", bg="#d6c9b1")
        self.precio_label.pack(pady=5)

          # Mostrar información inicial
        self.numeroTarjeta_var = tk.StringVar(value=f"Realizar compra con la tarjeta: {usuario.numero_tarjeta}")
        self.numeroTarjeta_label = tk.Label(self, textvariable=self.numeroTarjeta_var, bg="#d6c9b1")
        self.numeroTarjeta_label.pack(pady=5)

        tk.Button(self, text="Cambiar método de pago", command=self.cambiarMetodo).pack(pady=10)
  
        

          # Spinner para seleccionar la cantidad
        self.cantidad_var = tk.IntVar(value=1)  # Valor inicial
        tk.Label(self, text="Cantidad:", bg="#d6c9b1").pack(pady=5)
        self.spinbox_cantidad = tk.Spinbox(self, from_=1, to=100, textvariable=self.cantidad_var, width=5)
        self.spinbox_cantidad.pack(pady=5)

        

           # Crear campos para la dirección de envío
        tk.Label(self, text="Codigo Postal:", bg="#d6c9b1").pack(pady=5)

        # Código Postal
        self.entry_codigo_postal = tk.Entry(self, width=40)
        self.entry_codigo_postal.pack(pady=5)
        self.entry_codigo_postal.bind("<KeyRelease>", lambda event: self.mostrar_informacion_postal(event))

        
       
        # Otros campos
        tk.Label(self, text="Colonia:", bg="#d6c9b1").pack(pady=5)
        self.entry_colonia = tk.Entry(self, width=40)
        self.entry_colonia.pack(pady=5)
        tk.Label(self, text="Ciudad:", bg="#d6c9b1").pack(pady=5)
        

        self.entry_ciudad = tk.Entry(self, width=40)
        self.entry_ciudad.pack(pady=5)
        
          # Combobox para seleccionar el país
        self.label_pais = tk.Label(self, text="País: ")
        self.label_pais.pack(pady=10)
  
        self.pais_combobox = ttk.Combobox(self, state="readonly")
        self.pais_combobox.pack(pady=10)
        self.pais_combobox.bind("<<ComboboxSelected>>", self.actualizar_estados)  # Asociar evento de selección

        tk.Label(self, text="Estado:", bg="#d6c9b1").pack(pady=5)
        
        self.estado_combobox = ttk.Combobox(self, state="readonly")
        self.estado_combobox.pack(pady=10)






        self.aceptar=tk.Button(self, text="Confirmar Compra", command=self.realizar_compra)
        self.aceptar.pack(pady=10)
        tk.Button(self, text="Cancelar", command=self.cancelar_compra).pack(pady=5)
        self.cantidad_var.trace("w", self.actualizar_precio)
        #self.numeroTarjeta.trace("w",self.actualizar_precio)

        self.paises = {
            "México": ["CDMX", "Jalisco", "Nuevo León", "Puebla"],
            "Estados Unidos": ["California", "Texas", "Florida", "New York"],
            "Alemania": ["Baviera", "Berlín", "Hamburgo", "Hessen"],
            "Francia": ["París", "Marsella", "Lyon", "Toulouse"],
            "Reino Unido": ["Inglaterra", "Escocia", "Gales", "Irlanda del Norte"],
            "Suiza": ["Zúrich", "Ginebra", "Basilea", "Berna"]
        }
    def mostrar_informacion_postal(self, event):
       
        codigo_postal = self.entry_codigo_postal.get()

        
        # Lista de países
        paises = {
            "61": "México",
            "225": "Estados Unidos",
            "563": "Alemania",
            "505": "Francia",
            "510": "Reino Unido",
            "008": "Suiza",
        }

        # Obtener los países correspondientes según el código postal
        paises_validos = [pais for prefijo, pais in paises.items() if codigo_postal.startswith(prefijo)]
        
        if paises_validos:
            self.pais_combobox['values'] = paises_validos
            self.pais_combobox.set(paises_validos[0])  # Seleccionar el primer país por defecto
            pais=""
            self.actualizar_estados()
        else:
            self.pais_combobox.set("")  # Si no hay país válido, limpiar el Combobox
            #messagebox.showerror("Error", "Por el momento solo contamos con entregas a algunos países.")
            pais = "Por el momento solo contamos con entregas a Alemania, Francia, Reino Unido, USA, México."
            self.actualizar_estados()

        self.label_pais.config(text=f"País: {pais}")    


    def actualizar_estados(self, event=None):
        """Actualizar el combobox de estados según el país seleccionado."""
        pais_seleccionado = self.pais_combobox.get()

        # Verificar si el país seleccionado está en el diccionario
        if pais_seleccionado in self.paises:
            # Actualizar los estados según el país seleccionado
            estados = self.paises[pais_seleccionado]
            self.estado_combobox['values'] = estados
            self.estado_combobox.set(estados[0])  # Seleccionar el primer estado por defecto
        else:
            self.estado_combobox.set("")  # Limpiar el combobox de estados si no hay país

    def actualizar_precio(self, *args):
        """Método para actualizar el precio según la cantidad seleccionada."""
        cantidad = self.cantidad_var.get()
        precio_total = self.producto.precio * cantidad
        self.precio_label.config(text=f"Precio: ${precio_total:.2f}")
    

    def realizar_compra(self):
        cantidad = self.cantidad_var.get()
        codigo_postal = self.entry_codigo_postal.get()
        pais = self.label_pais.cget("text").replace("País: ", "")
        colonia = self.entry_colonia.get()
        ciudad = self.entry_ciudad.get()
        estado = self.estado_combobox.get()
        
        if not codigo_postal or not colonia or not ciudad or not estado:
            messagebox.showerror("Error", "Todos los campos de dirección son obligatorios.")
            return

            # Concatenar la dirección completa
        direccion = f"{colonia}, {ciudad}, {estado}, {pais}, CP: {codigo_postal}"

        # Asignar la dirección a la compra
        #self.usuario.set_direc(direccion)
    
        
        total_precio = self.producto.precio * cantidad

        if self.usuario.balance < total_precio:
            messagebox.showerror("Saldo insuficiente", "No tienes suficiente saldo para realizar esta compra.")
            return

        # Restar el monto de la compra al saldo del usuario
        self.usuario.balance -= total_precio
        

        # Crear una nueva compra y agregarla a la lista de compras
        nueva_compra = Compra(self.usuario, self.producto, nuevaDireccion=direccion, cant=cantidad, imagen_path=self.producto.imagen_path)

        self.compras.append(nueva_compra)  # Almacenar la compra en la lista de compras
         # Generar el ticket
        self.generar_ticket(nueva_compra, total_precio)

        # Confirmar la compra y mostrar el mensaje
        messagebox.showinfo("Compra Exitosa", f"Has comprado {cantidad} unidades de {self.producto.nombre} por ${total_precio:.2f}")


        # Regresar al panel de productos
        from principal.panelProductos import PanelProductos
        self.master.show_panel(PanelProductos,self.usuario)

    def cancelar_compra(self):
        """
        Lógica para cancelar la compra y volver al panel anterior.
        """
        from principal.panelProductos import PanelProductos
        self.master.show_panel(PanelProductos,self.usuario)
    def cambiarMetodo(self):
        """
        Muestra una caja para ingresar un nuevo método de pago.
        """
        nuevo_metodo = simpledialog.askstring("Cambiar método de pago", "Ingresa el nuevo número de tarjeta:")
        
        if nuevo_metodo:
            # Validar si el número ingresado es válido
            if not nuevo_metodo.isdigit() or len(nuevo_metodo) != 16:
                messagebox.showerror("Error", "Número de tarjeta no válido. Debe ser un número de 16 dígitos.")
                return

            # Actualizar el número de tarjeta del usuario
            self.usuario.numero_tarjeta = nuevo_metodo

            # Actualizar la etiqueta de la tarjeta de crédito
            self.numeroTarjeta_var.set(f"Realizar compra con la tarjeta: {self.usuario.numero_tarjeta}")
            messagebox.showinfo("Éxito", "El método de pago ha sido actualizado con éxito.")
    def generar_ticket(self, compra, total_precio):
        """Generar un archivo de ticket con los detalles de la compra."""
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") #guardamos la hora y fecha en la quehicmos la compra
        ticket_dir = "tickets" #la carpeta doende se guardaran los tickets
        os.makedirs(ticket_dir, exist_ok=True)  # Crear la carpeta si no existe
        ticket_path = os.path.join(ticket_dir, f"ticket_{timestamp}.txt") #formamos la ruta,osea tickets/ticket_{timestamp}


#tenmos el txt ya generado pero vacio, esto lo escribe y/0 genera extrallendo datos de arreglo compra
        with open(ticket_path, "w", encoding="utf-8") as file:
            file.write("=== TICKET DE COMPRA ===\n")
            file.write(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write(f"Usuario: {compra.get_usuario().nombre}\n")
            file.write(f"Producto: {compra.get_producto().nombre}\n")
            file.write(f"Cantidad: {compra.get_cant()}\n")
            file.write(f"Precio unitario: ${compra.get_producto().precio:.2f}\n")
            file.write(f"Total: ${total_precio:.2f}\n")
            file.write(f"Dirección de envío:\n{compra.get_nuevaDireccion()}\n")
            file.write(f"Estado de envío: {compra.get_edoEnvio()}\n")
            file.write("========================\n")
        
        # Notificar al usuario
        messagebox.showinfo("Ticket Generado", f"Se generó un ticket de compra en: {ticket_path}")        