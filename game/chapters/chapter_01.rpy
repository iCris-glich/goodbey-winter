label capitulo1:

    scene bg invierno at rederisionar with wipeup
    play music "audio/soundtrack/Love Plus [NDS Music] - Silent Night - Aedithy.mp3" fadein 1.0

    "Navidad en Japón es una época muy hermosa y llena de amor."
    "Los jóvenes se declaran y todos están en parejas."

    pause(0.5)

    scene bg desdearriba at rederisionar with dissolve
    play sound "audio/soundtrack/Sonido de gente hablando_sonido ambiente - Girona Studios.mp3"
    "*Murmullos*"
    pause(1.0)
    hide desdearriba with dissolve

    scene bg invierno at rederisionar with dissolve
    "Tokyo es el epicentro de todo este alboroto romántico y navideño."
    hide invierno with dissolve

    pause(2.0)

    "Por eso es increíble que esto esté pasando..."
    stop music fadeout 0.5
    pause(1.0)

    scene bg arboldenavidad at rederisionar with dissolve
    play music "audio/soundtrack/Love Plus [NDS Music] - Les larmes - Aedithy.mp3" fadein 1.5
    pause(0.5)
    scene bg arboldenavidad at desenfoque with dissolve 
    pause(1.5)

    # Escena de confesiones con imágenes blur
    show marikaavergonzada_blur at center with dissolve
    ma "Acepta mis sentimientos..."
    show marikaavergonzada_blur at moverCentroADerecha
    pause(0.5)

    show shizukaavergonzada_blur at center with dissolve 
    sh "Acepta mis sentimientos..."
    show shizukaavergonzada_blur at moverCentroAIzquierda
    pause(1.0)

    # Turnos de diálogo desenfocados
    hide shizukaavergonzada_blur with dissolve 
    show shizukahablandoavergonzada_blur at left with dissolve
    pause(0.3)
    cha1 "Estoy declarando mis sentimientos hacia ti... {w=1}Será mejor que los aceptes... tonto..."
    hide shizukahablandoavergonzada_blur with dissolve 
    show shizukaavergonzada_blur at left with dissolve

    hide marikaavergonzada_blur with dissolve 
    show marikahablandoavergonzada_blur at right with dissolve
    pause(0.3)
    cha2 "Siempre he estado enamorada de ti..."
    hide marikahablandoavergonzada_blur with dissolve 
    show marikaavergonzada_blur at right with dissolve 

    e "Dos chicas preciosas se me declaran... esto no puede ser real."
    e "¿Y ahora que se supone que haga?"
    pause(0.3)

    menu:
        "Aceptar la confesión de la segunda chica":
            $ aumentar_afinidad("Shizuka", 10)
            show screen pantalla_corazones with dissolve
            pause(2.0)
            hide screen pantalla_corazones with fade

            e "Elijo a Shizuka."
            hide shizukaavergonzada_blur with dissolve 
            hide marikaavergonzada_blur with dissolve 
            show shizukafeliz_blur at left with dissolve
            show marikatriste_blur at right with dissolve

        "Aceptar la confesión de la primer chica":
            $ aumentar_afinidad("Marika", 10)
            show screen pantalla_corazones with dissolve
            pause(2.0)
            hide screen pantalla_corazones with fade

            "Elijo a Marika."
            hide marikaavergonzada_blur with dissolve 
            hide shizukaavergonzada_blur with dissolve
            show marikafeliz_blur at right with dissolve
            show shizukatriste_blur at left with dissolve

    e "..."
    pause(0.5)
    e "Me siento mal por rechazar a una..."
    e "Con que así se siente ser popular..."

    pause(0.5)
    if afinidad["Shizuka"] > afinidad["Marika"]:
        hide shizukafeliz_blur with dissolve 
        hide marikatriste_blur with dissolve 
        show shizuka_blur at center with dissolve 
        cha1 "Por cierto... {w=0.5} ¿Cómo te llamas?"
        hide shizuka_blur with dissolve 
        call pedir_nombre
        show shizuka_blur at center with dissolve 
        cha1 "Ah, claro, ya lo recordé. Ese era tu nombre."

    else:
        hide shizukatriste_blur with dissolve 
        hide marikafeliz_blur with dissolve  
        show marika_blur at center with dissolve 
        cha2 "Perdona... {w=0.5} ¿Cuál era tu nombre?"
        hide marika_blur with dissolve 
        call pedir_nombre
        show marika_blur at center with dissolve 
        cha2 "Entonces así te llamabas..."

    cha2 "¡DESPIERTA!"
    pause(0.5)
    cha2 "¡DESPIERTA, [nombre_protagonista]!"

    e "¿Eh?"
    stop music fadeout 1.5

    scene black with fade 
    window hide 

    pause(0.5)
    scene bg clasevacia with fade
    pause(0.5)
    scene black
    pause(0.5)
    scene bg clasevacia
    pause(0.6)
    scene black
    pause(0.5)
    scene bg clasevacia at desenfoque with dissolve

    window show

    play music "audio/soundtrack/Love Plus [NDS Music] - Classroom Scenery - Aedithy.mp3" fadein 0.5

    e "¿Eh...? ¿Dónde estoy?"

    show marika with dissolve
    pause(0.5)
    hide marika with dissolve
    show marikafeliz with dissolve  
    ma "Por fin despiertas..."
    ma "Eres un tonto, ¡te quedaste dormido después de la tercera clase!"
    ma "La maestra Nagisa no pudo despertarte... ¿Qué clase de sueño estabas teniendo?"

    e "¿Un sueño?... Así que todo eso... solo fue mi imaginación."
    hide marikafeliz with dissolve
    show marika with dissolve
    ma "¿Qué estás murmurando tanto...?"

    e "Nada que importe."

    show shizuka with dissolve 
    show marika at moverCentroADerecha
    show shizuka at moverCentroAIzquierda
    pause 1.0
    hide shizuka with dissolve 
    show shizukafeliz at left  with dissolve 
    show marika at inactivo with dissolve

    sh "¡Hola, [nombre_protagonista]! Por fin despiertas."
    sh "Ya tenemos que irnos. Hoy no tengo actividades del club, así que podemos ir a donde quieras."

    hide marika with dissolve
    show marikafeliz at right with dissolve
    show shizukafeliz at inactivo with dissolve 

    ma "¿Y si vamos a comer ramen a ese nuevo puesto del distrito de Fukushima?"

    hide shizukafeliz with dissolve 
    pause(0.3)
    show shizuka at left with dissolve
    pause(0.3)
    hide shizuka with dissolve 
    show shizukafeliz at left  with dissolve  
    ma "¡Sí! ¡Vamos, [nombre_protagonista]!"

    e "Está bien..."
    e "(Aunque sigo pensando en ese sueño... ¿quiénes serían ellas?)"

    scene bg escuela_pasillo with fade
    pause 0.5 
    scene bg escuela_afuera with fade
    pause 0.5
    scene bg calle with fade 
    show shizuka with dissolve 
    sh "¿Dónde quedaba..."
    hide shizuka with dissolve
    show shizukafeliz with dissolve 
    sh "Ah, ya lo vi, ¡por aquí!"
    stop music fadeout 0.5
    pause 0.5

    scene bg restaurante with fade 
    play sound "audio/soundtrack/Sonido de gente hablando_sonido ambiente - Girona Studios.mp3"
    play music "audio/soundtrack/Love Plus [NDS Music] - Holiday (Daylight) - Aedithy.mp3" fadein 1.0
    scene bg restaurante at desenfoque with dissolve
    show marikafeliz with dissolve 
    ma "Nada como el olor a fideos recién hechos... {w=0.5}Rápido, pidamos una mesa."
    scene bg comiendo_restaurante with fade
    e "(Mejor dejo el sueño a un lado por ahora y disfruto el momento.)"

    scene bg calle with fade 
    scene bg calle at desenfoque with dissolve 
    show shizukafeliz with dissolve 
    sh "Nada como un buen plato de ramen."
    sh "Deseo volver a venir, estuvo muy bueno."
    show shizukafeliz at moverCentroADerecha
    pause 1.0
    show marika at left with dissolve 
    show shizukafeliz at inactivo with dissolve 

    ma "A mí no me gustó tanto..."
    show marika at inactivo with dissolve
    hide shizukafeliz with dissolve 
    show shizuka at right with dissolve
    show marika at inactivo with dissolve

    sh "Pero si fuiste tú quien dijo que viniéramos."

    e "Ellas son amigas mías: Shizuka Shirogane, extrovertida y llena de energía..."
    show shizuka at inactivo with dissolve
    show marika at activo with dissolve 
    ma "No hace falta que me lo recuerdes, en internet tenía muy buenas críticas."
    ma "Esos fideos tenían mucha grasa, ¡terminaré engordando así!"

    e "...y Marika, hija del Grupo Tachibana. Inteligente, directa... y con un carácter único."

    ma "¿Tú qué opinas, [nombre_protagonista]?"
    show shizuka at activo with dissolve 
    sh "Sí, ¿te gustaron?"

    menu:
        "Estuvieron ricos":
            $ aumentar_afinidad("Shizuka", 5)
            e "Sí, estuvieron buenos."

        "No, para nada":
            $ aumentar_afinidad("Marika", 5)
            e "No, no me convencieron."

    show screen pantalla_corazones with dissolve 
    pause 1.0
    hide screen pantalla_corazones with fade 
   
    e "(Un momento... ¿es ella?)"

    "Entra en escena alguien más, alguien un poco inesperado."
    stop music fadeout 0.5 
    pause 2.0

    play music "audio/soundtrack/Love Plus [NDS Music] - Les larmes - Aedithy.mp3" fadein 0.5
    show kirisaki with dissolve
    hide kirisaki with dissolve
    show kirisakiinviernoavergonzada with dissolve
    hide kirisakiinviernoavergonzada with dissolve 
    show kirisakiinviernohablandoavergonzada with dissolve   
    cha1 "Hola..."
    hide kirisakiinviernohablandoavergonzada with dissolve 
    show kirisakiinviernoavergonzada with dissolve 
    show kirisakiinviernoavergonzada at inactivo with dissolve 

    hide marika with dissolve 
    show marikatriste at left with dissolve 
    show marikatriste at inactivo with dissolve 
    hide shizuka with dissolve 
    show shizukafeliz at right with dissolve 

    sh "Ah, ¡hola Kirisaki!"
    sh "Llegas tarde, ya terminamos de comer."

    e "Shizuka... ¿tú la invitaste?"

    sh "¡Por supuesto! Quería un reencuentro después de tanto tiempo para los dos."
    show shizukafeliz at inactivo with dissolve 
    show kirisakiinviernoavergonzada at activo with dissolve

    e "(Kirisaki... {w=0.5}mi amiga de la infancia... {w=0.5}y mi ex.)"
    e "(Nuestra historia no es sencilla, pero tampoco necesito revolverla ahora.)"
    
    hide kirisakiinviernoavergonzada with dissolve
    show kirisakiinviernohablandoavergonzada with dissolve 
    ki "Parece que no te alegra verme, ¿no?"
    ki "No importa, vine porque Shizuka me invitó, no por otra razón..."

    hide kirisakiinviernohablandoavergonzada with dissolve 
    show kirisakiinviernoavergonzada with dissolve 
    hide shizukafeliz with dissolve 
    show shizuka at right with dissolve 

    "Shizuka se acerca al oído de Kirisaki y le susurra algo con suavidad."
    sh "Kirisaki, recuerda lo que hablamos..."
    pause(0.7)

    return
