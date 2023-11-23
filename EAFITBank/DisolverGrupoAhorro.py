from Seguridad import Seguridad
from Comisiones import Comisiones
seguridad = Seguridad()
comisiones = Comisiones()

class DisolverGrupoAhorro:

    def disolver_grupo(self, lista_grupos, lista_usuarios, movimientos):
        while True:
            print(25 * "")
            grupo = seguridad.Login_grupos(lista_grupos)
            if grupo is not None:
                num = int(input("Ingrese el numero de integrantes que había en su grupo"))
                if num == 2:
                    porcentaje = comisiones.comisiones_disvolver_grupo(num, grupo)
                    for _ in range(num):
                        usuario = seguridad.Login(lista_usuarios)
                        cuenta = usuario.obtener_cuenta()
                        cuenta += porcentaje
                        usuario.cuenta = cuenta
                
                        tipo_movimiento = "Disolución de grupo de ahorro"
                        movimientos.registrar_movimiento_usuario(usuario, tipo_movimiento, porcentaje, cuenta - porcentaje, cuenta)

                    lista_grupos.eliminar_grupo(grupo)
                    break

                elif num == 3:
                    porcentaje = comisiones.comisiones_disvolver_grupo(num, grupo)
                    for _ in range(num):
                        usuario = seguridad.Login(lista_usuarios)
                        cuenta = usuario.obtener_cuenta()
                        cuenta += porcentaje
                        usuario.cuenta = cuenta
                        
                        tipo_movimiento = "Disolución de grupo de ahorro"
                        movimientos.registrar_movimiento_usuario(usuario, tipo_movimiento, porcentaje, cuenta - porcentaje, cuenta)

                    lista_grupos.eliminar_grupo(grupo)
                    break
                else:
                    print("Ingrese un valor correcto")
                
            else:
                print("La cuenta del grupo de ahorro que acaba de ingresar no se ha encontrado")



