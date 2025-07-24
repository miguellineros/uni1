from auxiliares.version import version_actual
from negocio.negocio_menu import menu_principal,menu_asignaturas

from negocio.negocio_asignatura import listado_asignaturas,agregar_asignatura,modificar_asignatura,eliminar_asignatura

def programa_principal():
    print()
    print(f"aplicacion gestion de notas {version_actual}  ")
    print("=============================================")   
                   

    while True:
        menu_principal()

       
        opcion = input("seleccione una opcion")
        print()
        if opcion =="1":
            while True:
                menu_asignaturas()
                opcion_asignatura = input("seleccione una opcion      ")
                print()
                if opcion_asignatura == "1":
                    listado_asignaturas()
                elif opcion_asignatura == "2":
                    agregar_asignatura()
                elif opcion_asignatura == "3":
                    modificar_asignatura()
                elif opcion_asignatura == "4":
                    eliminar_asignatura()
                elif opcion_asignatura == "0":
                    print("volviendo al menu anterior...")
                    break
                else:
                    print("Opcion ingresada no corresponde....")

        elif opcion =="2":
            print(f"usted a seleccionado la opcion {opcion}")
            pass
        elif opcion =="3":
            print(f"usted a seleccionado la opcion {opcion}")
            pass
        elif opcion =="4":
            print(f"usted a seleccionado la opcion {opcion}")
            pass
        elif opcion== "0":
            print("saliendo")
            break
        else:
            print("opcion ingresada no corresponde")
        
        
        
    
programa_principal()    
#contador=1
#for asig in asignatura:
 #   print(f"{contador} {asig}")
  #  contador += 1

#pip install mysql-connector-python==8.0.33
  #mysql-connector-python 8.0.33