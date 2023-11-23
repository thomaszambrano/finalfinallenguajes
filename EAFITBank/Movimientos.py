from datetime import datetime
from Seguridad import Seguridad

seguridad = Seguridad()


class Movimientos:
    def __init__(self):
        self.movimientos_usuarios = {}
        self.movimientos_grupos = {}

    def registrar_movimiento_grupo(self, grupo, tipo_movimiento, monto, saldo_inicial, saldo_final):
        now = datetime.now()
        movimiento = {
            "fecha": now.strftime("%Y-%m-%d"),
            "hora": now.strftime("%H:%M:%S"),
            "tipo_movimiento": tipo_movimiento,
            "monto": monto,
            "saldo_inicial": saldo_inicial,
            "saldo_final": saldo_final
        }

        if grupo in self.movimientos_grupos:
            self.movimientos_grupos[grupo].append(movimiento)
        else:
            self.movimientos_grupos[grupo] = [movimiento]

    def registrar_movimiento_usuario(self, usuario, tipo_movimiento, monto, saldo_inicial, saldo_final):
        now = datetime.now()
        movimiento = {
            "fecha": now.strftime("%Y-%m-%d"),
            "hora": now.strftime("%H:%M:%S"),
            "tipo_movimiento": tipo_movimiento,
            "monto": monto,
            "saldo_inicial": saldo_inicial,
            "saldo_final": saldo_final
        }

        if usuario in self.movimientos_usuarios:
            self.movimientos_usuarios[usuario].append(movimiento)
        else:
            self.movimientos_usuarios[usuario] = [movimiento]

    def imprimir_movimientos_usuario(self, lista_usuarios):
        usuario = seguridad.Login(lista_usuarios)
        if usuario is not None:
            if usuario in self.movimientos_usuarios:
                print(f"Registro de movimientos para el usuario {usuario.obtener_datos_personales()[0]}:")
                for movimiento in self.movimientos_usuarios[usuario]:
                    self.mostrar_movimiento(movimiento)
            else:
                print("No hay movimientos registrados para este usuario.")
        else:
            print("El usuario no se ha encontrado, intente de nuevo")

    def imprimir_movimientos_grupo(self, lista_grupos):
        grupo = seguridad.Login_grupos(lista_grupos)
        if grupo is not None:
            if grupo in self.movimientos_grupos:
                nombre_grupo = grupo.obtener_nombre_grupo()
                print(f"Registro de movimientos para el grupo {nombre_grupo}:")
                for movimiento in self.movimientos_grupos[grupo]:
                    self.mostrar_movimiento(movimiento)
            else:
                print("No hay movimientos registrados para este grupo.")
        else:
            print("El grupo no se ha encontrado, intente de nuevo")

    def mostrar_movimiento(self, movimiento):
        print("Fecha:", movimiento["fecha"])
        print("Hora:", movimiento["hora"])
        print("Tipo de movimiento:", movimiento["tipo_movimiento"])
        print("Monto:", movimiento["monto"])
        print("Saldo inicial:", movimiento["saldo_inicial"])
        print("Saldo final:", movimiento["saldo_final"])
        print(25 * "-")
