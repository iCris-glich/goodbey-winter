label lobby:
    scene bg casa_noche with dissolve 
    window hide
    # Guardar estado previo de corazones
    $ corazones_antes = corazones.copy()
    play music "audio/soundtrack/Love Plus [NDS Music] - Holiday (Daylight) - Aedithy.mp3"

    pause 1.0
    call screen lobby_menu
    return 

screen lobby_menu():
    tag menu

    add im.Scale("images/backgrounds/cuarto.png", 1920, 1080)

    frame:
        style "lobby_frame"
        xalign 0.2
        yalign 0.5
        has vbox
        spacing 30

        textbutton "Dormir" action Jump("minijuego_sueño") style "lobby_button" at hover_scale
        textbutton "Revisar progreso" action Show("revisar_progreso", transition=dissolve) style "lobby_button" at hover_scale
        textbutton "Guardar partida" action ShowMenu("save") style "lobby_button" at hover_scale
        textbutton "Salir del juego" action Return() style "lobby_button" at hover_scale

style lobby_frame:
    background Solid("#00000080")  # negro con 50% opacidad
    xminimum 520
    yminimum 450
    padding (40, 40)

style lobby_button:
    background "#66000088"  # semitransparente rojo oscuro
    padding (20, 15)
    font "fonts/SomeFont.ttf"
    hover_background "#aa0000"
    hover_foreground "#537c9750"
    insensitive_background "#444444"
    insensitive_foreground "#999999"
    xminimum 400
    yminimum 60
    text_align 0.5

transform hover_scale:
    on hover:
        linear 0.15 zoom 1.05
    on idle:
        linear 0.15 zoom 1.0

