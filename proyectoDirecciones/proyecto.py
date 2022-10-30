import re

pattern =pattern = r"^(Calle|Carrera|Diagonal|diag|Transversal|Avenida|Autopista|Circunvalar|Kilometro|tr|Cll|cl|cl|cr|Kr|Crr|Dg|Tv|Av|At|Ccv|Km)\.?" \
          r"\s([0-9]{1,3}|[a-zA-Z]{0,15})\s?([a-zA-Z]{0,15})?\s?([a-zA-Z])?(bis)?\s?([a-zA-Z])?" \
          r"\s?([0-9]{1,3}|Este|Oeste|Norte|sur|Occidente|nte|occ|o)?\s?(#|No|N°)" \
          r"\s?([0-9]{1,3})\s?([a-zA-Z]{0,5}?)\s?\-?\s?([0-9]{1,3})" \
          r"\s?([a-zA-Z]?)\s?([a-zA-Z]{0,20})\s?([0-9]{1,3}?\s(bis|Este|Oeste|Norte|sur|Occidente)?)" \
          r"\s?(apto|apartamento|piso|edificio|barrio|bloque|interior|int|int)?\.?\s?\s?([a-zA-Z])?\s?" \
          r"([a-zA-Z])?\s?([a-zA-Z]{0,15})?" \
          r"(Torre)?\s?([0-9]{1,3})?$"

pattern2 = r"^(vereda)" \
           r"\s([a-zA-Z]{0,20})\s?([a-zA-Z]{0,20})" \
           r"\s(sector)\s?([a-zA-Z]{0,15})?"\
           r"\s([a-zA-Z]{0,20})" \
           r"\s([0-9]{1,3})?$"

def leerArchivo(path):
    text_file = open(path, "r")
    address = text_file.readlines()
    text_file.close()
    return address

def validarDirecciones(address):
    for i in range(0, len(address)):
        result = re.match("vereda", address[i], re.IGNORECASE)
        if result:
            validacionRural = re.match(pattern2, address[i], re.IGNORECASE)
            if validacionRural:
                print("Direccion rural correcta")
                print(address[i])
            else:
                print("Direccion rural incorrecta")
                print(address[i])
        else:
            validacionUrbana = re.match(pattern, address[i], re.IGNORECASE)
            if validacionUrbana:
                print("Dirrecion urbana correcta")
                print(address[i])
            else:
                print("Dirrecion urbana incorrecta")
                print(address[i])

#addresses = leerArchivo("arch.txt")
#validarDirecciones(addresses)