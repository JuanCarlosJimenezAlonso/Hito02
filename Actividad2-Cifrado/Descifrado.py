#Este script te descifra textos, puede ser usado para descifrar contraseñas.
#----------------------CIFRADO-----------------------------
texto = input("Tu texto: ")
digitos= "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz0123456789"
k = int(input("Valor de desplazamiento: "))
cifrado = ""
for c in texto:
    if c in digitos:
        cifrado += digitos[(digitos.index(c) + k) % len(digitos)]
    else:
        cifrado += c
print("Texto cifrado: ",cifrado)

#----------------------DESCIFRADO-----------------------------
texto = input("Mensaje: ")
letras="ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz0123456789"
for key in range(len(letras)):
    traduccion=""
    for elem in texto:
        if elem in letras:
            elemIndex = letras.find(elem)
            tradIndex = elemIndex - key
            if tradIndex<0:
                tradIndex = tradIndex + len(letras)
            traduccion = traduccion + letras[tradIndex]
        else:
            traduccion = traduccion + elem
        print("key #%s: %s" % (key, traduccion))