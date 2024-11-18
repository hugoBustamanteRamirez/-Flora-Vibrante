import tkinter as tk
from tkinter import font, messagebox
from principal.panelProductos import PanelProductos
from PIL import Image, ImageTk

from principal.panelCrearCuenta import PanelCrearCuenta


class PanelLogin(tk.Frame):
    def __init__(self, parent, main_app, usuarios, on_login_success):
        super().__init__(parent)
        self.main_app = main_app  
        self.usuarios = usuarios  
        self.on_login_success = on_login_success  

        bg_img_path = "img/background.jpg"
        self.background_image = load_background(parent, bg_img_path)
        bg_label = tk.Label(self, image=self.background_image)
        bg_label.place(relwidth=1, relheight=1)
       

        name_label = tk.Label(self, text="Nombre de usuario:", font=("Arial", 12), bg="#cccccc", fg="#333333")
        name_label.place(relx=0.4, rely=0.5, anchor="center")

        self.name_usuario = tk.Entry(self, font=("Arial", 12), width=30)
        self.name_usuario.place(relx=0.57, rely=0.5, anchor="center")

        password_label = tk.Label(self, text="Contraseña:", font=("Arial", 12), bg="#cccccc", fg="#333333")
        password_label.place(relx=0.4, rely=0.55, anchor="center")

        self.pass_usuario = tk.Entry(self, font=("Arial", 12), show="*", width=30)
        self.pass_usuario.place(relx=0.57, rely=0.55, anchor="center")

        start_button = tk.Button(self, text="Iniciar sesión", font=("Arial", 12), bg="#cccccc", fg="#333333",
                                 padx=20, pady=5, command=self.validar_login)
        start_button.place(relx=0.5, rely=0.6, anchor="e")

        start_button = tk.Button(self, text="No tienes una cuenta?....crea una aqui", font=("Arial", 12), bg="#cccccc", fg="#333333",
                                 padx=20, pady=5, command=lambda: self.main_app.show_panel(PanelCrearCuenta))
        start_button.place(relx=0.5, rely=0.6, anchor="w")

    def validar_login(self):
        nombre_usuario = self.name_usuario.get()
        contrasena_usuario = self.pass_usuario.get()

     
        for usuario in self.usuarios:
            if usuario.validar_usuario(nombre_usuario, contrasena_usuario):
                if usuario.isAdmin():
                    #messagebox.showinfo("Login exitoso", f"Bienvenido, {usuario.get_nombre()}!")
                    self.on_login_success(usuario)
                    self.main_app.show_panel(PanelProductos)

                    #self.main_app.crear_menu()
                    return
                else:
                    self.on_login_success(usuario)
                    self.main_app.show_panel(PanelProductos)
  
                    return
        
        messagebox.showerror("Error de Login", "Usuario o contraseña incorrectos")


def load_background(root, img_path):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    bg_image = Image.open(img_path)
    bg_image = bg_image.resize((screen_width, screen_height))
    return ImageTk.PhotoImage(bg_image)

def show_panel(self, panel_class):
       
        if self.current_panel:
            self.current_panel.pack_forget()
            self.current_panel.destroy()
        
        if panel_class == PanelCrearCuenta:
            self.current_panel = panel_class(self, self.usuarios)

        self.current_panel.pack(expand=True, fill="both")
