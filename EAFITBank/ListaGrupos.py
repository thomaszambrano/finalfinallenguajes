# ListaGrupos.py
from Usuario import Usuario

class ListaGrupos:
    def __init__(self):
        self.lista_grupos = []

    def agregar_grupo(self, nuevo_grupo):
        self.lista_grupos.append(nuevo_grupo)

    def eliminar_grupo(self, grupo):
        if grupo in self.lista_grupos:
            self.lista_grupos.remove(grupo)
            print("El grupo ha sido eliminado correctamente.")
        else:
            print("El grupo no se encuentra en la lista.")

    def imprimir_grupos(self):
        print("Lista de todos los grupos registrados en EAFITBank: ")
        print(25 * "")
        for grupo in self.lista_grupos:
            datos_personales = grupo.obtener_datos_personales_grupo()
            nombre_grupo = grupo.obtener_nombre_grupo()
            cuenta_grupo = grupo.obtener_cuenta()
            prestamo_grupo = grupo.obtener_prestamo()
            meses_grupo = grupo.obtener_meses()
            print(f"Nombres de los usuarios del grupo: {datos_personales[0]}")
            print(f"Correo: {datos_personales[1]}")
            print(f"Nombre del grupo: {nombre_grupo}")
            print(f"Cuenta del grupo: {cuenta_grupo}")
            print(f"Prestamo del grupo: {prestamo_grupo} y plazo que tienen {meses_grupo} meses")
            print(25 * "-")

    def identificar_y_premiar_mejores_contribuyentes(self):
        from ListaUsuarios import ListaUsuarios  # Importa aquí para evitar dependencia circular

        for grupo in self.lista_grupos:
            usuarios_grupo = grupo.obtener_usuarios()
            usuarios_ordenados = sorted(usuarios_grupo, key=lambda usuario: usuario.obtener_aportes(), reverse=True)

            if usuarios_ordenados:
                mejor_contribuyente = usuarios_ordenados[0]
                mejor_contribuyente.otorgar_descuento_comision(1)
                print(
                    f"El usuario {mejor_contribuyente.obtener_nombre()} del grupo {grupo.obtener_nombre_grupo()} ha sido premiado con un 1% de descuento en comisiones.")
            else:
                print(f"No hay usuarios en el grupo {grupo.obtener_nombre_grupo()}.")

# Luego, puedes llamar a este método en tu código principal cuando lo desees, por ejemplo:
# lista_grupos = ListaGrupos()
# lista_grupos.identificar_y_premiar_mejores_contribuyentes()
