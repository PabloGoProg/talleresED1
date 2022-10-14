from time import sleep
from double_linked_list import DoubleLinkedList
from signly_linked_list import linked_list

class Solution:
    def __init__(self):
        self.selected_structure = None
        self.structures = ['Enlace simple', 'Enlace doble']

    def select_structure(self):
        while True:
            try:
                for i in range(2):
                    print(f'{i+1} - {self.structures[i]}')
                seleccion = int(input('Seleccione el tipo de estructuracon la que le gustaria trabajar: '))
                if seleccion == 1:
                    self.selected_structure = linked_list()
                elif seleccion == 2:
                    self.selected_structure = DoubleLinkedList()
                else:
                    continue
                break
            except:
                print('Seleccione un valor numerico')

    def sub_menu(self):
        self.select_structure()
        follow = 1
        menu = '''
                    1 - Añadir nodo
                    2 - Eliminar nodo
                    3 - Consultar valor contenido en el nodo
                    4 - Modificar valor de nodo
                    5 - Invertir toda la lista
                '''
        while follow == 1:
            print(menu)
            while True:
                try:
                    seleccion = int(input('Que accion desea realizar? '))
                    if seleccion == 1:
                        self.anadir_nodo()
                    elif seleccion == 2:
                        self.eliminar_nodo()
                    elif seleccion == 3:
                        while True:
                            try:
                                index = int(input('Indice del valor que desea consultar: '))
                                if index > self.selected_structure.len or index < self.selected_structure.len:
                                    print('Inidce por fuera de la lista, ingrese nuevamente')
                                    continue
                                self.selected_structure.get_node_value(index)
                                break
                            except:
                                print('Ingrese un valor numerico ')
                    elif seleccion == 4:
                        while True:
                            try:
                                index = int(input('Indice del valor que desea actualizar: '))
                                value = int(input('Valor que reemplazara al actual: '))
                                if index > self.selected_structure.len or index < self.selected_structure.len:
                                    print('Inidce por fuera de la lista, ingrese nuevamente')
                                    continue
                                self.selected_structure.update_value(value, index)
                                break
                            except:
                                print('Debe entregar un valor numerico')
                    elif seleccion == 5:
                         self.selected_structure.reverse()
                    else:
                        print('Seleccione un valor de la lista')
                        print(menu)
                        continue
                    break
                except:
                    print('Seleccione un valor numerico')
            print('En caso de que quiera agregar mas opciones')
            print('''
                1 - Realizar otra accion
                2 - Cambiar la estructura
                Cualquier otro - Cerrar el programa
            ''')
            while True:
                try:
                    o = int(input(''))
                    if o == 2:
                        self.select_structure()
                    elif o != 1:
                        follow = 0
                    break
                except:
                    print('Seleccione un valor del tablero')

    def anadir_nodo(self):
        while True:
            try:
                print('''
                    1 - Al inicio
                    2 - Al final
                    3 - En una posición específica
                ''')
                method = int(input('Que methodo desea usar? '))
                if method == 1:
                    while True:
                        try:
                            data = int(input('Que valor numerico desea agregar: '))
                            self.selected_structure.unshift_node(data)
                            break
                        except:
                            print('Debe ser un valor numerico')
                elif method == 2:
                    while True:
                        try:
                            data = int(input('Que valor numerico desea agregar: '))
                            self.selected_structure.append_node(data)
                            break
                        except:
                            print('Debe ser un valor numerico')
                elif method == 3:
                    while True:
                        try:
                            index = int(input('A que indice numerico desea agregar: '))
                            while True:
                                try:
                                    data = int(input('Que valor numerico desea agregar: '))
                                    break
                                except:
                                    print('Ingrese un valor numerico para añadir')
                            self.selected_structure.insert_node(index, data)
                            break
                        except:
                            print('Debe ser un valor numerico')
                self.selected_structure.print()
                break
            except:
                print('Seleccione un valor numerico')
            
    def eliminar_nodo(self):
        menu = '''
                    1 - Al inicio
                    2 - Al final
                    3 - En una posición específica
                '''
        print(menu)
        while True:
            try:
                method = int(input('Que methodo desea usar? '))
                if method == 1:
                    self.selected_structure.remove_head()
                elif method == 2:
                    self.selected_structure.pop()
                elif method == 3:
                    while True:
                        try:
                            index = int(input('Indice del valor que desee eliminar: '))
                            self.selected_structure.remove_by_index(index)
                            break
                        except:
                            print('Seleccione un valor numerico')
                else:
                    print('Ingrese un valor del menu: ')
                    print(menu)
                    continue
                self.selected_structure.print()
                break
            except:
                print('Seleccione un valor numerico')
