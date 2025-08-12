label minijuego_sueño:
    
    pause 1.5                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              

    stop music fadeout 1.0 

    pause 1.5

    scene black with fade 

    e "..."

    pause 1.0

    play music "audio/soundtrack/Love Plus [NDS Music] - Afternoon Park - Aedithy.mp3" fadein 0.5
    scene bg arboldenavidad at desenfoque with fade 

    e "¿Ehh?..."
    e "¿Donde estoy?..."

    pause 0.5

    e "Todo se ve familiar... pero me siento raro..."
    e "Es como en ese sueño..."

    pause 0.5 

    cha1 "[nombre_protagonista]..."

    e "¿Quien dijo eso?..."

    cha1 "Fui yo [nombre_protagonista]..."

    "De pronto aparece un misterioso personaje de una chica"
    show diosa at center with dissolve 

    e "¡Eh!"
    e "¿Quien eres?..."
    
    "El misterioso personaje sonrie"
    cha1 "Soy Melisa la Diosa del amor"

    e "Diosa... Ahora... estoy loco..."

    "La Diosa sonrie"
    diosa "No [nombre_protagonista] solo estas durmiendo, en un sueño muy profundo"

    e "Aja..."

    diosa "Bueno voy al grano, estoy aqui para guiarte en tu historia de amor... Con..."

    pause 0.5

    diosa "..."

    hide diosa with dissolve 
    show diosa_soprendida with dissolve 
    
    $ mayor, puntos = personaje_mayor_afinidad()
    diosa "Acaso sera... [mayor]?..."
    
    if cambio_corazones: 
        $ cambio_corazones = False 
        $ eleccion = renpy.call_screen("menu_flores")
    else:
        pass 

    diosa "Ya veo..."

    e "Ehh?..."

    diosa "Cuando terminemos podras ver las respuestas y tu mente se aclarara... sigamos"


    if barra_llena_personaje is not None:
            # Mostrar mensaje o animación de que ganó afinidad
            "¡La barra de [barra_llena_personaje] se llenó!"
            show screen barra_progreso with dissolve 

            hide screen barra_progreso with dissolve 
            $ barra_progreso[barra_llena_personaje] = 0
            $ barra_llena_personaje = None

    show screen pantalla_corazones with dissolve 
    pause 0.5
    hide screen pantalla_corazones with dissolve 

    diosa "[nombre_protagonista] no te preocupes, aqui estoy cada ves que lo necesites... en tus sueños..."
    diosa "Adios [nombre_protagonista]"

    hide diosa_soprendida with dissolve 

    e "Mañana sera otro día..."
    e "..."

    scene black with fade 

    ""
    return 