class persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
       
    def presentacion(self):
        return f"Mi amigo se llama {self.nombre} tiene {self.edad} aÃ±os y su profesiÃ³n es ser {self.profesion}"
    
class trabajador(persona):
    def __init__(self, nombre, edad, profesion, empresa1):
        super().__init__(nombre, edad, profesion)
        self.empresa1 = empresa1
    def presentacion2(self):
        return f"Mi amigo se llama {self.nombre} tiene {self.edad} aÃ±os y su profesiÃ³n es ser {self.profesion} y trabaja en {self.empresa1}"
    
p = persona("Manuel Morales", 17, "futbolista")
t = trabajador("Manuel Morales", 17, "futbolista","El Pozo")
print(t.presentacion2())