label seguir_a_shizuka:

    
    show shizukafeliz with dissolve 

    sh "Entonces quieres venir conmigo, ¿ves que sí te gusto?"

    e "Solo vamos, quiero pensar en algunas cosas durante el camino."

    "Ambos se alejan del grupo rumbo a la estación del tren."

    scene bg calle with fade 

    show shizuka with dissolve 

    "En el camino, Shizuka muestra intriga sobre lo que pasó entre Kirisaki y tú."

    sh "Oye, [nombre_protagonista], ¿puedo preguntarte algo?"

    e "*Suspiras*"
    e "Sé lo que vas a preguntar, así que adelante... después de todo evitarlo solo despertara tu curiosidad."

    sh "¿Odias a Kirisaki?"

    pause 0.5

    e "No, no la odio."

    sh "Tengo entendido que es tu mejor amiga."
    sh "Pero en el restaurante no parecía que fueran tan cercanas."

    e "Nuestra historia es un poco enredada."

    pause 0.5

    sh "Pues... sí, sobre eso... Sé que ella y tú..."

    "Shizuka se siente un poco avergonzada y tan distraída que golpeó un poste con la cara."
    play sound "audio/effects/golpe.mp3"
    pause 1.0
    show shizuka at golpe_lateral

    sh "¡Auch!"

    e "Eres algo torpe."
    e "Quédate ahí, te ayudaré."

    "Te agachas para ayudarla."

    scene bg golpe_shizuka with fade

    e "Hey, ten más cuidado, mira que te saldrá un chichón en la cabeza."

    sh "Soy una cabeza dura."
    sh "{cps=2}JA JA JA"

    "Ayudas a levantar a Shizuka."

    scene bg calle with fade

    e "¿Segura que estás bien?"

    show shizukahablandoavergonzada with dissolve 

    sh "Sí, ya falta poco para llegar a la estación."

    "La expresión de Shizuka cambió un poco, de estar alegre a pensativa."

    "Se acercan a la estación del tren."

    e "Mira, ya llegamos a la estación."

    sh "Ah... sí..."

    stop music

    scene bg estacion_tren with fade
    pause 1.0
    play music "audio/soundtrack/Love Plus [NDS Music] - Mountain Scenery - Aedithy.mp3" fadein 0.5

    e "..."

    show shizuka with dissolve 

    sh "Sabes... Inivite a Kirisaki a comer con nosotros por que crei que te gustaria verla otra vez."
    sh "Tal vez fue tonto de mi parte hacerlo."

    e "..."

    "Levantas tu brazo para darle un golpe en la frente."
    play sound "audio/effects/golpe.mp3" 
    show shizuka at golpe_lateral 

    sh "¡Ay! mi frente"

    e "Cambia esa cara larga quieres, no te preocupes por eso."

    sh "¿En serio?"

    pause 0.3

    e "Si."

    pause 0.5

    sh "..."
    sh "Eres un tonto por hacerme preocupar asi."
    sh "!TONTO!"

    "Shizuka recobra la sonrisa de siempre."
    show shizukafeliz with dissolve 

    "Sonríes levemente."

    "Llega el tren a la estación, puntual como siempre."
    play sound "audio/effects/sonido de tren con su bocina - pedro chamay sanchez.mp3"

    sh "¡Ah!, tengo que tomar el tren."
    sh "Hablamos mañana, [nombre_protagonista]."

    pause 2.0

    jump lobby
    return



label seguir_a_marika:

    show marikafeliz with dissolve 

    ma "Bueno veo que quieres seguirme, no te culpo."
    
    "La expresion de marika cambio"
    show marika with dissolve 
    
    ma "Pero debo negarme, ya que deseo estar sola un momento, pero gracias."

    e "¿Eh?"

    ma "Adios"
    
    hide marika with dissolve
    hide marikafeliz with dissolve  

    "Marika se despide mientras se aleja del lugar."

    e "No era la respuesta que esperaba."

    jump lobby
    return 



label seguir_a_kirisaki:

    show kirisakiinviernoavergonzada with dissolve
    
    ki "Em... No lo se..." 
    
    e "Vives lejos de aqui y en el metro siempre hay gente rara."
    e "Es lo menos que puedo hacer."

    "Kirisaki lo piensa de forma intensa."
    pause 1.5

    ki "Esta bien..."
    ki "Pero no creas que es por otra cosa"

    e "Esta bien no te preocupes."

    "Se alejan del grupo rumbo a la estacion"

    scene bg calle with fade

    "Depues de un rato de caminar."
    "Kirisaki no te ha dirigido la palabra desde que le propusiste acompañarla."

    e "Kirisaki..."

    show kirisakiinviernohablandoavergonzada with dissolve 

    ki "¡Si!"

    "Kirisaki esta sorprendida y algo nerviosa, a de ser por estar cerca de ti."

    e "Eh, no solo quiero saber si estas bien."
    e "No hemos hablando desde, bueno ese día."

    ki "{cps=5}Bueno... Si..."
    ki "Estoy bien no te preocupes, ya no soy como antes y no necesito ayuda."

    "Suelta una pequeña sonrisa"
    hide kirisakiinviernohablandoavergonzada with dissolve 
    show kirisaki with dissolve 
    "Correspondes a la pequeña sonrisa."

    e "Eso me alegra oirlo sabes."

    "Despues de un rato caminando llegan a la estacion."

    scene bg estacion_metro with dissolve 

    show kirisaki with dissolve 

    ki "Desde aquí puedo irme por mi cuenta."
    ki "Gracias por acompañarme [nombre_protagonista]"

    hide kirisaki with dissolve 

    "Kirisaki empieza a alejarse."
    "Pero deja caer algo al suelo."

    pause 0.5           

    "Son sus llaves"

    e "Siempre haz sido muy distraida Kirisaki."

    show screen presentacion_llaves with dissolve 
    pause 0.5
    hide screen presentacion_llaves with dissolve
    "Recoges las llaves para luego buscarla entre la multitud."
    play sound "game/audio/effects/El ruido - Calle.mp3" 

    pause 0.5 

    "Depues de un rato logras encontrala pero esta junto a unos tipos raros."

    scene bg kirisaki_intimidada_metro at sacudida 

    "¿Hola linda estas sola?"

    "Kirisaki esta asustada, se ve en su cuerpo contraido y mirada asustada."
    
    "Sin pensarlo te abalanzas para ayudarla"

    scene bg protegiendo_kirisaki at sacudida

    e "¡¿...?!"

    ki "[nombre_protagonista]"

    "La mirada intimidada de Kirisaki se ilumina cuando te ve llegar"

    "Ugh... ni te creas el heroe idiota."
    "Los tipos de se van de la escena "

    scene bg estacion_metro with dissolve 

    show kirisakiinviernoavergonzada with dissolve 
    ki "[nombre_protagonista] gracias por llegar."

    "Kirisaki tienen la mirada vidriosa casi como si llorara"

    e "¿Esta bien?" 

    ki "Si..."
    ki "Ellos llegaron y me sorprendieron, tenia que haberme alejado de ellos"
    
    e "Ya todo paso, lo importante esque llegue a tiempo."
    e "Te seguí para darte tus llaves."


    "Le das las llaves a Kirisaki"

    hide kirisakiinviernohablandoavergonzada with dissolve 
    show kirisakiinviernoavergonzada with dissolve 

    ki "Creo que quede como una tonta despues de que lo dije."
    ki "Y no quiero ser mas asi... Cambiare."

    pause 0.5

    ki "Tengo que irme ya nos vemos."
    hide kirisakiinviernoavergonzada with dissolve 

    "Kirisaki se despide y toma el metro rumbo a su casa."
    play sound "audio/effects/sonido de tren con su bocina - pedro chamay sanchez.mp3"

    e "..."

    stop sound

    pause 0.5
    jump lobby
    return 