from subprocess import check_output
from os import system
mensajes={"inicio":"INICIANDO EL GESTOR DE MODULOS PARA PYTHON",
        "opcion":"Instalr/Desinstalar/Buscar modulos instalados[I/D/B] --> ",
        "modulo":"Modulo --> "
          }

def limpiar_pantalla():
    system("cls")

def comprobar_modulo(modulo):
    try:
        exec(f"import {modulo}")
        return True
    except Exception as e:
        print(e)
        return False
def instalar(lista):
    no_inst=[]
    inst=[]
    ya_inst=[]
    for modulo in lista:
        if comprobar_modulo(modulo):
            print(f"{modulo} ya estaba instalado")
            ya_inst.append(modulo)
        else:
            try:
                print(f">>> Iniciando instalación de: {modulo}")
                consola=check_output("py -m pip install "+modulo,shell=True)
                print(consola)
                
            except Exception as e:
                print(f"ERROR!:Fallo en la instalación de: {modulo}")
                print("Exception:")
                print(e)
            if comprobar_modulo(modulo):
                inst.append(modulo)
            else:
                no_inst.append(modulo)
        print("#"*50)
    print(f"MODULOS QUE YA ESTABAN INSTALADOS: {len(ya_inst)}/{len(lista)}:D")
    print("_"*50)
    for modulo in ya_inst:
        print("-"+modulo)
    print("\n")
    print("#"*50)
    print(f"MODULOS INSTALADOS CORRECTAMENTE: {len(inst)}/{len(lista)}:D")
    print("_"*50)
    for modulo in inst:
        print("-"+modulo)
    print("\n")
    print("#"*50)
    print(f"MODULOS QUE NO SE HAN INSTALADO: {len(no_inst)}/{len(lista)}:C")
    print("_"*50)
    for modulo in no_inst:
        print("-"+modulo)
    print("\n")
    print("#"*50)
def desinstalar(lista):
    no_inst=[]
    inst=[]
    for modulo in lista:
        try:
            print(f">>> Iniciando des-instalación de: {modulo}")
            consola=check_output("py -m pip uninstall -y "+modulo,shell=True)
            print(consola)
            inst.append(modulo)
        except Exception as e:
            print(f"ERROR!:Fallo en la des-instalación de: {modulo}")
            print("Exception:")
            print(e)
            no_inst.append(modulo)
            
        print("#"*50)
    print(f"Modulos des-instalados correctamente: {len(inst)}/{len(lista)}:D")
    for modulo in inst:
        print(modulo)
    print("#"*50)
    print(f"Modulos NO des-instalados: {len(no_inst)}/{len(lista)}:C")
    for modulo in no_inst:
        print(modulo)

def p():
    print(mensajes["inicio"])
    i=input(mensajes["opcion"])
    while i!="":
        limpiar_pantalla()
        lista_modulos=[]
        if i.lower()=="i":
            print("INSTALAR UN MODULO")
            t=input(mensajes["modulo"])
            while t!="":
                lista_modulos.append(t)
                t=input("Modulo --> ")
            print("INICIANDO INSTALACIÓN")
            print("#"*50)
            instalar(lista_modulos)
        elif i.lower()=="d":
            print("DES-INSTALAR UN MODULO")
            t=input(mensajes["modulo"])
            while t!="":
                lista_modulos.append(t)
                t=input("Modulo --> ")
            print("INICIANDO DESINSTALACIÓN")
            print("#"*50)
            desinstalar(lista_modulos)
        elif i.lower()=="b":
            print("BUSCAR UN MODULO")
            help('modules')
        i=input(mensajes["opcion"])

