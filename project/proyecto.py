import re

pattern = r"^(Calle|Carrera|Diagonal|Transversal|Avenida|Autopista|Circunvalar|Kilometro|Vereda|Cll|Kr|Crr|Dg|Tv|Av|At|Ccv|Km)" \
          r"\s([0-9]{1,3}|[a-zA-Z]{0,15})\s?([a-zA-Z])?\s?(bis)?" \
          r"\s?(Este|Oeste|Norte|Sur|Occidente)?\s?(#|No|N°)" \
          r"\s?([0-9]{1,3})\s?([a-zA-Z]?)\s?\-\s?([0-9]{1,3})" \
          r"\s?([a-zA-Z]?)\s?([a-zA-Z]{0,20})\s?([0-9]{1,3}?)$"

text_file = open("arch.txt", "r")
address = text_file.readlines()
text_file.close()
print(address);

for i in range(0, len(address)):
    result = re.match(pattern, address[i], re.IGNORECASE)
    if result:
        print("Direccion correcta")
        print(address[i])
    else:
        print("Dirrecion incorrecta bruto")
        print(address[i])