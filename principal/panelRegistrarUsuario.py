import tkinter as tk
from tkinter import messagebox
from modelo.Usuario import Usuario
from principal.panelProductos import PanelProductos
#esta clase recibe como parametros a los usuarios,por que?  para registrarlo en nuestro arreglo usarios

class PanelRegistrarUsuario(tk.Frame):
    def __init__(self, parent, usuarios):
        super().__init__(parent)
        self.usuarios = usuarios  #usamos nuestra variable global para guardar el usaurio 
        self.configure(bg="#d6c9b1")  #nada ps el color, background de el panel


        #etiqueta,label ,texto como lo quieran ver,proiedades font= tipo de letra,tamaño, padx,pady= padding x,padding y tamaños pues,anchor= w,e,o,n, posiciones o coordenadas de donde estara situado 
        #pack? para mostrarlo en el panel y/o ventana
        #lo mismo para todas las etiquetas que siguen
        title_label = tk.Label(self, text="Registrar Nuevo Usuario", font=("Arial", 16))
        title_label.pack(pady=10)

        tk.Label(self, text="Nombre:").pack(anchor="w", padx=10)
        self.cajaNombre = tk.Entry(self)
        self.cajaNombre.pack(fill="x", padx=10, pady=5)

        tk.Label(self, text="Contraseña:").pack(anchor="w", padx=10)
        self.cajaContrasena = tk.Entry(self, show="*")
        self.cajaContrasena.pack(fill="x", padx=10, pady=5)

        tk.Label(self, text="Dirección:").pack(anchor="w", padx=10)
        self.cajaDireccion = tk.Entry(self)
        self.cajaDireccion.pack(fill="x", padx=10, pady=5)

        tk.Label(self, text="Rol:").pack(anchor="w", padx=10)
        #parseo, osea convertir a valor entero lo que devulva el radio
        self.rol_var = tk.IntVar()
        tk.Radiobutton(self, text="Usuario", variable=self.rol_var, value=0).pack(anchor="w", padx=20)
        tk.Radiobutton(self, text="Administrador", variable=self.rol_var, value=1).pack(anchor="w", padx=20)

#los btones
        btn_registrar = tk.Button(self, text="Registrar", command=self.registrar_usuario)
        btn_registrar.pack(pady=20)

        btn_Continuar = tk.Button(self, text="Vaciar cajas de texto", command=self.ConContinuarRegistrandoUsuarios)
        btn_Continuar.pack(pady=21)
        
        btn_Cancelar = tk.Button(self, text="Volver", command=self.Cancelar)
        btn_Cancelar.pack(pady=22)
        
#logicara para registrar un usaurio
    def registrar_usuario(self):
        #extraemos el texto de las repsectivas cajas o tk.entrys de arriba
        nombre = self.cajaNombre.get()
        contraseña = self.cajaContrasena.get()
        direccion = self.cajaDireccion.get()
        rol = self.rol_var.get()

        if not nombre or not contraseña or not direccion:
            messagebox.showwarning("Campos vacíos", "Todos los campos son obligatorios.")
            return
#le pasmos los campos
        nuevo_usuario = Usuario(nombre, contraseña, direccion, "5540500001000004","12/25","938",40,rol=rol)
        
        self.usuarios.append(nuevo_usuario)
        messagebox.showinfo("Usuario registrado", f"Usuario {nombre} registrado exitosamente.")
#vaciamos las cajas
        self.cajaNombre.delete(0, tk.END)
        self.cajaContrasena.delete(0, tk.END)
        self.cajaDireccion.delete(0, tk.END)
        self.rol_var.set(0)

    def ConContinuarRegistrandoUsuarios(self):


        self.cajaNombre.delete(0, tk.END)
        self.cajaContrasena.delete(0, tk.END)
        self.cajaDireccion.delete(0, tk.END)
        self.rol_var.set(0)
    
    def Cancelar(self) :
        self.master.show_panel(PanelProductos)  
        