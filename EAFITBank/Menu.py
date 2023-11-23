from Usuario import CrearUsuario
from GrupoAhorro import *
from ListaUsuarios import ListaUsuarios
from ListaGrupos import ListaGrupos
from PrestamosGrupo import PrestamosGrupos
from Transacciones import Transacciones
from Movimientos import Movimientos
from DisolverGrupoAhorro import DisolverGrupoAhorro
import PrestamosGrupo

lista_usuarios = ListaUsuarios()
lista_grupos = ListaGrupos()
creador_usuario = CrearUsuario()
grupo_ahorros = CrearGrupo()
prestamos_grupos = PrestamosGrupos()
movimientos = Movimientos()
transacciones = Transacciones()
disolver = DisolverGrupoAhorro()


class Menu:

    def menuPrincipal(self):

        while True:
            print(25 * "")
            print("1. Crear un nuevo usuario")
            print("2. Crear un grupo de ahorro")
            print("3. Pedir un prestamo para el grupo de ahorro")
            print("4. Impirmir lista de todos los usuarios de EAFITBank")
            print("5. Impirmir lista de todos los grupos de ahorro de EAFITBank")
            print("6. Disolver grupo de ahorro")
            print("7. Prestamo a otros grupos de ahorro")
            print("8. Usuario que aporta mas al grupo de ahorro")
            print("9. Transacciones disponibles")
            print("10. Salir de EAFITBank")
            print(25 * "")

            opcion = input("Seleccione una opción: ")
            print(25 * "")

            if opcion == "1":
                creador_usuario.crear_usuario(lista_usuarios)
            elif opcion == "2":
                grupo_ahorros.crear_grupo(lista_usuarios, lista_grupos)
            elif opcion == "3":
                PrestamosGrupos.prestar_dinero_grupo(lista_grupos, movimientos)
            elif opcion == "4":
                lista_usuarios.imprimir_usuarios()
            elif opcion == "5":
                lista_grupos.imprimir_grupos()
            elif opcion == "6":
                disolver.disolver_grupo(lista_grupos, lista_usuarios, movimientos)
            elif opcion == "7":
                PrestamosGrupos.Prestamo_otros_grupos(lista_grupos, lista_usuarios,lista_usuarios)
            elif opcion == "8":
                ListaGrupos.identificar_y_premiar_mejores_contribuyentes(lista_grupos)
            elif opcion == "9":
                self.menu_transacciones()
            elif opcion == "10":
                print("Se ha cerrado EAFITBank")
                break
            else:
                print("Opción incorrecta, ingrese de nuevo un valor")

    def menu_transacciones(self):
        while True:
            print(25 * "")
            print("1. Ingresar dinero a su cuenta personal")
            print("2. Ingresar dinero a su cuenta de grupo de ahorros")
            print("3. Sacar dinero de su cuenta personal")
            print("4. Sacar dinero de su cuenta de grupo de ahorros")
            print("5. Pagar deudas de su grupo de ahorros")
            print("6. Ver movimientos de su cuenta personal")
            print("7. Ver movimientos de su cuenta de grupo de ahorros")
            print("8. Ver usuario que mas aporta al grupo de ahorros")
            print("9. volver al menu principal de EAFITBank")

            print(25 * "")

            opcion = input("Seleccione una opción: ")
            print(25 * "")

            if opcion == "1":
                transacciones.ingresar_dinero(lista_usuarios, movimientos)
            elif opcion == "2":
                transacciones.ingresar_dinero_grupo(lista_grupos, movimientos)
            elif opcion == "3":
                transacciones.sacar_dinero(lista_usuarios, movimientos)
            elif opcion == "4":
                transacciones.sacar_dinero_grupo(lista_grupos, movimientos)
            elif opcion == "5":
                transacciones.pagar_deudas_grupo(lista_grupos, movimientos)
            elif opcion == "6":
                movimientos.imprimir_movimientos_usuario(lista_usuarios)
            elif opcion == "7":
                movimientos.imprimir_movimientos_grupo(lista_grupos)
            elif opcion == "8":
                GrupoAhorro.usuarioquemasaporta(lista_usuarios, lista_grupos)
            else:
                print("Opción incorrecta, ingrese de nuevo un valor")


if __name__ == "__main__":
    menu = Menu()
    menu.menuPrincipal()
