# ==============================
# DEFINICIONES DE FONDOS
# ==============================

image bg invierno        = "images/backgrounds/calleInvierno.png"
image bg desdearriba     = "images/backgrounds/desdearriba.png"
image bg arboldenavidad  = im.Scale("images/backgrounds/arboldenavidad.png", 1920, 1080)
image bg clasevacia = im.Scale("images/backgrounds/Gemini_Generated_Image_nk5mitnk5mitnk5m.png", 1920, 1080)
image bg escuela_afuera = im.Scale("images/backgrounds/escuela_afuera.png", 1920, 1080)
image bg escuela_pasillo = im.Scale("images/backgrounds/pasillo.png", 1920, 1080)
image bg calle = im.Scale("images/backgrounds/calle.png", 1920, 1080)
image bg restaurante = im.Scale("images/backgrounds/restaurante.png", 1920, 1080)
image bg comiendo_restaurante = im.Scale("images/backgrounds/comiendo_en_el_restaurante.png", 1920, 1080)
image bg akihabara = im.Scale("images/backgrounds/akihabara.png", 1920, 1080)

# ==============================
# SPRITES DE PERSONAJES
# ==============================

# ==============================
# TRANSFORMACIONES
# ==============================

# Reescalado general de backgrounds
transform rederisionar: 
    size (1920, 1080)

# Reescalado general de personajes
transform rederisionarPersonajes:
    linear 0.5 size (800, 900)

# Movimiento de personajes
transform moverCentroAIzquierda:
    xpos 0.5
    linear 1.0 xpos 0.2

transform moverCentroADerecha:
    xpos 0.5
    linear 1.0 xpos 0.8

# Efecto visual de estado activo/inactivo
transform activo: 
    alpha 1.0
    linear 0.3 alpha 1.0

transform inactivo:
    alpha 0.5
    linear 0.3 alpha 0.5

# Desenfoque para fondos
transform desenfoque: 
    blur 10

init python:
    preferences.text_cps = 30  # o la velocidad que quieras (caracteres por segundo)

transform golpe_lateral:
    linear 0.05 xoffset 20
    linear 0.05 xoffset -20
    linear 0.05 xoffset 15
    linear 0.05 xoffset -15
    linear 0.05 xoffset 0
