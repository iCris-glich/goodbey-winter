screen pantalla_corazones:
    frame:
        xalign 0.5
        yalign 0.1
        background Solid("#000000aa")
        padding (20, 20)

        vbox:
            spacing 15

            text "Afinidad de Shizuka:" style "corazones_text"
            hbox:
                spacing 5
                for i in range(obtener_corazones("Shizuka")):
                    add im.Scale("images/backgrounds/corazon.png", 40, 40)  # ← Cambia el tamaño aquí
            text "Afinidad de Marika:" style "corazones_text"
            hbox:
                spacing 5
                for i in range(obtener_corazones("Marika")):
                    add im.Scale("images/backgrounds/corazon.png", 40, 40)  # ← Cambia el tamaño aquí
style corazones_text:
    color "#ffffff"
    size 24
    font "DejaVuSans.ttf"

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
