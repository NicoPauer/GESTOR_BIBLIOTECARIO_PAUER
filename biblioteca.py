#!/usr/bin/python3

'''
    Busca en el archivo 'libros-argentinos.csv' de forma gráfica usando Gtk 3
    a traves de módulo gi (GObject Instrospection) una coincidencia para los
    datos o algunos de ellos introducido de forma intuitiva por el usuario.
'''
# Para manejar expresiones regulares
import re
# Por si es necesario controlar algo del sistema como cierre de ventana
import os
# Importo módulo de GObject Instrospection que permite usar bibliotecas escritas en C con Python

import gi

# Solicito versión especifica de bibliotecas GObject Instrospection a usar
#
# Sintaxis: gi.require_version(biblioteca, version)

gi.require_version('Gtk', '3.0')

# Importo cada un de las bibliotecas a usar desde el repositorio GObject Instrospection
from gi.repository import Gtk
 
# Creo instancia Gtk.Window para la ventana principal con el formulario de busqueda

# VentanaPrincipal hereda de Gtk.Window

class VentanaPrincipal(Gtk.Window):

    def __init__(self, nombre_de_ventana = 'Nueva Ventana', dimensiones_pixeles = [100, 100]):

        # Utilizo constructor superior para dar titulo a ventana

        super().__init__(title = nombre_de_ventana)

        # Configuracion de ventana

        # Defino tamaño: Ancho y Alto en entero de pixeles
        
        self.set_size_request(dimensiones_pixeles[0], dimensiones_pixeles[1])
        # Creo widgtes para formulario ISBN, Autor, Nombre de libro, boton buscar, selector de editorial

        self.lector_de_codigo = Gtk.Entry()
        self.lector_de_codigo.set_placeholder_text('Código ISBN')
        # Establecer que solo se puedan ingresar en cantidad 13 numeros con sus 5 guiones de separacion de codigo ISBN-13
        self.lector_de_codigo.set_max_length(19)
        
        self.entrada_anio = Gtk.Entry()
        self.entrada_anio.set_placeholder_text('Año de publicación')

        self.entrada_autor = Gtk.Entry()
        self.entrada_autor.set_placeholder_text('Autor')

        self.entrada_titulo = Gtk.Entry()
        self.entrada_titulo.set_placeholder_text('Titulo del libro')

        self.selector_editoriales = Gtk.Entry()
        self.selector_editoriales.set_placeholder_text('Editorial')

        self.boton_enviar_formulario = Gtk.Button(label = ' BUSCAR ')

        self.boton_enviar_formulario.connect('clicked', self.busqueda)

        self.vista_de_resultados = Gtk.Label('[  LIBROS ARGENTINOS  ]')
        # Agrego contenedor de widgets vertical a la ventana

        self.contenedor_formulario = Gtk.VBox()

        espaciado = 6

        for widget in [self.lector_de_codigo,   self.entrada_anio,  self.entrada_autor, self.entrada_titulo,   self.selector_editoriales,   self.boton_enviar_formulario,   self.vista_de_resultados]:

             self.contenedor_formulario.pack_start(widget, True, True, espaciado)

             if (    widget is self.boton_enviar_formulario ):
                # Para juntarse mas vista_de_resultados el formulario
                espaciado -= 3

        self.add(self.contenedor_formulario)

        # Muestra todo
        # Sino estarian ocultos los elementos
        self.show_all()

    def busqueda(self, boton_enviar_formulario):
        # Encuentro filas de archivos libros-argentinos.csv

        fuente = open('libros-argentinos.csv', 'r')

        filas = ''

        for fila in fuente.readlines():
            # Defino condiciones de la busqueda
           
            contiene_ISBN = bool(   re.findall( self.lector_de_codigo.get_text().lower(),  fila.split(',')[0].lower()    )   )

            contiene_Titulo = bool( re.findall(  self.entrada_titulo.get_text().lower(), fila.split(',')[1].lower()    )   )

            contiene_Autor = bool(  re.findall(  self.entrada_autor.get_text().lower(),  fila.split(',')[2].lower() )    )

            contiene_Editorial = bool(  re.findall(  self.selector_editoriales.get_text().lower(),   fila.split(',')[3].lower()    )  )

            contiene_anio = bool(   re.findall(  self.entrada_anio.get_text().lower(),   fila.split(',')[4].lower()  ) )
            # Voy mostrando lo que cumple las condiciones, ir armando segun requerimintos las expresiones
            if (    (fila[0] != 'I') and (  (   contiene_anio and (  (  contiene_ISBN or (   contiene_Editorial or contiene_Autor    ) )    )  ) and ( contiene_Titulo and contiene_Autor  )   )   ):
            # Solo agrega si es una fila de valores y no de nombres de columnas
            # Ademas que su ISBN, AÑO, EDITORIAL, TITULO, AUTOR sean iguales (al menos dos)
                 filas += ('\n--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n[\t' + fila.replace(',', '\t | \t').replace('\n', '') + '\t]\n')
        fuente.close()

        # Muestro tabla con los datos de archivos encontrados
        self.vista_de_resultados.set_text('\tBusqueda de lo ingresado consultando "%s":\n\n[\tISBN\t]\t[\tTitulo\t]\t[\tAutor\t]\t[\tEditorial\t]  [\tAño\t]\n\n%s\n' % ('libros-argentinos.csv', filas))

# Algoritmo principal: funcionamiento inspirado en C pero que lo implenentaron en Python
if __name__ == '__main__':
    # Creo instancia de VentanaPrincipal
    ventana = VentanaPrincipal('Busqueda de libros argentinos por su ISBN-13 en archivo de datos CSV ', [700, 650])
    # Muestro toda la interfaz gráfica generada

# LA PARTE EN QUE MUESTRO LA VENTANA LA HAGO CON MANEJO DE CONTROL DE FLUJO DE EXCEPCIONES POR SI CIERRAN LA VENTANA
    try:

        Gtk.main()

    except:
        # Cierro la ventana
        ventana.close()
        os.system('clear && echo "\n\t[ VENTANA CERRADA]\t\n" && exit 0')
