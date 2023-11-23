class Seguridad:

    def Login_grupos(self, lista_grupos):
        nombre = input("Ingrese el nombre del grupo de ahorro: ")
        contraseña = input("Ingrese la contraseña del grupo de ahorro: ")

        for grupo in lista_grupos.lista_grupos:
            datos_personales = grupo.obtener_datos_personales_grupo()
            nombre_grupo = grupo.obtener_nombre_grupo()
            if nombre_grupo == nombre and datos_personales[2] == contraseña:
                return grupo
        
        return None
    
    def Login(self, lista_usuarios):
        nombre = input("Ingrese el nombre del usuario: ")
        contraseña = input("Ingrese la contraseña del usuario: ")

        for usuario in lista_usuarios.lista_usuarios:
            datos_personales = usuario.obtener_datos_personales()
            if datos_personales[0] == nombre and datos_personales[2] == contraseña:
                return usuario
            
        return None
            
    def solicitar_contraseña(self):
        while True:
            contraseña = input("Ingrese la contraseña: ")
            vefcontraseña = input("Ingrese la contraseña(verificación): ")

            if contraseña == vefcontraseña:
                return contraseña
            else:
                print("La verificación de la contraseña no coincide. Vuelva a intentar.")
                print(25 * "")
