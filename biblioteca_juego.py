from datos import lista
import json


'''
A. Analizar detenidamente el set de datos (puede agregarle más preguntas si así
lo desea).
B. Crear una pantalla de inicio, con 3 (tres) botones, “Jugar”, “Ver Puntajes”,
“Salir”, la misma deberá tener alguna imagen cubriendo completamente el
fondo y tener un sonido de fondo. Al apretar el botón jugar se iniciará el juego.
Opcional: Agregar un botón para activar/desactivar el sonido de fondo.
C. Crear 2 botones uno con la etiqueta “Pregunta”, otro con la etiqueta “Reiniciar”
D. Imprimir el Puntaje: 000 donde se va a ir acumulando el puntaje de las
respuestas correctas. Cada respuesta correcta suma 10 puntos.
E. Al hacer clic en el botón “Pregunta” debe mostrar las preguntas comenzando
por la primera y las tres opciones, cada clic en este botón pasa a la siguiente
pregunta.
F. Al hacer clic en una de las tres palabras que representa una de las tres
opciones, si es correcta, debe sumar el puntaje, reproducir un sonido de
respuesta correcta y dejar de mostrar las otras opciones.
G. Solo tiene 2 intentos para acertar la respuesta correcta y sumar puntos, si
agotó ambos intentos, deja de mostrar las opciones y no suma puntos. Al
elegir una respuesta incorrecta se reproducirá un sonido indicando el error y
se ocultará esa opción, obligando al usuario a elegir una de las dos restantes.
H. Al hacer clic en el botón “Reiniciar” debe mostrar las preguntas comenzando
por la primera y las tres opciones, cada clic pasa a la siguiente pregunta.
También debe reiniciar el puntaje.
I. Una vez terminado el juego se deberá pedirle el nombre al usuario, guardar
ese nombre con su puntaje en un archivo, y volver a la pantalla de inicio.
J. Al ingresar a la pantalla “Ver Puntajes”, se deberá mostrar los 3 (tres) mejores
puntajes ordenados de mayor a menor, junto con sus nombres de usuario
correspondientes. Debe haber un botón para volver al menú principal.


NOTAS:
- Tienen total libertad para utilizar los sonidos, imágenes, y animaciones
(opcional) alusivas, donde corresponda.
- El formato del archivo que se debe crear para guardar los puntajes
debe ser TXT, CSV o JSON.
- Se deben definir y utilizar funciones, y las mismas deben estar
documentadas e importadas desde otro archivo (biblioteca).
'''




'''
E. Al hacer clic en el botón “Pregunta” debe mostrar las preguntas comenzando
por la primera y las tres opciones, cada clic en este botón pasa a la siguiente
pregunta.
'''



def guardar_nombres(lista: list,nombre: str, puntaje: int):
    '''
    recibe por parametros una lista, nombre y puntaje.
    se crea un diccionario
    el nombre lo agrega en un diccionario como valor en la clave "nombre"
    el puntaje se lo agrega como valor a la clave "puntaje
    El diccionario se agrega a la lista
    me retorna esa lista
    '''

    diccionario = {"nombre": nombre, "puntaje": puntaje}
    lista.append(diccionario)

    return lista


def cargar_json():
    '''
    lee los datos pasados por la ruta y me retorna lo leido en el archivo
    '''
    with open("juego_preguntados/nombre_jugadores.json", "r+") as archivo:
        datos = json.load(archivo)
        lista_de_jugadores = datos['jugadores'] 
    return lista_de_jugadores


    


def guardar_json(lista):
    '''
    recibe una lista por parametro
    guarda los datos de esa lista en la ruta del archivo json indicado
    '''
    with open("juego_preguntados/nombre_jugadores.json", "w") as archivo:
        json.dump({"jugadores": lista}, archivo, indent=2)



def ordenar_puntaje(lista_datos: list, clave: int):
    '''
    recibe una lista y una clave por parametros
    recorre la lista dos veces para ir comparando valores y ordenando de mayor a menor
    returna la lista ordenada
    '''
    for i in range(len(lista_datos)-1):
        for j in range(i+1, len(lista_datos)):
            if lista_datos[i][clave] < lista_datos[j][clave]:
                auxiliar = lista_datos[i]
                lista_datos[i] = lista_datos[j]
                lista_datos[j] = auxiliar

    return lista_datos

'''
texto_pregunta = font.render((pregunta_a_mostrar['pregunta']), True, (0,0,0))
texto_opcion_a = font.render((pregunta_a_mostrar['a']), True, (0,0,0))
texto_opcion_b = font.render((pregunta_a_mostrar['b']), True, (0,0,0))
texto_opcion_c = font.render((pregunta_a_mostrar['c']), True, (0,0,0))
'''

# def mostrar_pregunta(font,screen,lista_preguntas, pregunta_a_mostrar, clave_uno,clave_dos,clave_tres,clave_cuatro, color):

#     pregunta_a_mostrar = lista[lista_preguntas]
#     texto_pregunta = font.render((pregunta_a_mostrar[clave_uno]), True, color)
#     texto_opcion_a = font.render((pregunta_a_mostrar[clave_dos]), True, color)
#     texto_opcion_b = font.render((pregunta_a_mostrar[clave_tres]), True, color)
#     texto_opcion_c = font.render((pregunta_a_mostrar[clave_cuatro]), True, color)
  
#     return texto_pregunta, texto_opcion_a, texto_opcion_b, texto_opcion_c


def controlar_volumen(criterio:str, error,correcto,felicitaciones,click,jugar,puntajes,inicioo):
    '''
    recibe por parametros el indicador de va a ejecutar, y cada item a modificar
    si esta en true baja todos los volumenes, si esta en false los vuelve a subir
    '''
    if criterio == True:
        error.set_volume(0)
        correcto.set_volume(0)  
        felicitaciones.set_volume(0) 
        click.set_volume(0) 
        jugar.set_volume(0) 
        puntajes.set_volume(0) 
        inicioo.set_volume(0)
    else:
        error.set_volume(0.1)
        correcto.set_volume(0.1) 
        felicitaciones.set_volume(0.2) 
        click.set_volume(0.3) 
        jugar.set_volume(0.1) 
        puntajes.set_volume(0.2) 
        inicioo.set_volume(0.2)





