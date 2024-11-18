class Compra:
    def __init__(self, usuario, producto,nuevaDireccion,cant=0,total=0,edoEnvio=""):
        self.usuario = usuario  
        self.producto = producto  
        self.edoEnvio = edoEnvio
        self.nuevaDireccion=nuevaDireccion
        self.cant=cant
        self.total=total

    def get_usuario(self):
        """Devuelve el usuario que realizó la compra."""
        return self.usuario

    def get_producto(self):
        """Devuelve el producto que fue comprado."""
        return self.producto
    
    def get_edoEnvio(self):
        """Devuelve el usuario que realizó la compra."""
        return self.edoEnvio
    
    def get_cant(self):
        return self.cant

    def set_cant(self, cant):
        self.cant = cant

    def get_nuevaDireccion(self):  # Método de acceso correcto
        return self.nuevaDireccion
    
    def set_nuevaDireccion(self, nuevaDireccion):  # Método de modificación correcto
        self.nuevaDireccion = nuevaDireccion

    def get_total(self):
        return self.total

    def set_cant(self, total):
        self.cant = total
    
    
    def set_edoEnvio(self, set_edoEnvio):
        self.edoEnvio = set_edoEnvio
    
    


    def __str__(self):
        """Representación en cadena de la compra."""
        return f"Compra realizada por {self.usuario.nombre}. Producto: {self.producto.nombre} .Estado de envío: {self.edoEnvio}"

