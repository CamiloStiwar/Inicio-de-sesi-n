maxIntentos = 3
storedPassword = "123abc"

contraseña = input("Digite su contraseña: ")

contador = 0

while storedPassword != contraseña and maxIntentos > contador:
    print("Error, las contraseñas no coinciden")
    contador = contador + 1
    contraseña = input("Por favor digite nuevamente la contraseña: ")

if contador >= maxIntentos:
    print("Te equivocaste más de 3 veces, te hemos bloqueado")

else:
    print("Inicio de sesión exitoso")
