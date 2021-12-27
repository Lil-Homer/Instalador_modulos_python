from subprocess import check_output
def instalar(lista):
    no_inst=[]
    inst=[]
    for modulo in lista:
        try:
            print(f">>> Iniciando instalación de: {modulo}")
            consola=check_output("py -m pip install "+modulo,shell=True)
            print(consola)
            inst.append(modulo)
        except Exception as e:
            print(f"ERROR!:Fallo en la instalación de: {modulo}")
            print("Exception:")
            print(e)
            no_inst.append(modulo)
            
        print("#"*50)
    print(f"Modulos instalados correctamente: {len(inst)}/{len(lista)}:D")
    for modulo in inst:
        print(modulo)
    print("#"*50)
    print(f"Modulos NO instalados: {len(no_inst)}/{len(lista)}:C")
    for modulo in no_inst:
        print(modulo)

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
    i=input("Instalr/Desinstalar[I/D] --> ")
    while i!="":
        lista_modulos=[]
        if i=="i":
            t=input("Modulo --> ")
            while t!="":
                lista_modulos.append(t)
                t=input("Modulo --> ")
            print("INICIANDO INSTALACIÓN")
            print("#"*50)
            instalar(lista_modulos)
        elif i=="d":
            t=input("Modulo --> ")
            while t!="":
                lista_modulos.append(t)
                t=input("Modulo --> ")
            print("INICIANDO DESINSTALACIÓN")
            print("#"*50)
            desinstalar(lista_modulos)
        i=input("Instalr/Desinstalar[I/D] --> ")
p()
