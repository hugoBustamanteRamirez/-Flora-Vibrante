import tkinter as tk
from tkinter import font, messagebox
from PIL import Image, ImageTk
from modelo.Usuario import Usuario
from modelo.Producto import Producto
from modelo.Compra import Compra
from principal.panelLogin import PanelLogin
from principal.panelProductos import PanelProductos
from principal.panelListarUsuarios import PanelUsuarios
from principal.panelRegistrarUsuario import PanelRegistrarUsuario
from principal.panelAccones import PanelAcciones
from principal.panelEliminarUsuario import PanelEliminarUsuario
from principal.panelCrearCuenta import PanelCrearCuenta
from principal.panelRegistrarProducto import PanelRegistrarProducto
from principal.panelMostrarProductos import PanelMostrarProductos
from principal.panelEliminarProducto import PanelEliminarProducto
from principal.panelModificarProductos import PanelModificarProducto
from principal.panelRegistrarCompra import PanelRegistrarCmpra
from principal.panelMostrarCompras import PanelMostrarCompras
from principal.panelCuentaUsuario import PanelCuentaUsuario
from principal.panelRealizarCompra import PanelRealizarCompra
from principal.panelModificarDireccion import PanelModificarDireccion
from principal.panelModificarEnvio import PanelModificarEstadoEnvio


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Florerías bornay") #establecemos el nombre de la app
        #tomamos las medias de nuestra pantalla y con self.geometry dibujamos la ventana
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}")

        #variables globales donde inicializamos, esto para hacer recursividad para reutilizar lo mas que se pueda y no perder datos

        self.usuario_logueado = None
        self.producto_seleccionado = None
        self.usuario_actual = None

        #creacion y llenado de los arreglos usuarios,productos y compras(donde se encuentran dichas clases? en modelo)
        self.usuarios = [
            Usuario("admin", "1234","La joya ", "9876 5432 1098 7654", "11/23", "456",7000,rol=1),
            Usuario("karol", "1234","La palma", "1234 5678 9012 3456", "12/25", "123",7000,rol=0,),
            Usuario("yo", "1234", "el povorin",rol=0)
        ]
        self.productos = [
            Producto("123456789", "Amacener","Rosa rosa rosa rosa  ", 45,"Envio en 1 o2 dias","img/suenio_primaveral.jpg"),
            Producto("123456788", "paraiso azul","Rosa rosa rosa rosa ", 34,"Envio en 1 o2 dias","img/amanecer.jpg"),
            Producto("123456777", "brisa lila", "Rosa rosa rosa rosa ",90,"Envio en 1 o2 dias","img/brisa_lila.jpg"),
            Producto("123456777", "brisa lila", "Rosa rosa rosa rosa ",90,"Envio en 1 o2 dias","img/dulce_encanto.jpg"),
            Producto("123456777", "brisa lila", "Rosa rosa rosa rosa ",90,"Envio en 1 o2 dias","img/nostalgia_otono.jpg"),
            Producto("123456777", "brisa lila", "Rosa rosa rosa rosa ",90,"Envio en 1 o2 dias","img/paraiso_azul.jpg"),
            Producto("123456777", "brisa lila", "Rosa rosa rosa rosa ",90,"Envio en 1 o2 dias","img/sol_y_nieve.jpg"),
               ]
        self.compras=[
              Compra(usuario=self.usuarios[1],producto=self.productos[0],nuevaDireccion="Calle Siempre Viva 123",cant=2,total=self.productos[0].precio * 2,edoEnvio="En camino"),
              Compra(usuario=self.usuarios[0],producto=self.productos[0],nuevaDireccion="Calle Siempre Viva 123",cant=2,total=self.productos[0].precio * 2,edoEnvio="En camino"),

         ]
        #inicializamos nuestra variable  self.current_panel por que esta cambiara a lo largo de la ejecucion 
        self.current_panel = None
         #mostramos el panel por defecto, si o si al ejecutar la app esta sera la primera que se muestre
        self.show_panel(PanelLogin) 
        
#funcion que ayuda al cambiar de panelees
    def show_panel(self, panel_class,*args, **kwargs):
       #elimina nuestro panel en el que estamos si cambiamos de panel(opcion)
        if self.current_panel:
            self.current_panel.pack_forget()
            self.current_panel.destroy()

        
        if panel_class == PanelCrearCuenta:
            self.current_panel = panel_class(self, self.usuarios)
        elif panel_class == PanelLogin:
            self.current_panel = panel_class(self, self, self.usuarios, self.on_login_success)
        elif panel_class == PanelProductos:
            self.current_panel = panel_class(self, self.productos,self.usuario_logueado)
        elif panel_class == PanelRegistrarUsuario:
            self.current_panel = panel_class(self, self.usuarios)
        elif panel_class == PanelEliminarUsuario:
            self.current_panel = panel_class(self, self.usuarios)
        elif panel_class == PanelUsuarios:
            self.current_panel = panel_class(self, self.usuarios)
        elif panel_class == PanelRegistrarProducto:
            self.current_panel = panel_class(self, self.productos)
        elif panel_class == PanelModificarEstadoEnvio:
            self.current_panel = panel_class(self, self.compras, self.usuario_logueado)
        elif panel_class == PanelModificarDireccion:
            self.current_panel = panel_class(self, self.compras, self.usuario_logueado)

        elif panel_class == PanelMostrarProductos:
            self.current_panel = panel_class(self, self.productos)
        elif panel_class == PanelEliminarProducto:
            self.current_panel = panel_class(self, self.productos)
        elif panel_class == PanelModificarProducto:
            self.current_panel = panel_class(self, self.productos)
        elif panel_class == PanelRegistrarCmpra:
            self.current_panel = panel_class(self, self.productos,self.usuario_logueado)
        elif panel_class == PanelRealizarCompra:
            self.current_panel = panel_class(self,*args)
        elif panel_class == PanelCuentaUsuario:
            self.current_panel = panel_class(self,self.usuario_logueado)
        elif panel_class == PanelMostrarCompras:
            self.current_panel = panel_class(self, self.compras, self.usuario_logueado)
   
        else:
            self.current_panel = panel_class(self, *args, **kwargs)

        

        self.current_panel.pack(expand=True, fill="both")#posicioneas o colocamos nuestro panel dentro de la ventana
   
    # ir a on_login_succes antes de ver esta funcion
    def crear_menu(self):
        self.config(menu=None)
        
        #if self.usuario_logueado is None:
         #   return 
        menubar = tk.Menu(self, background='#e8bf30', foreground='white', 
                        activebackground='#333333', activeforeground='white')
        self.config(menu=menubar)
        
        if self.usuario_logueado.rol == 1: 
            self.crear_menu_admin(menubar)
        elif self.usuario_logueado.rol == 0:  
            self.crear_menu_usuario(menubar)
            print("Creando menú para usuario normal")
        else:
            self.crear_menu_usuario(menubar)
            print("Creando menú")



    def crear_menu_admin(self, menubar):
        menu_usuarios = tk.Menu(menubar, tearoff=0, background='#1a1a1a', foreground='white', font=('Arial', 14))
        menubar.add_cascade(label="Usuarios 👤", menu=menu_usuarios)
        menu_usuarios.add_command(label="Registrar nuevo usuario ✅", command=lambda: self.show_panel(PanelRegistrarUsuario))
        menu_usuarios.add_command(label="Listar usuarios 📓", command=lambda: self.show_panel(PanelUsuarios))
        menu_usuarios.add_command(label="Eliminar usuario ❌", command=lambda: self.show_panel(PanelEliminarUsuario))
        menu_usuarios.add_separator()
        
        menu_productos = tk.Menu(menubar, tearoff=0, background='#1a1a1a', foreground='white', font=('Arial', 14))
        menubar.add_cascade(label="Productos 🌹🌹", menu=menu_productos)
        menu_productos.add_command(label="Registrar nuevo producto ✅", command=lambda: self.show_panel(PanelRegistrarProducto))
        menu_productos.add_command(label="Modificar producto ♻", command=lambda: self.show_panel(PanelModificarProducto))
        menu_productos.add_command(label="Eliminar producto ❌", command=lambda: self.show_panel(PanelEliminarProducto))
        menu_productos.add_separator()
        
        menu_compras = tk.Menu(menubar, tearoff=0, background='#1a1a1a', foreground='white', font=('Arial', 14))
        menubar.add_cascade(label="Realizar una compra 🛒", menu=menu_compras)
        menu_compras.add_command(label="Registrar compra ✅", command=lambda: self.show_panel(PanelProductos))
        menu_compras.add_command(label="Modificar estado del envio ✅", command=lambda: self.show_panel(PanelModificarEstadoEnvio))
        #menu_compras.add_command(label="Modificar direccion  ✅", command=lambda: self.show_panel(PanelModificarDireccion))
        menu_compras.add_command(label="Ver mis pedidos 📓", command=lambda: self.show_panel(PanelMostrarCompras))
        menu_usuario = tk.Menu(menubar, tearoff=0, background='#1a1a1a', foreground='white', font=('Arial', 14))
        menubar.add_cascade(label="Mi Perfil", menu=menu_usuario)
        menu_usuario.add_command(label="Mis datos de facturacion",command=lambda:self.show_panel(PanelCuentaUsuario))
       
        menu_usuario.add_command(label="Cerrar sesión", command=self.logout)


    def crear_menu_usuario(self, menubar):
        menu_compras = tk.Menu(menubar, tearoff=0, background='#1a1a1a', foreground='white', font=('Arial', 14))
        menubar.add_cascade(label="Realizar una compra 🛒", menu=menu_compras)
        menu_compras.add_command(label="Registrar compra ✅", command=lambda: self.show_panel(PanelProductos))
        menu_compras.add_command(label="Ver mis pedidos 📓", command=lambda: self.show_panel(PanelMostrarCompras))
        #menu_compras.add_command(label="Modificar direccion  ✅", command=lambda: self.show_panel(PanelModificarDireccion))
       
        
        menu_usuario = tk.Menu(menubar, tearoff=0, background='#1a1a1a', foreground='white', font=('Arial', 14))
        menubar.add_cascade(label="Mi Perfil", menu=menu_usuario)
        menu_usuario.add_command(label="Mis datos de facturacion",command=lambda:self.show_panel(PanelCuentaUsuario))
        menu_usuario.add_command(label="Cerrar sesión", command=self.logout)

       
    
    #esta funcion nos ayudara a indentificar el y que usuario esta con la session, y de acuerdo al rol se creara la funcion crear_menu(), dentro de 
    # esta funcion crar_menu() estara la logica para mostrar las opciones deacuerdo al rol del usuario   
    def on_login_success(self, user):
        self.usuario_logueado = user #usamos nuestra variable globlal para capturar al usuario que ha iniciado sesion 
        self.crear_menu() #ir ahora si a la funcion de arriba 
        self.show_panel(PanelRegistrarCmpra, self.productos, self.usuario_logueado) #mostramos este panel 
        messagebox.showinfo("Login exitoso", f"Bienvenido, {user.get_nombre()}")
        print(f"Rol del usuario logueado: {user.rol}")
        producto_seleccionado = self.productos[0] #nos ayudara a sabaer que producto se selecciono cuando dan click en comprar 
        #self.show_panel(PanelRealizarCompra, producto_seleccionado, self.usuario_logueado)  # Muestra el panel de compra
        #self.show_panel(PanelRealizarCompra, producto_seleccionado, self.usuario_logueado, self.compras)
        self.show_panel(PanelRealizarCompra, producto_seleccionado, self.usuario_logueado, self.compras) #se muestra ese panel

    def ivitado(self):
        self.crear_menu()  
        


#esta funcion se llama en las opciones cerrar sesion que como su nombre lo dice cerramos la sesion
#basicamente es asignarle nada nuestra ariable self.usuario_logueado, asi como borrar el menu(no lo hace jaja), destruimos o borrramos el panel en elque estamos
# y nos redirige al panel login
    def logout(self):
        self.usuario_logueado = None

        self.menu = None
        self.config(menu=None)

        if self.current_panel:
            self.current_panel.pack_forget()
            self.current_panel.destroy()
            self.current_panel = None

        self.show_panel(PanelLogin)
#creamos la estancia de esta misma clase,la definimoos como nuestra clase principal
if __name__ == "__main__":
    app = MainApp()
    app.mainloop()