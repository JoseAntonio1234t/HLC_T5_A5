#Ejercicio 1
class persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
       
    def presentacion(self):
        return f"Mi amigo se llama {self.nombre} tiene {self.edad} años y su profesión es ser {self.profesion}"
    
p = persona("Manuel Morales", 17, "futbolista")

#Ejercicio 2 usando heredando el 1
class estudiante(persona):
    def __init__(self, nombre, edad, profesion, asignatura):
        super().__init__(nombre, edad, profesion)
        self.asignatura = asignatura
    def presentacion2(self):
        return f"Mi amigo se llama {self.nombre} tiene {self.edad} años y su profesión es ser {self.profesion} y su asignatura es {self.asignatura}"

e = estudiante("Marc Montoro", 17, "carnicero", "HLC")
print(p.presentacion())
print(e.presentacion2())

#Ejercicio 3

