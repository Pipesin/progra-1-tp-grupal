import datetime
from datetime import timedelta 


libros = [[1,'Sapo Pepe',3000],[2,'Martin Fierro',5000],[3,'Dracula',7000]]
libros_reservados = []
usuarios_totales = []
selector = 0

def main():

    print('Bienvendio al sistema de reservas de biblioteca de la UADE!')
    login()

def login():

    ahora = datetime.datetime.now()
    ahora_txt = ahora.strftime("%d/%m/%Y %H:%M")

    ingresar_legajo = int(input('Porfavor, Ingrese su legajo a continuación:\n---> '))
    ingresar_nombre = input ('Porfavor, Ingrese su nombre a continuación:\n---> ')

    usuario = [ingresar_legajo,ingresar_nombre,ahora_txt]
    usuarios_totales.append(usuario)

    if usuario[0] == 1111 and usuario[1] == 'admin':
        menu_admin(usuario)
    else:
        print ('Sesion iniciada: Nombre:',usuario[1],' Legajo:',usuario[0],' Horario:',ahora_txt,'\nBienvenido!')
        menu(usuario)

def menu(usuario):
    print('Ingrese la opción que desee llevar a cabo.\n1. Ver listado de libros disponibles.\n2. Realizar una reserva.\n3. Ver libros reservados.\n0. Salir.')
    selector = int(input('---> '))
    if selector == 1:
        listado_libros(usuario)
    elif selector == 2:
        reservar_libros(usuario)
    elif selector == 3:
        libros_ya_reservados(usuario)
    elif selector == 0:
        print ('Hasta luego!!')
        
def menu_admin(usuario):
    print ('Iniciando partición de administrador.')

def listado_libros(usuario):
    print ('Libros Disponibles.')
    for i in libros:
        print ('id:',i[0],'/ nombre:',i[1],'/ precio:',i[2],)
    menu(usuario)
    
def libros_ya_reservados(usuario):
    if libros_reservados == []:
        print('No hay reservas existentes.')
    else:
        print ('Libros reservados.')
        for i in libros_reservados:
            print ('--->id:',i[0],'\nNombre:',i[1],'\nprecio:',i[2],'\nfecha de reserva:',i[3], '\nfecha de caducidad:',i[4],)
    menu(usuario)
    

def reservar_libros(usuario):
    precio_total = 0
    flag = 's'

    while flag != 'n':
        print('Seleccione el id del libro que desea reservar.')
        for i in libros:
            print ('id:',i[0],'/ nombre:',i[1],'/ precio:',i[2],)
        di = int(input('---> '))
        libro_encontrado = 0

        for l in libros:
            if l[0] == di:
                libro_encontrado = l
                break

        if libro_encontrado:

            ahora = datetime.datetime.now()
            expiracion = ahora + timedelta(days=7) #Usamos timedelta(days=7) para sumarle unos 7 dias a la fecha acutal, esto para agregar un "timer" de vencimiento a las reservas.
            
            ahora_txt = ahora.strftime("%d/%m/%Y %H:%M")
            expiracion_txt = expiracion.strftime("%d/%m/%Y %H:%M")

            libro_encontrado.append(ahora_txt) 
            libro_encontrado.append(expiracion_txt)

            libros.remove(libro_encontrado)
            libros_reservados.append(libro_encontrado)
            print ('Libro reservado!\nEl libro a sido agregado a la lista de libros reservados.\nCosto del libro:',
            libro_encontrado[2],'\nFecha de reserva:',libro_encontrado[3],'\nFecha de expiracion:',libro_encontrado[4],)
            flag = input ('Desea reservas otro libro? (s/n)\n--->')
        
        else:
            print('Error, el id ingresado es inexistente.')
            flag = input ('Desea intentar nuevamente? (s/n)\n--->')

    print('Usted ha reservado:')
    for l in libros_reservados:
        print('Libro:',l[0],', Precio:',l[2],)
        precio_total += l[2]

    print('Precio final:',precio_total,)
    
    menu(usuario)




main()