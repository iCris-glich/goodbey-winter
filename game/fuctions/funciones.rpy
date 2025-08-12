default temp_nombre = ""

label pedir_nombre:
    call screen pedir_nombre_screen
    $ nombre_protagonista = temp_nombre.strip()
    if nombre_protagonista == "":
        $ nombre_protagonista = "Makoto"
return

default barra_progreso = {
    "Shizuka": 0, 
    "Marika": 0, 
    "Kirisaki": 0, 
    "Karen": 0
}        

default barra_llena_personaje = None
    
init python:
    def aumentar_barra(nombre, puntos):
        global barra_progreso, barra_llena_personaje
        if barra_llena_personaje is not None:
            # Si ya hay una barra llena esperando reinicio, no aumentamos otra
            return

        if nombre in barra_progreso:
            barra_progreso[nombre] += puntos

            if barra_progreso[nombre] >= 100:
                aumentar_afinidad(nombre, 10)
                barra_progreso[nombre] = 100
                barra_llena_personaje = nombre


init python:
    def personaje_mayor_afinidad():
        max_personaje = None 
        max_puntos = -1

        for personaje, puntos in afinidad.items():
            if puntos > max_puntos:
                max_puntos = puntos
                max_personaje = personaje
        
        return max_personaje, max_puntos