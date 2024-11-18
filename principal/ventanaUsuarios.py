import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk

import importlib
def open_Users(usuarios):
    global menu

    ventana_usuarios = tk.Toplevel() 
    ventana_usuarios.title("Usuaeos")
    
    screen_width = ventana_usuarios.winfo_screenwidth()
    screen_height = ventana_usuarios.winfo_screenheight()
    ventana_usuarios.geometry(f"{screen_width}x{screen_height}")

    ventana_usuarios.configure(bg="#d6c9b1") 

    header_frame = tk.Frame(ventana_usuarios, bg="#d6c9b1", height=100)
    header_frame.pack(fill="x")

    header_label = tk.Label(header_frame, text="FLORERIA'S BORNAY", font=("Times New Roman", 24, "bold"), bg="#d6c9b1", fg="#4a2e5d")
    header_label.pack(side="left", padx=20, pady=20)

   

    menu_icon = tk.Label(header_frame, text="≡", font=("Arial", 24, "bold"), bg="#d6c9b1", fg="black")
    menu_icon.pack(side="left", padx=10)
    menu = create_menu(ventana_usuarios)

    def show_menu(event):
        menu.post(event.x_root, event.y_root)  

    menu_icon.bind("<Button-1>", show_menu)


    search_bar = tk.Entry(header_frame, font=("Arial", 14), width=30, bg="#c7b7a4")
    search_bar.pack(side="left", padx=10)
    search_icon = tk.Label(header_frame, text="🔍", font=("Arial", 18), bg="#d6c9b1", fg="black")
    search_icon.pack(side="left")

    tree = ttk.Treeview(ventana_usuarios, columns=("Nombre", "Contraseña", "Rol"), show="headings")

    tree.heading("Nombre", text="Nombre")
    tree.heading("Contraseña", text="Contraseña")
    tree.heading("Rol", text="Rol")
    for usuario in usuarios:
        tree.insert("", tk.END, values=(usuario.get_nombre(), usuario.get_contraseña(), usuario.get_rol()))

    tree.pack(padx=10, pady=10)

    #ventana_usuarios.mainloop()


def alguna_funcion():
    from principal.allProducts import open_all_products
    open_all_products()
    
def load_image(file, size=(150, 150)):
    try:
        img = Image.open(file)
        img = img.resize(size)
        return ImageTk.PhotoImage(img)
    except FileNotFoundError:
        print(f"Error: El archivo {file} no se encontró.")
        return None
   
def create_menu(ventana_usuarios):
    menu = tk.Menu(ventana_usuarios)
    ventana_usuarios.config(menu=menu)

    profile_menu = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label="Gestionar usuarios", font=("Times New Roman", 20),menu=profile_menu)
    profile_menu.add_command(label="Ver todos los usaurios 👤", font=("Arial", 18),command=lambda:(ventana_usuarios.destroy(), open_Users()))

    produtos= tk.Menu(menu, tearoff=0)
    menu.add_cascade(label="Productos", font=("Times New Roman", 20),menu=produtos)
    produtos.add_command(label="Ver todos los productos  🫡", font=("Arial", 18),command=lambda: (ventana_usuarios.destroy(),alguna_funcion()))
    produtos.add_separator()
    payment_menu = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label="Método de pago", font=("Times New Roman", 20),menu=payment_menu)
    payment_menu.add_command(label="Opción 1 🛒",font=("Arial", 18), command=lambda: print("Seleccionaste Opción 1")  ,image=load_image("img/icono_carrito.png"), compound='left')
    payment_menu.add_command(label="Opción 3 💵", font=("Arial", 18),command=lambda: print("Seleccionaste Opción 3"))
    payment_menu.add_separator()
    payment_menu.add_command(label="Volver a inicio", command=ventana_usuarios.destroy)

    return menu
