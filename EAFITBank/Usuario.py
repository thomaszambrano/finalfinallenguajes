from Seguridad import Seguridad
seguridad = Seguridad()
class Usuario:
    def __init__(self, nombre="", correo="", contraseña="", cuenta=1000):
        self.datos_personales = (nombre, correo, contraseña)
        self.cuenta = cuenta

    def obtener_datos_personales(self):
        return self.datos_personales

    def obtener_cuenta(self):
        return self.cuenta
    

class Cliente(Usuario):
    def __init__(self, nombre="", correo="", contraseña=""):
        super().__init__(nombre, correo, contraseña)


class CrearUsuario:
    def SignUp(self):
        nombre = input("Ingrese un nombre de usuario: ")
        correo = input("Ingrese un correo electrónico: ")
        contraseña = seguridad.solicitar_contraseña()
        return nombre, correo, contraseña
                

    def crear_usuario(self, lista_usuarios):
        datos_usuario = self.SignUp()
        if datos_usuario:
            nombre, correo, contraseña = datos_usuario
            cliente = Cliente(nombre=nombre, correo=correo, contraseña=contraseña)
            lista_usuarios.agregar_usuario(cliente)

