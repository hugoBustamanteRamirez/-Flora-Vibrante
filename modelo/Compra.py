class Compra:
    def __init__(self, usuario, producto,edoEnvio="En proceso de envío"):
        self.usuario = usuario  
        self.producto = producto  
        self.edoEnvio = edoEnvio

    def get_usuario(self):
        """Devuelve el usuario que realizó la compra."""
        return self.usuario

    def get_producto(self):
        """Devuelve el producto que fue comprado."""
        return self.producto
    
    def get_edoEnvio(self):
        """Devuelve el usuario que realizó la compra."""
        return self.edoEnvio

    
    
    def set_edoEnvio(self, set_edoEnvio):
        self.set_edoEnvio = set_edoEnvio
    
    


    def __str__(self):
        """Representación en cadena de la compra."""
        return f"Compra realizada por {self.usuario.nombre}. Producto: {self.producto.nombre} .Estado de envío: {self.edoEnvio}"

