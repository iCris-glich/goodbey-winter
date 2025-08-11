default temp_nombre = ""

label pedir_nombre:
    call screen pedir_nombre_screen
    $ nombre_protagonista = temp_nombre.strip()
    if nombre_protagonista == "":
        $ nombre_protagonista = "Makoto"
return
