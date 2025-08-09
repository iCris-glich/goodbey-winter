# 0_afinidades.rpy
# ================================
# VARIABLES GLOBALES DE AFINIDAD
# ================================

default afinidad = {
    "Shizuka": 0,
    "Marika": 0,
    "Kirisaki": 0,
    "Karen": 0
}

default corazones = {
    "Shizuka": 0,
    "Marika": 0,
    "Kirisaki": 0,
    "Karen": 0
}

default ultimo_cambio_chica = None  # Rastrea la última chica con aumento de afinidad

# ================================
# FUNCIONES DE AFINIDAD
# ================================

init python:
    def set_afinidad(nombre, puntos):
        """Establece una afinidad exacta para un personaje"""
        if nombre in afinidad:
            afinidad[nombre] = puntos
            actualizar_corazones()

    def aumentar_afinidad(nombre, puntos):
        """Aumenta la afinidad de un personaje"""
        global ultimo_cambio_chica
        if nombre in afinidad:
            afinidad[nombre] += puntos
            ultimo_cambio_chica = nombre  # Priorizar aumentos
            actualizar_corazones()

    def reducir_afinidad(nombre, puntos):
        """Reduce la afinidad de un personaje"""
        if nombre in afinidad:
            afinidad[nombre] = max(0, afinidad[nombre] - puntos)
            # No actualizamos ultimo_cambio_chica para priorizar aumentos
            actualizar_corazones()

    def actualizar_corazones():
        """Convierte los puntos de afinidad en corazones"""
        for personaje in afinidad:
            corazones[personaje] = afinidad[personaje] // 10  # 1 corazón cada 10 puntos

    def obtener_afinidad(nombre):
        """Devuelve la afinidad actual de un personaje"""
        return afinidad.get(nombre, 0)

    def obtener_corazones(nombre):
        """Devuelve los corazones actuales de un personaje"""
        return corazones.get(nombre, 0)