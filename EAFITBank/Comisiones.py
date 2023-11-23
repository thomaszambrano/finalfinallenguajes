from Seguridad import *
import Seguridad
class Comisiones:

    def calcular_deuda_total(self, grupo, meses):
        deuda_actual = grupo.obtener_prestamo()
        if deuda_actual > 0:
            valor_por_mes = deuda_actual / grupo.obtener_meses()
            valor_a_pagar = valor_por_mes * meses
            intereses = valor_a_pagar * (3 / 100) * meses
            total_a_pagar = valor_a_pagar + intereses
            return total_a_pagar, valor_a_pagar
    
    def comision_transacciones(self, valor_transaccion):
        comision = valor_transaccion * 0.001  # 0.1% = 0.001
        return comision
    

    def comisiones_disvolver_grupo(self, num_personas, grupo):
        total_fondos = grupo.obtener_cuenta() 

        comision_banco = total_fondos * 0.05  
        fondos_restantes = total_fondos - comision_banco


        monto_por_persona = fondos_restantes / num_personas
        
        return monto_por_persona

    def comision_prestamo_grupo_usuario_repetido(self, lista_usuarios, lista_grupos, movimientos):
        usuario = Seguridad.Login(lista_usuarios)
        if usuario is not None:
            grupo = Seguridad.Login_grupos(lista_grupos)
            if grupo is not None:
                if usuario in grupo.obtener_usuarios():
                    valor = float(input("Ingrese el monto que desea prestar: "))
                    if grupo.obtener_cuenta() >= valor:
                        saldo_inicial = grupo.obtener_cuenta()
                        grupo.cuenta -= valor*0.05
                        saldo_final = grupo.obtener_cuenta()
                        print("Préstamo exitoso")

                        tipo_movimiento = "Préstamo a otro grupo de ahorro"
                        movimientos.registrar_movimiento_grupo(grupo, tipo_movimiento, valor, saldo_inicial, saldo_final)
                    else:
                        print("No hay suficiente saldo en la cuenta de grupo de ahorros")
            else:
                print("El grupo no se ha encontrado, intente de nuevo")
        else:
            print("El usuario no se ha encontrado, intente de nuevo")