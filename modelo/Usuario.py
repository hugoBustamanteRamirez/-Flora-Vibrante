class Usuario:
    def __init__(self, nombre, contraseña, direccion,numero_tarjeta=None, fecha_vencimiento=None, codigo_seguridad=None, balance=0,rol=0, ):
        self.nombre = nombre
        self.contraseña = contraseña
        self.rol = rol 
        self.direccion= direccion
        self.numero_tarjeta = numero_tarjeta
        self.fecha_vencimiento = fecha_vencimiento
        self.codigo_seguridad = codigo_seguridad
        self.balance=balance

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_contraseña(self):
        return self.contraseña

    def set_contraseña(self, contraseña):
        self.contraseña = contraseña

    def get_rol(self):
        return self.rol

    def set_rol(self, rol):
        self.rol = rol

    def get_direc(self):
        return self.direccion

    def set_direc(self, direccion):
        self.direccion = direccion
    
    def set_tarjeta(self, numero, fecha, codigo):
        self.numero_tarjeta = numero
        self.fecha_vencimiento = fecha
        self.codigo_seguridad = codigo

    def get_tarjeta_info(self):
        if self.numero_tarjeta:
            return {
                "numero_tarjeta": self.numero_tarjeta[-4:], 
                "fecha_vencimiento": self.fecha_vencimiento,
            }
        else:
            return None

    def get_fecha_vencimiento(self):
        return self.fecha_vencimiento

    def set_fecha_vencimiento(self, fecha_vencimiento):
        self.fecha_vencimiento = fecha_vencimiento

    def get_codigo_seguridad(self):
        return self.codigo_seguridad

    def set_codigo_seguridad(self, codigo_seguridad):
        self.codigo_seguridad = codigo_seguridad

    def get_balacen(self):
        return self.balance

    def set_nombre(self, balance):
        self.balance = balance


    def __str__(self):
        tipo_usuario = "Administrador" if self.rol == 1 else "Usuario"
        return f"Nombre: {self.nombre}, Contraseña: {self.contraseña}, Rol: {tipo_usuario}"
       
    def validar_usuario(self, nombre_usuario, contrasena_usuario):
        return self.nombre == nombre_usuario and self.contraseña == contrasena_usuario
    
    def isAdmin(self):
        return self.rol == 1
