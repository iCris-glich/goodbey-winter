image corazon_peq = im.Scale("images/corazon.png", 40, 40)
image corazon_vacio_peq = im.Scale("images/corazon_vacio.png", 40, 40)

transform corazon_anim(index):
    zoom 0.0
    alpha 0.0
    pause 0.15 * index
    linear 0.3 zoom 1.0 alpha 1.0
    pause 0.3
    linear 0.15 zoom 1.2
    linear 0.15 zoom 1.0

define MAX_CORAZONES = 10

screen pantalla_corazones:
    frame:
        xalign 0.5
        yalign 0.1
        background Solid("#000000aa")
        padding (20, 20)

        vbox:
            spacing 15

            if ultimo_cambio_chica is not None:
                text "Afinidad de [ultimo_cambio_chica]:" style "corazones_text"
                hbox:
                    spacing 5
                    $ corazones_actuales = obtener_corazones(ultimo_cambio_chica)
                    for i in range(MAX_CORAZONES):
                        if i < corazones_actuales:
                            add "corazon_peq" at corazon_anim(i)
                        else:
                            add "corazon_vacio_peq"

style corazones_text:
    color "#ff69b4"
    size 28
    font "DejaVuSans.ttf"
    outlines [(2, "#000000", 0, 0)]

screen pedir_nombre_screen():

    modal True

    frame:
        xalign 0.5
        yalign 0.5
        background Solid("#00000080")
        padding (30, 20)

        vbox:
            spacing 15
            text "¿Cómo te llamas?" size 35 color "#ffffff" xalign 0.5

            input value VariableInputValue("temp_nombre") length 20 color "#ffffff" size 28 xalign 0.5

            textbutton "Aceptar":
                xalign 0.5
                action Return()

screen lobby_menu():
    tag menu

    add im.Scale("images/backgrounds/cuarto.png", 1920, 1080)

    frame:
        style "lobby_frame"
        xalign 0.5
        yalign 0.5
        has vbox
        spacing 30

        textbutton "Dormir" action Jump("avanzar_día") style "lobby_button" at hover_scale
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


image llaves = im.Scale("images/llaves.png", 150, 150)
screen presentacion_llaves:

    frame:
        xalign 0.5
        yalign 0.5
        padding(20,20)
        add "llaves"

