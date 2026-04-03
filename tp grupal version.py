libros = [[1,'Sapo Pepe'],[2,'Martin Fierro'],[3,'Dracula']]
libros_reservados = []
selector = 0

def main():
    print('Bienvendio al sistema de reservas de biblioteca de la UADE!')
    usuario = input ('Porfavor, Ingrese su nombre a continuación \n---> ')
    if usuario == 'admin':
        menu_admin(usuario)
    else:
        print ('Bienvenido', usuario,'!')
        menu(usuario)

def menu(usuario):
    print('Ingrese la opción que desee llevar a cabo.\n1. Ver listado de libros disponibles.\n2. Realizar una reserva.\n3. Ver libros reservados.')
    selector = int(input('---> '))
    if selector == 1:
        listado_libros(usuario)
    elif selector == 2:
        reservar_libros(usuario)
    elif selector == 3:
        libros_ya_reservados(usuario)
    else:
        print ('Hasta luego!!')
        
def menu_admin(usuario):
    print ('Iniciando partición de administrador.')

def listado_libros(usuario):
    print ('Libros Disponibles.')
    for i in libros:
        print ('id:',i[0],'nombre:',i[1])
    menu(usuario)
    
def libros_ya_reservados(usuario):
    if libros_reservados == []:
        print('No hay reservas existentes.')
    else:
        print ('Libros reservados.')
        for i in libros_reservados:
            print ('id:',i[0],'nombre:',i[1])
    menu(usuario)
    
def reservar_libros(usuario):
    print('Seleccione el id del libro que desea reservar.')
    for i in libros:
        print ('id:',i[0],'nombre:',i[1])
    di = int(input('---> '))
    for l in libros:
        if l[0] == di:
            libro_encontrado = l
            libros.remove(libro_encontrado)
            libros_reservados.append(libro_encontrado)
            print ('Libro reservado!!\nSu libro se ha agregado a la lista de libros reservados.')
        else:
            print('Error.')
    menu(usuario)


main()
