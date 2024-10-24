Alumnos = {"nombre":[], "edad":[]}

for i in range(0,2):
    nombre = input("coloque su nombre: ")
    edad = int(input("coloque su edad: "))
    Alumnos["nombre"].append(nombre)
    Alumnos["edad"].append(edad)
    

print(Alumnos["nombre"])
print(Alumnos["edad"])
    
print(max(Alumnos["edad"]))

print(Alumnos["nombre"][Alumnos["edad"].index(max(Alumnos["edad"]))])