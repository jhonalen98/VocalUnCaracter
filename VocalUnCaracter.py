Letra = input("Ingrese una letra: ")

if len(Letra) > 1:
        print("Sólo debe ingresar una letra.")
elif Letra.lower() in 'aeiou':
        print("Es vocal.")
else:
        print("No es vocal.")