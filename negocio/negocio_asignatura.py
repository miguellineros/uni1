
from datos.datos_asignatura import guardar_asignatura,obtener_listado_asignaturas

def listado_asignaturas():
    #if asignatura != None:
     #   print(f"con !=none {asignatura}")
    print("listado asignaturas   ")
    print("===============")

    asignaturas = obtener_listado_asignaturas()
    if len(asignaturas) > 0 :
        contador = 0
        for asignatura in asignaturas:
            contador += 1
            print(f"[{contador}] {asignatura}")
            print("==========================")
    else:
        print("no se an encontrado elementos  ")



def agregar_asignatura():
    listado_asignaturas()
    nueva_asignatura = input("ingrese el nombre de su nueva asignatura:    ")
    print()
    asignaturas = obtener_listado_asignaturas()
    if len(asignaturas) >0:
        if nueva_asignatura != "":
              asignaturas.append(nueva_asignatura.title())
    datos_guardar = f"asignaturas = {asignaturas}"      
    guardar_asignatura(datos_guardar)      
    listado_asignaturas()



def modificar_asignatura():
    listado_asignaturas()
    
    indicar_asignatura = input("indique el numero de la asignatura:  ")
    try:
        numero_asignatura = int(indicar_asignatura)
        asignaturas = obtener_listado_asignaturas()
        if len(asignaturas) > 0 :
            asignatura_modificada = input("ingrese nuevo nombre de asignatura:    ")
            if asignatura_modificada != "" :            
                asignaturas[numero_asignatura - 1] = asignatura_modificada
                print("asignatura no encontrada")
            datos_guardar = f"asignaturas = {asignaturas}"
            guardar_asignatura = {datos_guardar}
    except:
        print("valor no corresponde")



def eliminar_asignatura():
        listado_asignaturas()
    
        indicar_asignatura = input("indique el numero de la asignatura:  ")
        try:
            numero_asignatura = int(indicar_asignatura)
            asignaturas = obtener_listado_asignaturas()
            if len(asignaturas) > 0 :
                asignaturas.pop(numero_asignatura - 1)      
            datos_guardar = f"asignaturas = {asignaturas}"
            guardar_asignatura = {datos_guardar}
        except:
            print("valor no corresponde")



