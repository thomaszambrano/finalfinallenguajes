from Seguridad import Seguridad
from Comisiones import Comisiones

comisiones = Comisiones()
seguridad = Seguridad()

class Transacciones:
    def ingresar_dinero(self, lista_usuarios, movimientos):
        usuario = seguridad.Login(lista_usuarios)
        if usuario is not None:
            cuenta = usuario.obtener_cuenta()
            valor = float(input("Ingrese el monto que desea ingresar a su cuenta de ahorros: "))
            comision = comisiones.comision_transacciones(valor)
            valor_con_comision = valor - comision
            saldo_inicial = cuenta
            cuenta += valor_con_comision
            saldo_final = cuenta
            usuario.cuenta = cuenta
            print("Recarga exitosa con comisión del 0.1 aplicada")

            tipo_movimiento = "Consignación a cuenta de ahorro"
            movimientos.registrar_movimiento_usuario(usuario, tipo_movimiento, valor_con_comision, saldo_inicial, saldo_final)
        else: 
            print("El usuario no se ha encontrado, intente de nuevo")

    def ingresar_dinero_grupo(self, lista_grupos, movimientos):
        grupo = seguridad.Login_grupos(lista_grupos)
        if grupo is not None:
            valor = float(input("Ingrese el monto que desea ingresar a su cuenta de grupo de ahorros: "))
            comision = comisiones.comision_transacciones(valor)
            valor_con_comision = valor - comision
            saldo_inicial = grupo.obtener_cuenta()
            grupo.cuenta += valor_con_comision
            saldo_final = grupo.obtener_cuenta()
            print("Recarga exitosa con comisión del 0.1 aplicada")

            tipo_movimiento = "Consignación a cuenta de grupo de ahorro"
            movimientos.registrar_movimiento_grupo(grupo, tipo_movimiento, valor_con_comision, saldo_inicial, saldo_final)
        else: 
            print("El grupo no se ha encontrado, intente de nuevo")

    def sacar_dinero(self, lista_usuarios, movimientos):
        usuario = seguridad.Login(lista_usuarios)
        if usuario is not None:
            cuenta = usuario.obtener_cuenta()
            valor = float(input("Ingrese el monto que desea sacar de su cuenta de ahorros: "))
            comision = comisiones.comision_transacciones(valor)
            valor_con_comision = valor + comision
            if cuenta > 0 and cuenta >= valor_con_comision:
                saldo_inicial = cuenta
                cuenta -= valor_con_comision
                saldo_final = cuenta
                print("Retiro exitoso con comisión del 0.1 aplicada")

                tipo_movimiento = "Retiro de cuenta de ahorro"
                movimientos.registrar_movimiento_usuario(usuario, tipo_movimiento, valor_con_comision, saldo_inicial, saldo_final)
            else:
                print("No hay suficiente saldo en su cuenta de ahorros")
        else: 
            print("El usuario no se ha encontrado, intente de nuevo")

    def sacar_dinero_grupo(self, lista_grupos, movimientos):
        grupo = seguridad.Login_grupos(lista_grupos)
        if grupo is not None:
            valor = float(input("Ingrese el monto que desea sacar de su cuenta de grupo de ahorros: "))
            comision = comisiones.comision_transacciones(valor)
            valor_con_comision = valor + comision
            if grupo.obtener_cuenta() > 0 and grupo.obtener_cuenta() >= valor_con_comision:
                saldo_inicial = grupo.obtener_cuenta()
                grupo.cuenta -= valor_con_comision
                saldo_final = grupo.obtener_cuenta()
                print("Retiro exitoso con comisión del 0.1 aplicada")

                tipo_movimiento = "Retiro de cuenta de grupo de ahorro"
                movimientos.registrar_movimiento_grupo(grupo, tipo_movimiento, valor_con_comision, saldo_inicial, saldo_final)
            else:
                print("No hay suficiente saldo en la cuenta de grupo de ahorros")
        else: 
            print("El grupo no se ha encontrado, intente de nuevo")

    def pagar_deudas_grupo(self, lista_grupos, movimientos):
        grupo = seguridad.Login_grupos(lista_grupos)
        if grupo is not None:
            if grupo.obtener_prestamo() < 0:
                print("No hay deuda que pagar")

            print(f"Deuda de su grupo de ahorro {grupo.obtener_prestamo()} y meses a los que tiene la deuda: {grupo.obtener_meses()}")
            meses = int(input("Ingrese el número de meses que desea pagar: "))
            total_a_pagar, valor_a_pagar = comisiones.calcular_deuda_total(grupo, meses)

            if grupo.obtener_cuenta() >= total_a_pagar:
                print(f"Su deuda a pagar es {total_a_pagar} y su cuenta de ahorros tiene {grupo.obtener_cuenta()} por lo que su cuenta de ahorros quedaría: {grupo.obtener_cuenta() - total_a_pagar}")
                print(25 * "")
                opcion = input("¿Desea continuar? (S/N)")
                print(25 * "")
                if opcion == "S":
                    print("Deuda saldada")
                    grupo.cuenta -= total_a_pagar
                    grupo.prestamo -= valor_a_pagar
                    grupo.meses -= meses

                    saldo_inicial = grupo.obtener_cuenta() + total_a_pagar
                    saldo_final = grupo.obtener_cuenta()
                    tipo_movimiento = "Pago de deuda del grupo de ahorro"
                    movimientos.registrar_movimiento_grupo(grupo, tipo_movimiento, total_a_pagar, saldo_inicial, saldo_final)
            else:
                print("No hay suficiente saldo en su cuenta de grupo de ahorros")
        else: 
            print("El grupo no se ha encontrado, intente de nuevo")
