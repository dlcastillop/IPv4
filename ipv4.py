from sys import argv, exit
from ipv4_subnetting import *

# Mostrar opciones del programa
if argv[1] == '?':
    print("""python ipv4.py [OPCIONES...]
    Determinar ID de subred, dirección broadcast y/o rango de direcciones asignables.
        Opciones:
            -b IP máscara           Determina la dirección broadcast
            -i IP máscara           Determina el ID de subred
            -r IP máscara           Determina el rango de direcciones asignables
            -t IP máscara           Determina el ID de subred, la dirección broadcast y el rango de direcciones
                                    asignables
                                                    
        Notas:
            1. Se pueden combinar las opciones -i, -b y -r. Por ejemplo: -ib mostrará el ID de subred y la dirección
             broadcast
            2. La máscara se puede introducir en formato DDN (ejemplo: 255.0.0.0) o formato de prefijo (ejemplo: 8)
    """)
    exit(0)

# Obtener IP
ip = argv[2]

# Obtener máscara
if mascara_ddn(argv[3]) is None:
    mascara = argv[3]
else:
    mascara = mascara_ddn(argv[3])

# Validar que la dirección IP y la máscara son válidas
if not validar_ip(ip) and not validar_subnetting(ip) and not validar_mascara(mascara):
    print("Error. Has introducido una dirección IP y una máscara no válidas.")
    exit(0)
elif not validar_ip(ip) and not validar_subnetting(ip):
    print("Error. Has introducido una dirección IP no válida.")
    exit(0)
elif not validar_mascara(mascara):
    print("Error. Has introducido una máscara no válida.")
    exit(0)

# Opción -b
if argv[1] == '-b':
    print(dir_broadcast(ip, mascara))

# Opción -i
elif argv[1] == '-i':
    print(id_subred(ip, mascara))

# Opción -r
elif argv[1] == '-r':
    print(f"{primera_dir(ip, mascara)} - {ultima_dir(ip, mascara)}")

# Opción -t
elif argv[1] == '-t':
    print(f"ID de subred: {id_subred(ip, mascara)}")
    print(f"Dirección broadcast: {dir_broadcast(ip, mascara)}")
    print(f"Rango: {primera_dir(ip, mascara)} - {ultima_dir(ip, mascara)}")

# Combinaciones de -b y -i
elif argv[1] == '-bi' or argv[1] == '-ib':
    print(f"ID de subred: {id_subred(ip, mascara)}")
    print(f"Dirección broadcast: {dir_broadcast(ip, mascara)}")

# Combinaciones de -b y -r
elif argv[1] == '-br' or argv[1] == '-rb':
    print(f"Dirección broadcast: {dir_broadcast(ip, mascara)}")
    print(f"Rango: {primera_dir(ip, mascara)} - {ultima_dir(ip, mascara)}")

# Combinaciones de -i y -r
elif argv[1] == '-ir' or argv[1] == '-ri':
    print(f"ID de subred: {id_subred(ip, mascara)}")
    print(f"Rango: {primera_dir(ip, mascara)} - {ultima_dir(ip, mascara)}")
