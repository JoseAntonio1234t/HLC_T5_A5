class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
class Biblioteca:
    def __init__(self):
        self.libros = []
    def agregar_libro(self, titulo, autor):
        nuevo_libro = Libro(titulo, autor)
        self.libros.append(nuevo_libro)
        return f"Libro agregado: {titulo} - {autor}"
    def mostrar_libro(self):
        for libro in self.libros:
            print(f"{libro.titulo} - {libro.autor}")
biblio = Biblioteca()
biblio.agregar_libro("1984", "George Orwell")
biblio.agregar_libro("Cien Años de Soledad", "Gabriel García Márquez")
biblio.mostrar_libro()