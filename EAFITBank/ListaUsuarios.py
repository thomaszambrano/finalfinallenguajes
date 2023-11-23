# ListaUsuarios.py
from Usuario import Usuario

class ListaUsuarios:
    def __init__(self):
        self.lista_usuarios = []

    def agregar_usuario(self, usuario):
        self.lista_usuarios.append(usuario)

    def imprimir_usuarios(self):
        from ListaGrupos import ListaGrupos  # Importa aquí para evitar dependencia circular

        print("Lista de todos los usuarios registrados en EAFITBank: ")
        for usuario in self.lista_usuarios:
            datos_personales = usuario.obtener_datos_personales()
            cuenta = usuario.obtener_cuenta()
            print(f"Nombre: {datos_personales[0]}")
            print(f"Correo: {datos_personales[1]}")
            print(f"Saldo de la cuenta: {cuenta}")
            print(25 * "-")







