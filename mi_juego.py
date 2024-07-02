import pygame
from biblioteca_juego import *
from datos import lista

pygame.init() #Se inicializa pygame

dimension_pantalla = [1000,800]

ubicacion_a = (245, 340, 310, 45)
ubicacion_b = (245, 410 , 310, 45)
ubicacion_c = (245, 480, 310, 45)

rect_boton_jugar = pygame.Rect(354, 530, 250, 45)
rect_boton_puntaje = pygame.Rect(354, 590, 250, 45)
rect_boton_salir = pygame.Rect(354,650,250,45)

rect_boton_preguntar = pygame.Rect(55, 61, 250, 45)
rect_boton_reiniciar = pygame.Rect(367, 61, 250, 45)
rect_boton_atras = pygame.Rect(697, 61, 250, 45)

rect_opcion_a = pygame.Rect(ubicacion_a)
rect_opcion_b = pygame.Rect(ubicacion_b)
rect_opcion_c = pygame.Rect(ubicacion_c)

rect_usuario = pygame.Rect(137, 235, 750, 80)

#! COLORES
color_botones = (195, 245, 250)
color_titulos = (245, 22, 29)

#!FUENTES Y TEXTOS
font = pygame.font.SysFont("Arial Narrow", 45)
font_score = pygame.font.SysFont("Arial Narrow", 30)
font_titulos = pygame.font.SysFont("Arial Narrow", 50)
# PANTALLA A
texto_jugar = font.render("Jugar", True, (0,0,0))
texto_puntaje = font.render("Ver puntajes", True, (0,0,0))
texto_salir = font.render("Salir", True, (0,0,0))
puntaje = 0
texto_score = font_score.render(f"Puntaje: {puntaje}", True,(0,0,0))

#PANTALLA B
texto_preguntar = font.render("Preguntar", True, (0,0,0))
texto_reiniciar = font.render("Reiniciar", True, (0,0,0))
texto_atras = font.render("Atras", True, (0,0,0))
texto_intentos = font_score.render("Selecciona una opción, ¡tienes dos intentos para sumar 10 puntos!", True, (0,0,0))
texto_mucha_suerte = font_score.render("¡Mucha suerte!", True, (0,0,0))

#PANTALLA C
texto_mejores_puntajes = font_titulos.render("¡Estos son los mejores puntajes!", True, (color_titulos))

#PANTALLA D:
texto_felicitaciones = font_titulos.render("¡Felicitaciones!", True, (color_titulos))
#texto_gracias = font.render("¡Gracias por jugar con nosotros!", True, (0,0,0))
texto_gracias = font_titulos.render("", True, (0,0,0))
texto_gracias_continuacion = font_score.render("", True, (0,0,0))
texto_ingresar_usuario = font.render(f"Ingrese su nombre(hasta 8 caracteres):", True, (0,0,0))


#! texto sonido mute:
texto_sonido_activo = font_score.render("Sound on", True, (0,0,0))
rect_sonido_activo = pygame.Rect(10,10,120,30)


#!  IMAGENES
imagen_fondo = pygame.image.load("juego_preguntados/archivos/imageen_fondo.jpg")
imagen_fondo = pygame.transform.scale(imagen_fondo, dimension_pantalla)
imagen_jugar =  pygame.image.load("juego_preguntados/archivos/Preguntados.jpg")
imagen_puntaje =  pygame.image.load("juego_preguntados/archivos/img_puntajes.jpg")
imagen_puntaje = pygame.transform.scale(imagen_puntaje, dimension_pantalla)
icono_puntajes =  pygame.image.load("juego_preguntados/archivos/icono_puntajes.png")
fondo_final =  pygame.image.load("juego_preguntados/archivos/fondo_final.jpg")
fondo_final = pygame.transform.scale(fondo_final, dimension_pantalla)
icono_final =  pygame.image.load("juego_preguntados/archivos/img_ultima_pantalla.png")
icono_final = pygame.transform.scale(icono_final, (350,350))

#! SONIDOS
pygame.mixer.init()
sonido_error = pygame.mixer.Sound("juego_preguntados/archivos/error-4-199275.mp3")
sonido_correcto = pygame.mixer.Sound("juego_preguntados/archivos/correcto.mp3")
sonido_inicio = pygame.mixer.Sound("juego_preguntados/archivos/iniciooo.mp3")
sonido_felicitaciones = pygame.mixer.Sound("juego_preguntados/archivos/felicitaciones.mp3")
sonido_click = pygame.mixer.Sound("juego_preguntados/archivos/click.mp3")
sonido__empezar_jugar = pygame.mixer.Sound("juego_preguntados/archivos/emepezar_jugar.mp3")
sonido_puntajes = pygame.mixer.Sound("juego_preguntados/archivos/puntaje.mp3")
sonido_inicio.set_volume(0.2)


lista_preguntas = 0
respuesta_a = "a"
respuesta_b = "b"
respuesta_c = "c"
errores = 0

screen = pygame.display.set_mode(dimension_pantalla) #Se crea una ventana
running = True

esta_jugando = "A"
cargar_pregunta = False

bandera_colision_a = False
bandera_colision_b = False
bandera_colision_c = False

nombre_usuario = ""
activar_teclado = False

control_repeticion = False

funcionamiento_preguntar = True

lista_jugadores = cargar_json()

sonido = True

sonido_inicio.play(10)
while running:
    pressed_keys = pygame.key.get_pressed()
   # Se verifica si el usuario cerro la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False
        if event.type == pygame.MOUSEBUTTONDOWN:

            #print(f"mouse down: {event.pos}")
            if esta_jugando == "A":  
                if rect_boton_jugar.collidepoint(event.pos):
                    sonido_inicio.stop()
                    sonido__empezar_jugar.play()
                    #print("se apreto boton jugar")
                    esta_jugando = "B"
                if rect_boton_puntaje.collidepoint(event.pos):
                    ordenar_puntaje(lista_jugadores, "puntaje")

                    sonido_inicio.stop()
                    sonido_puntajes.play()
                    esta_jugando = "C"
                    control_repeticion = True
                    #print("Se apreto Ver puntaje")
                if rect_boton_salir.collidepoint(event.pos):
                    #print("Se apreto Salir")
                    running = False

            if sonido == True:
                if rect_sonido_activo.collidepoint(event.pos):
                    texto_sonido_activo = font_score.render("Sound off", True, (0,0,0))
                    controlar_volumen(True,sonido_error,sonido_correcto,sonido_felicitaciones,sonido_click,sonido__empezar_jugar,sonido_puntajes,sonido_inicio)
                    sonido = False
            else:
                if rect_sonido_activo.collidepoint(event.pos):
                    texto_sonido_activo = font_score.render("Sound on", True, (0,0,0))
                    controlar_volumen(False,sonido_error,sonido_correcto,sonido_felicitaciones,sonido_click,sonido__empezar_jugar,sonido_puntajes,sonido_inicio)
                    sonido = True
                    


            if esta_jugando == "B":
                control_repeticion = True
                
                if rect_boton_preguntar.collidepoint(event.pos):
                    #print("Se apreto preguntar")
                    cargar_pregunta = True
                    sonido_click.play()
                    if lista_preguntas < len(lista):
                        if funcionamiento_preguntar == True:
                            pregunta_a_mostrar = lista[lista_preguntas]
                            texto_pregunta = font.render((pregunta_a_mostrar['pregunta']), True, (0,0,0))
                            texto_opcion_a = font.render((pregunta_a_mostrar['a']), True, (0,0,0))
                            texto_opcion_b = font.render((pregunta_a_mostrar['b']), True, (0,0,0))
                            texto_opcion_c = font.render((pregunta_a_mostrar['c']), True, (0,0,0))
                            bandera_colision_a = True
                            bandera_colision_b = True
                            bandera_colision_c = True
                            errores = 0
                            funcionamiento_preguntar = False
                    else:
                        esta_jugando = "D"
                        activar_teclado = True


                if bandera_colision_a == True:
                    if rect_opcion_a.collidepoint(event.pos):
                        #print("apreto en a")
                        if lista_preguntas < len(lista)-1:
                            
                            if respuesta_a == pregunta_a_mostrar['correcta']:
                                puntaje += 10
                                texto_score = font_score.render(f"Puntaje: {puntaje}", True,(0,0,0))
                                lista_preguntas += 1
                                pregunta_a_mostrar = lista[lista_preguntas]
                                texto_pregunta = font.render((pregunta_a_mostrar['pregunta']), True, (0,0,0))
                                texto_opcion_a = font.render((pregunta_a_mostrar['a']), True, (0,0,0))
                                texto_opcion_b = font.render((pregunta_a_mostrar['b']), True, (0,0,0))
                                texto_opcion_c = font.render((pregunta_a_mostrar['c']), True, (0,0,0))
                                errores = 0
                                bandera_colision_b = True
                                bandera_colision_c = True
                                sonido_correcto.play()
                            else:
                                errores += 1
                                texto_opcion_a = font.render((pregunta_a_mostrar['a']), True, (255,255,255))
                                bandera_colision_a = False
                                sonido_error.play()
                                #print("la bandera se puso false a")

                                if errores == 2:
                                    lista_preguntas += 1

                                    pregunta_a_mostrar = lista[lista_preguntas]
                                    texto_pregunta = font.render((pregunta_a_mostrar['pregunta']), True, (0,0,0))
                                    texto_opcion_a = font.render((pregunta_a_mostrar['a']), True, (0,0,0))
                                    texto_opcion_b = font.render((pregunta_a_mostrar['b']), True, (0,0,0))
                                    texto_opcion_c = font.render((pregunta_a_mostrar['c']), True, (0,0,0))
                                    errores = 0
                                    bandera_colision_a = True
                                    bandera_colision_b = True
                                    bandera_colision_c = True
                                    sonido_error.play()

                        else:
                            if respuesta_a == pregunta_a_mostrar['correcta']:
                                puntaje += 10
                                texto_score = font_score.render(f"Puntaje: {puntaje}", True,(0,0,0))
                                errores = 0
                                esta_jugando = "D"
                                activar_teclado = True
                                sonido_correcto.play()
                                sonido_felicitaciones.play()
                            else:
                                errores += 1
                                texto_opcion_a = font.render((pregunta_a_mostrar['a']), True, (255,255,255))
                                bandera_colision_a = False
                                sonido_error.play()
                                if errores == 2:
                                    esta_jugando = "D"
                                    activar_teclado = True
                                    sonido_error.play()
                                    sonido_felicitaciones.play()

                if bandera_colision_b == True:
                    if rect_opcion_b.collidepoint(event.pos):
                        #print("apreto en b")
                        if  lista_preguntas < len(lista)-1:
                            if respuesta_b == pregunta_a_mostrar['correcta']:
                                puntaje += 10
                                texto_score = font_score.render(f"Puntaje: {puntaje}", True,(0,0,0))
                                lista_preguntas += 1
                                pregunta_a_mostrar = lista[lista_preguntas]
                                texto_pregunta = font.render((pregunta_a_mostrar['pregunta']), True, (0,0,0))
                                texto_opcion_a = font.render((pregunta_a_mostrar['a']), True, (0,0,0))
                                texto_opcion_b = font.render((pregunta_a_mostrar['b']), True, (0,0,0))
                                texto_opcion_c = font.render((pregunta_a_mostrar['c']), True, (0,0,0))
                                errores = 0
                                bandera_colision_a = True
                                bandera_colision_c = True
                                sonido_correcto.play()

                            else:
                                errores += 1
                                #print(errores)
                                texto_opcion_b = font.render((pregunta_a_mostrar['b']), True, (color_titulos))
                                bandera_colision_b = False
                                sonido_error.play()
                                if errores == 2:
                                    lista_preguntas += 1
                                    pregunta_a_mostrar = lista[lista_preguntas]
                                    texto_pregunta = font.render((pregunta_a_mostrar['pregunta']), True, (0,0,0))
                                    texto_opcion_a = font.render((pregunta_a_mostrar['a']), True, (0,0,0))
                                    texto_opcion_b = font.render((pregunta_a_mostrar['b']), True, (0,0,0))
                                    texto_opcion_c = font.render((pregunta_a_mostrar['c']), True, (0,0,0))
                                    errores = 0
                                    bandera_colision_a = True
                                    bandera_colision_b = True
                                    bandera_colision_c = True
                                    sonido_error.play()
                        else:
                            if respuesta_b == pregunta_a_mostrar['correcta']:
                                puntaje += 10
                                texto_score = font_score.render(f"Puntaje: {puntaje}", True,(0,0,0))
                                errores = 0
                                esta_jugando = "D"
                                activar_teclado = True
                                sonido_correcto.play()
                                sonido_felicitaciones.play()
                            else:
                                errores += 1
                                #print(errores)
                                texto_opcion_b = font.render((pregunta_a_mostrar['b']), True, (255,255,255))
                                bandera_colision_b = False
                                sonido_error.play()
                                if errores == 2:
                                    esta_jugando = "D"
                                    activar_teclado = True
                                    sonido_error.play()
                                    sonido_felicitaciones.play()

                if bandera_colision_c == True:
                    if rect_opcion_c.collidepoint(event.pos):
                        #print("apreto en c")
                        if lista_preguntas < len(lista)-1:
                            if respuesta_c == pregunta_a_mostrar['correcta']:
                                puntaje += 10
                                texto_score = font_score.render(f"Puntaje: {puntaje}", True,(0,0,0))
                                lista_preguntas += 1
                                pregunta_a_mostrar = lista[lista_preguntas]

                                texto_pregunta = font.render((pregunta_a_mostrar['pregunta']), True, (0,0,0))
                                texto_opcion_a = font.render((pregunta_a_mostrar['a']), True, (0,0,0))
                                texto_opcion_b = font.render((pregunta_a_mostrar['b']), True, (0,0,0))
                                texto_opcion_c = font.render((pregunta_a_mostrar['c']), True, (0,0,0))
                                errores = 0
                                bandera_colision_a = True
                                bandera_colision_b = True
                                sonido_correcto.play()
                            else:
                                errores += 1
                                #print(errores)
                                texto_opcion_c = font.render((pregunta_a_mostrar['c']), True, (255,255,255))
                                bandera_colision_c = False
                                sonido_error.play()
                                #print("la bandera se puso false")
                                if errores == 2:
                                    lista_preguntas += 1
                                    pregunta_a_mostrar = lista[lista_preguntas]

                                    texto_pregunta = font.render((pregunta_a_mostrar['pregunta']), True, (0,0,0))
                                    texto_opcion_a = font.render((pregunta_a_mostrar['a']), True, (0,0,0))
                                    texto_opcion_b = font.render((pregunta_a_mostrar['b']), True, (0,0,0))
                                    texto_opcion_c = font.render((pregunta_a_mostrar['c']), True, (0,0,0))
                                    errores = 0
                                    bandera_colision_a = True
                                    bandera_colision_b = True
                                    bandera_colision_c = True
                                    sonido_error.play()

                        else:
                            if respuesta_c == pregunta_a_mostrar['correcta']:
                                puntaje += 10
                                texto_score = font_score.render(f"Puntaje: {puntaje}", True,(0,0,0))
                                errores = 0
                                esta_jugando = "D"
                                activar_teclado = True
                                sonido_correcto.play()
                                sonido_felicitaciones.play()
                            else:
                                errores += 1
                                #print(errores)
                                texto_opcion_c = font.render((pregunta_a_mostrar['c']), True, (255,255,255))
                                bandera_colision_c = False
                                sonido_error.play()
                                if errores == 2:
                                    esta_jugando = "D"
                                    activar_teclado = True
                                    sonido_error.play()
                                    sonido_felicitaciones.play()
                                    #print("la bandera se puso true")

                if rect_boton_reiniciar.collidepoint(event.pos):
                    #print("se apreto reiniciar")

                    puntaje = 0
                    texto_score = font_score.render(f"Puntaje: {puntaje}", True,(0,0,0))
                    errores = 0
                    lista_preguntas = 0
                    esta_jugando = "B"
                    cargar_pregunta = False
                    funcionamiento_preguntar = True
                    bandera_colision_a = False
                    bandera_colision_b = False
                    bandera_colision_c = False
                    sonido_click.play()

            if control_repeticion == True:
                if rect_boton_atras.collidepoint(event.pos):
                   #print("Se apreto atras")
                    puntaje = 0
                    texto_score = font_score.render(f"Puntaje: {puntaje}", True,(0,0,0))
                    errores = 0
                    #esta_jugando = "B"
                    lista_preguntas = 0
                    bandera_colision_a = False
                    bandera_colision_b = False
                    bandera_colision_c = False
                    cargar_pregunta = False
                    funcionamiento_preguntar = True
                    esta_jugando = "A"
                    sonido_puntajes.stop()
                    sonido_inicio.play()
                    control_repeticion = False

        if event.type == pygame.KEYDOWN:

            if activar_teclado == True:
                if event.key == pygame.K_BACKSPACE:
                    nombre_usuario = nombre_usuario[:-1]
                elif event.key == pygame.K_RETURN:
                    if len(nombre_usuario) <= 8:
                        #print(len(nombre_usuario))
                        lista_jugadores = guardar_nombres(lista_jugadores, nombre_usuario, puntaje)
                        guardar_json(lista_jugadores)
                        activar_teclado = False
                        texto_gracias = font.render(f"¡Gracias {nombre_usuario} por jugar con nosotros!", True, (color_titulos))
                        texto_gracias_continuacion = font_score.render("¡Podras ver el podio de mejores puntuaciones en la sección 'puntajes'!", True, (0,0,0))
                        nombre_usuario = "" 
                else:
                    nombre_usuario += event.unicode
                           

    match esta_jugando:
        case "A": # pantalla principal
            screen.blit(imagen_fondo, (0,0))
            pygame.draw.rect(screen, (color_botones),rect_boton_jugar, border_radius=25)
            pygame.draw.rect(screen, (color_botones),rect_boton_puntaje, border_radius=25)
            pygame.draw.rect(screen, (color_botones),rect_boton_salir, border_radius=25)
            pygame.draw.rect(screen, (color_botones),rect_sonido_activo, border_radius=25)
            screen.blit(texto_jugar, (433,540))
            screen.blit(texto_puntaje, (393,602))
            screen.blit(texto_salir, (438,665))
            screen.blit(texto_sonido_activo, (25,17))

        case "B": # pantalla de preguntas
            screen.blit(imagen_jugar,(0,0))
            pygame.draw.rect(screen, (color_botones),rect_boton_preguntar, border_radius=15)
            pygame.draw.rect(screen, (color_botones),rect_boton_reiniciar, border_radius=15)
            pygame.draw.rect(screen, (color_botones),rect_boton_atras, border_radius=15)
            pygame.draw.rect(screen, (color_botones),rect_sonido_activo, border_radius=25)
            screen.blit(texto_preguntar, (98,73))
            screen.blit(texto_reiniciar, (436,73))
            screen.blit(texto_atras, (784,73))
            screen.blit(texto_score, (833,17))
            screen.blit(texto_intentos, (50, 675))
            screen.blit(texto_mucha_suerte, (100, 720))
            if sonido == True:
                screen.blit(texto_sonido_activo, (25,17))
            else:
                screen.blit(texto_sonido_activo, (25,17))

            if cargar_pregunta == True:
                pygame.draw.rect(screen, (255,255,255),rect_opcion_a, border_radius=15)
                pygame.draw.rect(screen, (255,255,255),rect_opcion_b, border_radius=15)
                pygame.draw.rect(screen, (255,255,255),rect_opcion_c, border_radius=15)
                screen.blit(texto_pregunta, (77,267))
                screen.blit(texto_opcion_a, (285,353))
                screen.blit(texto_opcion_b, (285,423))
                screen.blit(texto_opcion_c, (285,492))
                      
        case "C": # pantalla de puntaje
            screen.blit(imagen_puntaje,(0,0))
            screen.blit(icono_puntajes, (72,403))
            screen.blit(texto_mejores_puntajes, (106, 88))
            pygame.draw.rect(screen, (color_botones),rect_boton_atras, border_radius=15)
            pygame.draw.rect(screen, (color_botones),rect_sonido_activo, border_radius=25)
            screen.blit(texto_atras, (784,73))
            if sonido == True:
                screen.blit(texto_sonido_activo, (25,17))
            else:
                screen.blit(texto_sonido_activo, (25,17))

            if len(lista_jugadores) >= 3:
                primer_puesto = lista_jugadores[0]["nombre"]
                primer_puntaje = lista_jugadores[0]['puntaje']
                segundo_puesto = lista_jugadores[1]["nombre"]
                segundo_puntaje = lista_jugadores[1]['puntaje']
                tercer_puesto = lista_jugadores[2]["nombre"]
                tercer_puntaje = lista_jugadores[2]['puntaje']
                texto_primer_lugar = font.render(f"1er Puesto: {primer_puesto}, {primer_puntaje} puntos ", True, (0,0,0))
                screen.blit(texto_primer_lugar, (217,163))
                texto_segundo_lugar = font.render(f"2do Puesto: {segundo_puesto}, {segundo_puntaje} puntos", True, (0,0,0))
                screen.blit(texto_segundo_lugar, (217,263))
                texto_tercer_lugar = font.render(f"3er Puesto: {tercer_puesto}, {tercer_puntaje} puntos ", True, (0,0,0))
                screen.blit(texto_tercer_lugar, (217,363))
            else:
                if len(lista_jugadores) == 2 :
                    primer_puesto = lista_jugadores[0]["nombre"]
                    primer_puntaje = lista_jugadores[0]['puntaje']
                    segundo_puesto = lista_jugadores[1]["nombre"]
                    segundo_puntaje = lista_jugadores[1]['puntaje']
                    texto_primer_lugar = font.render(f"1er Puesto: {primer_puesto}, {primer_puntaje} puntos ", True, (0,0,0))
                    screen.blit(texto_primer_lugar, (217,163))
                    texto_segundo_lugar = font.render(f"2do Puesto: {segundo_puesto}, {segundo_puntaje} puntos", True, (0,0,0))
                    screen.blit(texto_segundo_lugar, (217,263))
                    texto_sin_jugador_tres = font.render(f"3er Puesto: sin jugador", True, (0,0,0))
                    screen.blit(texto_sin_jugador_tres, (217,363))

                else:
                    if len(lista_jugadores) == 1:
                        primer_puesto = lista_jugadores[0]["nombre"]
                        primer_puntaje = lista_jugadores[0]['puntaje']
                        texto_primer_lugar = font.render(f"1er Puesto: {primer_puesto}, {primer_puntaje} puntos", True, (0,0,0))
                        screen.blit(texto_primer_lugar, (217,163))
                        texto_sin_jugador_dos = font.render(f"2do Puesto: sin jugador", True, (0,0,0))
                        screen.blit(texto_sin_jugador_dos, (217,263))
                        texto_sin_jugador_tres = font.render(f"3er Puesto: sin jugador", True, (0,0,0))
                        screen.blit(texto_sin_jugador_tres, (217,363))
                    else:
                        texto_sin_jugador_uno = font.render(f"1er Puesto: sin jugador ", True, (0,0,0))
                        screen.blit(texto_sin_jugador_uno, (217,163))
                        texto_sin_jugador_dos = font.render(f"2do Puesto: sin jugador", True, (0,0,0))
                        screen.blit(texto_sin_jugador_dos, (217,263))
                        texto_sin_jugador_tres = font.render(f"3er Puesto: sin jugador", True, (0,0,0))
                        screen.blit(texto_sin_jugador_tres, ())

        case "D": # pantalla de fin de juego
            control_repeticion = True
            screen.blit(fondo_final,(0,0))
            screen.blit(texto_felicitaciones, (98,53))
            texto_puntaje_final = font.render(f"Su puntaje es {puntaje}", True, (0,0,0))
            screen.blit(texto_puntaje_final,(98,118)) 
            screen.blit(icono_final,(48, 378)) 
            screen.blit(texto_gracias, (322,658))
            screen.blit(texto_gracias_continuacion, (280,706))
            pygame.draw.rect(screen, (color_botones),rect_boton_atras, border_radius=15)
            screen.blit(texto_atras, (784,73)) 
            pygame.draw.rect(screen,(color_botones),rect_usuario, border_radius=25)
            pygame.draw.rect(screen, (color_botones),rect_sonido_activo, border_radius=25)

            screen.blit(texto_ingresar_usuario, (240,193))
            nombre = font.render(nombre_usuario, True,(0,0,0))
            screen.blit(nombre, (385, 259))

            if sonido == True:
                screen.blit(texto_sonido_activo, (25,17))
            else:
                screen.blit(texto_sonido_activo, (25,17))

    pygame.display.flip()# Muestra los cambios en  la pantalla

pygame.quit() # Fin



