label capitulo1:

    scene bg invierno at rederisionar with wipeup
    play music "audio/soundtrack/Love Plus [NDS Music] - Silent Night - Aedithy.mp3" fadein 1.0
    play sound "audio/soundtrack/Sonido de gente hablando_sonido ambiente - Girona Studios.mp3"
    "*Murmullos*"

    "Navidad en Japón es una época muy hermosa y llena de amor."
    "Los jóvenes se declaran y todos están en parejas."

    pause(0.5)

    scene bg desdearriba at rederisionar with dissolve
    play sound "audio/effects/El ruido - Calle.mp3"
    "Los autos pasan de forma rutinaria"
    pause(1.0)
    hide desdearriba with dissolve

    scene bg invierno at rederisionar with dissolve
    "Tokyo es el epicentro de todo este alboroto romántico y navideño."
    hide invierno with dissolve

    pause(0.5)

    "Por eso es increíble que esto esté pasando..."
    stop sound 
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

    e "¿Ehh?..."

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

    pause(0.5)
    cha2 "¡DESPIERTA, [nombre_protagonista]!"

    e "¿Eh?"
    stop music fadeout 1.5

    scene black with fade 
    window hide 
    scene black with fade
    pause(0.6)
    scene bg clasevacia with fade
    pause(0.3)
    scene black with fade
    pause(0.3)
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

    ma "Tienes una mirada perdida... Como la de un pervertido..."

    e "Hey mide tus palabras."

    ma "No me digas que hacer pervertido"

    "Marika retrocede un poco, se esta tomando muy real esto."

    show shizuka with dissolve 
    show marika at moverCentroADerecha
    show shizuka at moverCentroAIzquierda
    pause 1.0
    hide shizuka with dissolve 
    show shizukafeliz at left  with dissolve 
    show marika at inactivo with dissolve

    sh "¡Hey, Hey!, veo que se divierten sin la gran Shizuka"
    sh "JA JA JA"

    "Shizuka voltea para verte"

    sh "¡Hola, [nombre_protagonista]! Por fin despiertas."
    sh "Dormites mucho en clases, estabas soñando acaso con..."
    sh "{cps=5}Conmigo..."
    "Shizuka se rie levemente"

    e "Deja de bromear así quieres."

    "Levantas tu brazo para darle un leve golpe a Shizuka en la cabeza."
    play sound "audio/effects/golpe.mp3"
    pause 0.5

    show shizukafeliz at golpe_lateral
    sh "JI JI JI"
    sh "Pero tienes suerte [nombre_protagonista] hoy suspendieron las actividades del club."
    sh "¡Tengo toda la tarde libre!"

    hide marika with dissolve
    show marikafeliz at right with dissolve
    show shizukafeliz at inactivo with dissolve 

    ma "Como soy tan buena propondre algo."
    ma "¿Y si vamos a comer ramen a ese nuevo puesto en Akihabara?"
    ma "He escuchado que es muy bueno"

    hide shizukafeliz with dissolve 
    pause(0.3)
    show shizuka at left with dissolve
    pause(0.3)
    hide shizuka with dissolve 
    show shizukafeliz at left  with dissolve  
    sh "¡Sí! ¡Buena idea Marika, [nombre_protagonista] vamos!"

    e "Está bien..."
    e "(Aunque sigo pensando en ese sueño... ¿quiénes serían ellas?)"
    e "(Me parecian familiares esos rostros, como si ya los hubiera visto.)"

    scene bg escuela_pasillo with fade
    pause 0.5 
    scene bg escuela_afuera with fade
    pause 0.5
    scene bg akihabara with fade 
    show shizuka with dissolve 
    sh "¿Dónde quedaba..."
    hide shizuka with dissolve
    show shizukafeliz with dissolve 
    sh "Ah, ya lo vi, ¡por aquí!"
    stop music fadeout 0.5
    pause 0.5

    scene bg restaurante with fade 
    play sound "audio/soundtrack/Sonido de gente hablando_sonido ambiente - Girona Studios.mp3"
    play music "audio/soundtrack/Love Plus [NDS Music] - Holiday (Daylight) - Aedithy.mp3" fadein 0.5
    scene bg restaurante at desenfoque with dissolve
    show marikafeliz with dissolve 
    ma "Nada como el olor a fideos recién hechos... {w=0.5}Rápido, pidamos una mesa."
    scene bg comiendo_restaurante with fade
    e "(Mejor dejo el sueño a un lado por ahora y disfruto el momento.)"

    scene bg restaurante with fade 
    scene bg restaurante at desenfoque with dissolve 
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

    show shizuka at inactivo with dissolve
    show marika at activo with dissolve 
    
    ma "No hace falta que me lo recuerdes, en internet tenía muy buenas críticas."
    ma "Esos fideos tenían mucha grasa, ¡terminaré engordando así!"
    pause 0.3
    ma "¿Tú qué opinas, [nombre_protagonista]?"

    show shizuka at activo with dissolve 
    sh "Sí, ¿te gustaron?"

    menu:
        "Estuvieron ricos":
            $ aumentar_afinidad("Shizuka", 2)
            e "Sí, estuvieron buenos."

        "No, para nada":
            $ aumentar_afinidad("Marika", 2)
            e "No, no me convencieron."

    show screen pantalla_corazones with dissolve 
    pause 1.0
    hide screen pantalla_corazones with fade 
   
    e "(Ya me siento mas relajado)"
    "Alzas la mirada solo por curiosidad para ver el lugar"    
    e "(Un momento... ¿es ella?)"
    "Ves un rostro familiarSs"

    "Entra en escena alguien más, alguien un poco inesperado."
    stop music fadeout 0.5 
    pause 1.5

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

    "La expresion de Marika cambio"

    show marikatriste at inactivo with dissolve 
    hide shizuka with dissolve 
    show shizukafeliz at right with dissolve 

    sh "Ah, ¡hola Kirisaki!"
    sh "Llegas tarde, ya terminamos de comer."

    e "Shizuka... ¿tú la invitaste?"

    sh "¡Por supuesto! Quería un reencuentro después de tanto tiempo para los dos."
    show shizukafeliz at inactivo with dissolve 
    show kirisakiinviernoavergonzada at activo with dissolve

    e "(Kirisaki... {w=0.5}mi amiga de la infancia...)"
    e "(Nuestra historia no es sencilla, pero tampoco necesito revolverla ahora.)"
    
    hide kirisakiinviernoavergonzada with dissolve
    show kirisakiinviernohablandoavergonzada with dissolve 
    ki "Parece que no te alegra verme, ¿no?"
    ki "No importa, vine porque Shizuka me invitó, no por otra razón..."

    hide kirisakiinviernohablandoavergonzada with dissolve 
    show kirisakiinviernoavergonzada with dissolve

    "El aire se siente un poco tenso desde la llegada de Kirisaki"

    hide shizukafeliz with dissolve 
    show shizuka at right with dissolve 

    "Shizuka se acerca al oído de Kirisaki y le susurra algo con suavidad."
    sh "Kirisaki, recuerda lo que hablamos..."
    show marikatriste 
    "Kiriskai voltea para ver a Shizuka y acienta con la cabeza"
    "Kirisaki un poco nerviosa toma asiento en silencio"
    ki "C-con permiso..."

    e "(Esto es como un sueño... Rodeado de chicas... {w=0.5}O una pesadilla.)"
    e "(Ahora que veo mejor la escena la expresión de Marika cambio desde que llego Kirisaki.)"
    hide shizuka with dissolve 
    show shizukafeliz at right with dissolve 
    sh "Pasemos todos un buen rato desde ahora."
    
    show shizukafeliz at inactivo with dissolve
    show kirisakiinviernoavergonzada at inactivo with dissolve 
    show marikatriste at activo with dissolve 
    ma "Si..."
    pause(0.5)

    scene black with fade 

    "Depues de ese momento todos estuvieron tranquilos hasta que llego la hora de irse."
    
    scene bg akihabara with fade 

    show shizukafeliz with dissolve 
    sh "Estuvo muy buena la comida, pero ya devo irme a casa"
    hide shizukafeliz with dissolve 
    
    show marika with dissolve 
    ma "Yo me quedare, tengo algunas cosas que hacer"
    hide marika with dissolve

    show kirisaki with dissolve 
    ki "Igual tengo que irme a casa, espero llegar a tiempo tomar el ultimo metro"
    hide kirisaki with dissolve 

    show shizukafeliz with dissolve 
    sh "Tu ¿Que haras [nombre_protagonista]?"

    show shizukafeliz at inactivo with dissolve 
    menu: 
        "Acompañar a Shizuka a su casa":
            e "Te acompaño, Shizuka."
            $ aumentar_afinidad("Shizuka", 5)
            $ reducir_afinidad("Marika", 5)
            $ reducir_afinidad("Kirisaki", 15)
            show screen pantalla_corazones with dissolve
            pause 1.0
            hide screen pantalla_corazones with fade
            e "(Tal vez con Shizuka pueda entender qué significaba ese sueño tan vívido...)"

        "Acompañar a Marika con sus mandados":
            e "Voy contigo, Marika."
            $ aumentar_afinidad("Marika", 5)
            $ reducir_afinidad("Kirisaki", 15)
            show screen pantalla_corazones with dissolve
            pause 1.0
            hide screen pantalla_corazones with fade
            e "(Quizás Marika me ayude a aclarar mis pensamientos revueltos...)"

        "Acompañar a Kirisaki al metro":
            e "Quieres que te acompañe, Kirisaki..."
            $ aumentar_afinidad("Kirisaki", 15)
            $ reducir_afinidad("Marika", 5)
            show screen pantalla_corazones with dissolve
            pause 1.0
            hide screen pantalla_corazones with fade
            e "(Aun me preocupo por ella... Vive muy lejos de aquí.)"

        "Irte por tu cuenta":
            e "Iré a mi casa por mi cuenta."
            e "(Necesito tiempo para pensar en ese sueño... y en Kirisaki.)"
        # No mostramos pantalla_corazones porque no hay cambios de afinidad

    ""
return
