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


image llaves = im.Scale("images/llaves.png", 150, 150)
screen presentacion_llaves:

    frame:
        xalign 0.5
        yalign 0.5
        padding(20,20)
        add "llaves"

screen barra_progreso():
    frame:
        xalign 0.5
        yalign 0.05
        background Solid("#222222aa")
        padding (15, 10)
        vbox:
            spacing 10
            text "Progreso Shizuka: [barra_progreso['Shizuka']] / 100"
            bar value barra_progreso["Shizuka"] range 100
            text "Progreso Kirisaki: [barra_progreso['Kirisaki']] / 100"
            bar value barra_progreso["Kirisaki"] range 100
            text "Progreso Karen: [barra_progreso['Karen']] / 100"
            bar value barra_progreso["Karen"] range 100
            text "Progreso Marika: [barra_progreso['Marika']] / 100"
            bar value barra_progreso["Marika"] range 100

screen menu_flores():
    frame: 
        xalign 0.5
        yalign 0.5
        hbox:
            spacing 100
            imagebutton:
                idle "rosa" at animacion
                action [Function(aumentar_barra, "Shizuka", 100), Return("Shizuka")]
            imagebutton:
                idle "girasol" at animacion
                action [Function(aumentar_barra, "Karen", 10), Return("Karen")]
            imagebutton:
                idle "margarita" at animacion
                action [Function(aumentar_barra, "Marika", 10), Return("Marika")]
            imagebutton:
                idle "lirio" at animacion
                action [Function(aumentar_barra, "Kirisaki", 10), Return("Kirisaki")]

transform animacion:
    ease 0.5 rotate 15
    ease 0.5 rotate -15
    repeat 

transform agrandar:
    zoom 1.1

screen menu_cosas():
    frame: 
        xalign 0.5
        yalign 0.5
        hbox:
            spacing 100
            imagebutton: 
                idle ""
                action [Function(aumentar_barra, "Shizuka", 10), Return("Shizuka")]

screen dia():
    frame:
        align (0.95, 0.05)
        text "Dia [dia_actual]" color "#FFFFFF"