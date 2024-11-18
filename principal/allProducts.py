import tkinter as tk
from PIL import Image, ImageTk
from principal.ventanaUsuarios import *

def open_all_products():
    global menu
    products_window = tk.Toplevel() 
    products_window.title("Productos")
    
    screen_width = products_window.winfo_screenwidth()
    screen_height = products_window.winfo_screenheight()
    products_window.geometry(f"{screen_width}x{screen_height}")

    products_window.configure(bg="#d6c9b1") 

    header_frame = tk.Frame(products_window, bg="#d6c9b1", height=100)
    header_frame.pack(fill="x")

    header_label = tk.Label(header_frame, text="FLORERIA'S BORNAY", font=("Times New Roman", 24, "bold"), bg="#d6c9b1", fg="#4a2e5d")
    header_label.pack(side="left", padx=20, pady=20)

   

    menu_icon = tk.Label(header_frame, text="≡", font=("Arial", 24, "bold"), bg="#d6c9b1", fg="black")
    menu_icon.pack(side="left", padx=10)
    menu = create_menu(products_window)

    def show_menu(event):
        menu.post(event.x_root, event.y_root)  

    menu_icon.bind("<Button-1>", show_menu)


    search_bar = tk.Entry(header_frame, font=("Arial", 14), width=30, bg="#c7b7a4")
    search_bar.pack(side="left", padx=10)
    search_icon = tk.Label(header_frame, text="🔍", font=("Arial", 18), bg="#d6c9b1", fg="black")
    search_icon.pack(side="left")

   


    flower_data = [
        ("img/suenio_primaveral.jpg", "Sueño primaveral"),
        ("img/encanto_amatis.jpg", "Encanto de amatista"),
        ("img/nostalgia_otono.jpg", "Nostalgia de otoño"),
        ("img/brisa_lila.jpg", "Brisa lila"),
        ("img/dulce_encanto.jpg", "Dulce encanto"),
        ("img/amanecer.jpg", "Amanecer"),
        ("img/paraiso_azul.jpg", "Paraíso azul"),
        ("img/sol_y_nieve.jpg", "Sol y nieve")
    ]

    

    flowers_frame = tk.Frame(products_window, bg="#d6c9b1")
    flowers_frame.pack(pady=20)

    row, col = 0, 0
    for file, name in flower_data:
        img = load_image(file)
        if img:  
            img_label = tk.Label(flowers_frame, image=img)
            img_label.image = img  
            img_label.grid(row=row, column=col, padx=20, pady=10)

            text_label = tk.Label(flowers_frame, text=name, font=("Arial", 12, "italic"))
            text_label.grid(row=row + 1, column=col, pady=(0, 20))

            col += 1
            if col > 3:  
                col = 0
                row += 2
        else:
            print(f"Error al cargar la imagen: {file}")

   
def load_image(file, size=(150, 150)):
    try:
        img = Image.open(file)
        img = img.resize(size)
        return ImageTk.PhotoImage(img)
    except FileNotFoundError:
        print(f"Error: El archivo {file} no se encontró.")
        return None
   


def create_menu(products_window):
    menu = tk.Menu(products_window)
    products_window.config(menu=menu)

   
    produtos= tk.Menu(menu, tearoff=0)
    menu.add_cascade(label="Productos", font=("Times New Roman", 20),menu=produtos)
    produtos.add_command(label="Ver todos los productos  🫡", font=("Arial", 18),command=lambda: (products_window.destroy(), open_all_products()))
    produtos.add_separator()
    payment_menu = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label="Método de pago", font=("Times New Roman", 20),menu=payment_menu)
    payment_menu.add_command(label="Opción 1 🛒",font=("Arial", 18), command=lambda: print("Seleccionaste Opción 1")  ,image=load_image("img/icono_carrito.png"), compound='left')
    payment_menu.add_command(label="Opción 3 💵", font=("Arial", 18),command=lambda: print("Seleccionaste Opción 3"))
    payment_menu.add_separator()
    payment_menu.add_command(label="Volver a inicio", command=products_window.destroy)

    return menu

def load_image(file, size=(20, 20)): 
    try:
        img = Image.open(file)
        img = img.resize(size)  
        return ImageTk.PhotoImage(img)
    except FileNotFoundError:
        print(f"Error: El archivo {file} no se encontró.")
        return None
    
