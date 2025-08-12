default imagenes_persoonajes = {
    "Shizuka" : "images/characters/shizuka/shizuka.png",
    "Marika" : "images/characters/marika/marika.png",
    "Kirisaki": "images/characters/kirisaki/kirisaki-Photoroom.png",
    "Karen" : "images/characters/karen/karen.png"
}

style nombre_personaje:
    size 28
    color "#FFD700"  # dorado
    bold True
    outlines [(2, "#000000", 0, 0)]

style puntos_afinidad:
    size 22
    color "#FFFFFF"
    outlines [(1, "#000000", 0, 0)]

style corazones:
    size 24
    color "#FF4444"

style style_progreso:
    background Solid("#000000C0")
    padding (40, 40)
    xminimum 800
    yminimum 600
    drop_shadow [2, 2, 5, "#00000080"]


screen revisar_progreso():
    modal True
    
    frame:
        style "style_progreso"
        xalign 0.5
        yalign 0.5

        vbox:
            spacing 20
            text "Progreso" size 40

            for personaje in afinidad:
                if afinidad[personaje] > 0:
                    frame:
                        background Solid("#22222280")
                        xminimum 600
                        yminimum 160
                        xpadding 15
                        ypadding 15

                        hbox:
                            spacing 15
                            
                            frame:
                                background Solid("#444444")
                                xpadding 5
                                ypadding 5
                                add imagenes_persoonajes[personaje] size (80, 120)
                            
                            vbox:
                                spacing 5
                                text "[personaje]:" style "nombre_personaje"
                                text "[afinidad[personaje]] pts" style "puntos_afinidad"
                                bar range 100 value afinidad[personaje] xminimum 600
                                text "❤️ [corazones[personaje]]" style "corazones"

            textbutton "Cerrar" action Hide("revisar_progreso", transition=dissolve) xalign 0.5:
                padding (10, 8)
                hover_background "#FF7777"
                xminimum 120
                yminimum 40
