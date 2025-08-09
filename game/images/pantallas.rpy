image corazon_peq = im.Scale("images/backgrounds/corazon.png", 40, 40)
image corazon_vacio_peq = im.Scale("images/backgrounds/corazon_vacio.png", 40, 40)

transform corazon_anim(index):
    zoom 0.0
    alpha 0.0
    pause 0.15 * index
    linear 0.3 zoom 1.0 alpha 1.0
    pause 0.3
    linear 0.15 zoom 1.2
    linear 0.15 zoom 1.0

define MAX_CORAZONES = 5

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
