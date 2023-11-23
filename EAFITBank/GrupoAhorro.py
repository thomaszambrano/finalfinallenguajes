from Seguridad import Seguridad
seguridad = Seguridad()
class GrupoAhorro:
    def __init__(self, nombres="", correo="", contraseña="", nombre_grupo="", cuenta=6000, prestamo=0, meses=0):
        self.datos_personales_grupo = (nombres, correo, contraseña)
        self.nombre_grupo = nombre_grupo
        self.cuenta = cuenta
        self.prestamo = prestamo
        self.meses = meses

    def obtener_datos_personales_grupo(self):
        return self.datos_personales_grupo

    def obtener_nombre_grupo(self):
        return self.nombre_grupo

    def obtener_cuenta(self):
        return self.cuenta

    def obtener_prestamo(self):
        return self.prestamo

    def obtener_meses(self):
        return self.meses


class Clientes(GrupoAhorro):
    def __init__(self, nombres="", correo="", contraseña=""):
        super().__init__(nombres, correo, contraseña)


class CrearGrupo:
    def crear_grupos(self, lista_usuarios):
        while True:  
            print("1. Grupo de ahorro de 2 personas")
            print("2. Grupo de ahorro de 3 personas")
            print("3. Volver al menú principal")
            opcion = input("")
            if opcion in ["1", "2"]:
                num_personas = 2 if opcion == "1" else 3
                nombres = []

                for i in range(num_personas):
                    print(f"Ingrese la información del usuario {i + 1}:")
                    nombre = input("Ingrese un nombre de usuario: ")
                    contraseña = input("Ingrese la contraseña: ")

                    usuario_encontrado = False
                    for usuario in lista_usuarios:
                        if usuario.obtener_datos_personales()[0] == nombre and usuario.obtener_datos_personales()[2] == contraseña:
                            print("Usuario encontrado")
                            print(25*"")
                            usuario_encontrado = True
                            break

                    if not usuario_encontrado:
                        print("Usuario no encontrado. Vuelva a intentar.")
                        return None

                    nombres.append(nombre)

                grupo_nombre = input("Ingrese el nombre del grupo: ")
                grupo_correo = input("Ingrese el correo del usuario del grupo: ")
                grupo_contraseña = seguridad.solicitar_contraseña()
                return nombres, grupo_nombre, grupo_correo, grupo_contraseña

            elif opcion == "3":
                print("Volviendo al menú principal...")
                break

            else:
                print("Escoja una opción válida")

    def crear_grupo(self, lista_usuarios, lista_grupos):
        datos_usuario = self.crear_grupos(lista_usuarios.lista_usuarios)
        if datos_usuario:
            nombres, nombre_grupo, correo, contraseña = datos_usuario

            grupo = GrupoAhorro(nombres=nombres, correo=correo, contraseña=contraseña, nombre_grupo=nombre_grupo)

            lista_grupos.agregar_grupo(grupo)


