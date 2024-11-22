tema = input("Ingrese el tema del cuestionario: ")

preguntas = {
    "historia": [
        {"pregunta": "¿Quién fue el primer presidente de México?", "opciones": ["Benito Juárez", "Miguel Hidalgo", "José María Morelos"], "respuesta": 0},
        {"pregunta": "¿En qué año se independizó México?", "opciones": ["1810", "1821", "1910"], "respuesta": 1},
        {"pregunta": "¿Quién fue el líder del movimiento de independencia?", "opciones": ["Miguel Hidalgo", "José María Morelos", "Emiliano Zapata"], "respuesta": 0}
    ],
    "fisica" or "física": [
        {"pregunta": "¿Cuál es el planeta más grande del sistema solar?", "opciones": ["Júpiter", "Saturno", "Urano"], "respuesta": 0},
        {"pregunta": "¿Cuál es la fórmula de la energía cinética?", "opciones": ["E = mc^2", "E = 1/2 mv^2", "E = mgh"], "respuesta": 1},
        {"pregunta": "¿Quién descubrió la gravedad?", "opciones": ["Isaac Newton", "Galileo Galilei", "Albert Einstein"], "respuesta": 0}
    ],
    "matematicas" or "matemáticas": [
        {"pregunta": "¿Cuál es la raíz cuadrada de 16?", "opciones": ["2", "4", "8"], "respuesta": 1},
        {"pregunta": "¿Cuanto?"}
    ]
}

import pygame
import sys

pygame.init()

ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Cuestionario")

fuente = pygame.font.SysFont("Arial", 24)

pregunta_actual = 0
puntuacion = 0

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if pregunta_actual < len(preguntas[tema]):
                respuesta_seleccionada = evento.pos[1] // 50 - 100
                if respuesta_seleccionada == preguntas[tema][pregunta_actual]["respuesta"]:
                    puntuacion += 1
                pregunta_actual += 1
            else:
                ventana.fill((255, 255, 255))
                texto = fuente.render("Puntuación final: " + str(puntuacion) + "/" + str(len(preguntas[tema])), True, (0, 0, 0))
                ventana.blit(texto, (100, 100))
                pygame.display.update()
                pygame.time.wait(2000)
                pygame.quit()
                sys.exit()

    ventana.fill((255, 255, 255))

    if pregunta_actual < len(preguntas[tema]):
        texto = fuente.render(preguntas[tema][pregunta_actual]["pregunta"], True, (0, 0, 0))
        ventana.blit(texto, (100, 50))
        for i, opcion in enumerate(preguntas[tema][pregunta_actual]["opciones"]):
            texto = fuente.render(opcion, True, (0, 0, 0))
            ventana.blit(texto, (100, 100 + i * 50))
    else:
        texto = fuente.render("Puntuación final: " + str(puntuacion) + "/" + str(len(preguntas[tema])), True, (0, 0, 0))
        ventana.blit(texto, (100, 100))

    pygame.display.update()