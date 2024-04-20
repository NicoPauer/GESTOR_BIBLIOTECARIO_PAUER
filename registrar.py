#!/usr/bin/python3

'''
    Autor: Nico Pauer 
    Projecto: Registrador de libros v1, programada el 18/04/2024 de 14:23 a 18:04 hs (3 horas y 41 minutos).
    Descripción: Registra de forma sencilla nuevos libros en 'libros-argentinos.csv'
'''

# Uso Gobject instrospection para poder usar las bibliotecas de Gtk programadas en C de entornos 
# de escritorio que lo tengan como Gnome, Cinnamon, Mate, Xfce y derivados
import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

class Ventana(Gtk.Window):

    def __init__(self, titulo = 'Nueva Ventana', ancho = 100, alto = 100):
      # Defino titulo de ventana
        super().__init__(title = titulo)
      # Defino su tamaño
        self.set_size_request(ancho, alto)
      # Agregar código ISBN
        self.lector_de_codigo = Gtk.Entry()
        self.lector_de_codigo.set_placeholder_text('Código ISBN')
    # Establecer que solo se puedan ingresar en cantidad 13 numeros con sus 5 guiones de separacion de codigo ISBN-13
        self.lector_de_codigo.set_max_length(19)
    # Ingresar año de publicación    
        self.entrada_anio = Gtk.Entry()
        self.entrada_anio.set_placeholder_text('Año de publicación')
    # Ingresar autor
        self.entrada_autor = Gtk.Entry()
        self.entrada_autor.set_placeholder_text('Autor')
    # Ingresar titulo
        self.entrada_titulo = Gtk.Entry()
        self.entrada_titulo.set_placeholder_text('Titulo del libro')
    # Ingresar titulo
        self.editorial = Gtk.Entry()
        self.editorial.set_placeholder_text('Editorial')
    # Agregar boton
        self.datos = []
        self.boton_enviar_formulario = Gtk.Button(label = ' REGISTRAR')
        self.boton_enviar_formulario.connect('clicked', self.registro)
    # Creo contenedor
        self.contenedor = Gtk.VBox()
        #help(self.contenedor)
        self.contenedor.set_spacing(42)
    # Agrego todos los widgets a la interfaz grafica
        for widget in [self.lector_de_codigo, self.entrada_titulo, self.entrada_autor, self.editorial, self.entrada_anio, self.boton_enviar_formulario]:

            self.contenedor.add(widget)
    # Agrego contenedor a ventana para que todos los elementos sean visibles 
        self.add(self.contenedor)

    def registro(self, boton_enviar_formulario):

        '''
            Evento que se genera al oprimir botón 'REGISTRAR' que actualiza lista de datos
            ingresados por el usuario y agrega nueva linea al archivo 'libros-argentinos.csv'
        '''
        # Actualizo los datos
        self.datos = [self.lector_de_codigo.get_text(), self.entrada_titulo.get_text(), self.entrada_autor.get_text(), self.entrada_anio.get_text(), self.editorial.get_text()]
        # Preparo para la actualizacion

        print(self.datos)

        actualizando_archivo = open('libros-argentinos.csv', 'a')

        actualizando_archivo.write('%s,%s,%s,%s,%s\n' % (self.datos[0], self.datos[1], self.datos[2], self.datos[4], self.datos[3]))

        actualizando_archivo.close()


# Me encargo de crear y mostrar la interfaz
if (__name__ == '__main__'):
    # Crea instancia de Ventana para crear la ventana_principal
    ventana_principal = Ventana('REGISTRAR LIBRO ', 390, 600)
    # Muestra la ventana con todos sus widgets
    ventana_principal.show_all()
    try:

        Gtk.main()

    except:

        print('\n\tFIN DE VENTANA...\n')
