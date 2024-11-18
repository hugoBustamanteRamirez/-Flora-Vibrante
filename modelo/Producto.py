from PIL import Image, ImageTk

class Producto:
    def __init__(self, id_producto, nombre, descripcion, precio, fechatentativa, imagen_path=None):
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.fechatentativa = fechatentativa
        self.imagen_path = imagen_path
        self.imagen = None  

        if imagen_path:
            self.cargar_imagen(imagen_path)
    def get_fechatentativa(self):
        return self.fechatentativa

    def set_fechatentativa(self, fechatentativa):
        self.fechatentativa = fechatentativa
    def obtener_informacion(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Descripción: {self.descripcion}, Precio: ${self.precio}, fecha: {self.fechatentativa}"

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def actualizar_fechatentativa(self, cantidad):
        self.fechatentativa += cantidad
     


    def is_disponible(self):
        return self.fechatentativa > 0

    def cargar_imagen(self, imagen_path):
        try:
            self.imagen = Image.open(imagen_path)
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")
            self.imagen = None

    def mostrar_imagen(self):
        return self.imagen
