from double_linked_list import DoubleLinkedList
from signly_linked_list import linked_list
from colorama import *

class Solution:
    def __init__(self):
        self.sll = linked_list()
        self.dll = DoubleLinkedList()
        self.selected_structure = None
        self.structures = ['Listas simplemente enlazada', 'Listas doblemente enlazadas']

    def select_structure(self):
        while True:
            try:
                print('Seleccione el tipo de lista que desea utilizar dentro de las siguientes opciones:')
                print(Fore.YELLOW + f'''
                    1 - {self.structures[0]}
                    2 - {self.structures[1]}
                ''')
                seleccion = int(input(Fore.WHITE + 'Seleccione el tipo de estructuracon la que le gustaria trabajar: '))
                if seleccion == 1:
                    self.selected_structure = self.sll
                elif seleccion == 2:
                    self.selected_structure = self.dll
                else:
                    continue
                break
            except:
                print(Fore.RED + 'Seleccione un valor numerico')

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
            print(Fore.YELLOW + menu)
            while True:
                try:
                    seleccion = int(input(Fore.WHITE + 'Que accion desea realizar? '))
                    if seleccion == 1:
                        self.anadir_nodo()
                    elif seleccion == 2:
                        self.eliminar_nodo()
                    elif seleccion == 3:
                        while True:
                            try:
                                index = int(input(Fore.WHITE + 'Indice del valor que desea consultar: '))
                                if index-1 > self.selected_structure.len or index-1 < 0:
                                    print(Fore.RED + 'Inidce por fuera de la lista, ingrese nuevamente')
                                    continue
                                print(self.selected_structure.get_node_value(index-1))
                                break
                            except:
                                print(Fore.RED + 'Ingrese un valor numerico ')
                    elif seleccion == 4:
                        self.actualizar_valor()
                    elif seleccion == 5:
                        while True:
                            try:
                                print(Fore.YELLOW + 
                                '''
                        1 - Reverse comun
                        2 - Reverse con raices
                                ''')
                                try:
                                    seleccion = int(input(Fore.WHITE + ''))
                                except:
                                    print(Fore.RED + 'Debe entregar un valor numerico')
                                if seleccion == 1:
                                    self.selected_structure.reverse()
                                elif seleccion == 2:
                                    self.selected_structure.reverse_raiz()
                                else:
                                    print(Fore.RED + 'Debe Seleccionar un valo de la lista')
                                    continue
                                break
                            except:
                                print(Fore.RED + "Debe ingresar un valor numerico")
                    else:
                        print(Fore.RED + 'Seleccione un valor de la lista')
                        print(Fore.YELLOW + menu)
                        continue
                    print(Fore.GREEN + 'Actualmente la lista se encuentra así: ')
                    self.selected_structure.print()
                    break
                except:
                    print(Fore.RED + 'Seleccione un valor numerico')
            print(Fore.YELLOW + 'En caso de que quiera agregar mas opciones')
            print(Fore.YELLOW + 
            '''
                    1 - Realizar otra accion
                    2 - Cambiar la estructura
                    Cualquier otro - Cerrar el programa
            ''' + Fore.WHITE)
            while True:
                try:
                    o = int(input(''))
                    if o == 2:
                        self.select_structure()
                    elif o != 1:
                        follow = 0
                    break
                except:
                    print(Fore.RED + 'Seleccione un valor del tablero')

    def actualizar_valor(self):
        while True:
            try:
                index = int(input(Fore.WHITE + 'Indice del valor que desea actualizar: '))
                if index-1 > self.selected_structure.len or index-1 < 0:
                    print(Fore.RED + 'Inidce por fuera de la lista, ingrese nuevamente')
                    continue
                if isinstance(self.selected_structure, DoubleLinkedList):
                    print(Fore.YELLOW + 
                    '''
                    Desea actualizar el valor como el cuadrado del valor anterior?
                        1 - Si
                        2 - No
                    ''')
                    try:
                        seleccion = int(input(Fore.WHITE))
                    except:
                        print(Fore.RED + 'Seleccione un valor de la lista')
                    if seleccion == 1:
                        self.cuadrado_anteior(index-1)
                        break
                try:
                    value = int(input(Fore.WHITE + 'Valor que reemplazara al actual: '))
                except:
                    print(Fore.RED + 'Debe ser un valor numerico')
                self.selected_structure.update_value(value, index-1)
                break
            except:
                print(Fore.RED + 'Debe entregar un valor numerico')

    '''
    Define las posibilidades para añadir valores dentro de una lista
    '''
    def anadir_nodo(self):
        while True:
            try:
                print(Fore.YELLOW + 
                '''
                    1 - Al inicio
                    2 - Al final
                    3 - En una posición específica
                ''')
                method = int(input(Fore.WHITE + 'Que methodo desea usar? '))
                if method == 1:
                    while True:
                        try:
                            data = int(input(Fore.WHITE + 'Que valor numerico desea agregar: '))
                            if self.repeated_value(data):
                                print(Fore.RED + 'Este valor ya existe en la lista, añada otro')
                                continue
                            self.selected_structure.unshift_node(data)
                            break
                        except:
                            print(Fore.RED + 'Debe ser un valor numerico')
                elif method == 2:
                    while True:
                        try:
                            data = int(input(Fore.WHITE + 'Que valor numerico desea agregar: '))
                            if self.repeated_value(data):
                                print(Fore.RED + 'Este valor ya existe en la lista, añada otro')
                                continue
                            self.selected_structure.append_node(data)
                            break
                        except:
                            print(Fore.RED + 'Debe ser un valor numerico')
                elif method == 3:
                    while True:
                        try:
                            index = int(input(Fore.WHITE + 'A que indice numerico desea agregar: '))
                            if index-1 <= self.selected_structure.len and index-1 >= 0:
                                try:
                                    data = int(input(Fore.WHITE + 'Que valor desea insertar? '))
                                    if self.repeated_value(data):
                                        print(Fore.RED + 'Este valor ya existe en la lista, añada otro')
                                        continue
                                except:
                                    print(Fore.RED + 'Ingrese un valor numerico')
                            else:
                                print(Fore.RED + 'Agrege una posicion valida dentro de; rango')
                                continue
                            self.selected_structure.insert_node(index-1, data)
                            break
                        except:
                            print(Fore.RED + 'Debe ser un valor numerico')
                else:
                    print(Fore.RED + 'Seleccione un valor de la lista')
                    continue
                break
            except:
                print(Fore.RED + 'Seleccione un valor numerico')
            
    def eliminar_nodo(self):
        menu = '''
                    1 - Al inicio
                    2 - Al final
                    3 - En una posición específica
                '''
        print(Fore.YELLOW + menu)
        while True:
            try:
                method = int(input(Fore.WHITE + 'Que methodo desea usar? '))
                if method == 1:
                    self.selected_structure.remove_head()
                elif method == 2:
                    self.selected_structure.pop()
                elif method == 3:
                    while True:
                        try:
                            index = int(input(Fore.WHITE + 'Indice del valor que desee eliminar: '))
                            if index-1 < 0 or index-1 > self.selected_structure.len:
                                print(Fore.RED + 'El indice esta por fuera de la lista, seleccione nuevamente')
                                continue
                            self.selected_structure.remove_by_index(index-1)
                            break
                        except:
                            print(Fore.RED + 'Seleccione un valor numerico')
                else:
                    print(Fore.RED + 'Ingrese un valor del menu: ')
                    print(Fore.YELLOW + menu)
                    continue
                break
            except:
                print(Fore.RED + 'Seleccione un valor numerico')

    def repeated_value(self, value):
        cur = self.selected_structure.head
        flag = False
        while cur != None:
            if cur.data == value:
                flag = True
                return flag
            cur = cur.next
        return flag

    def cuadrado_anteior(self, index):
        if index == 0:
            self.selected_structure.head.data = 0
            return
        prev = self.selected_structure.get_node(index-1)
        self.selected_structure.update_value(prev.data ** 2, index)
    


