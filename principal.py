from auxiliares.version import version_actual
from datos.asignatura import asignatura


def menu_principal():
    print()
    print(f"aplicacion gestion de notas {version_actual}")
    print("=============================================")                  

    
    while True:
        print("""
              [1] gestion asignatura
              [2] gestion docentes
              [3] gestion estudiantes
              [4] gestion notas
              [0] salir""")
        print("""
              ================================================""")
        opcion = input("seleccione una opcion")
        if opcion =="1":
            contador=1
            for asig in asignatura:
                
                print(f"{contador} {asig}")
                contador += 1
            
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
        
        
        
    
menu_principal()    