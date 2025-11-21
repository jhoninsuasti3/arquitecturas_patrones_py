class User:
    def __init__(self, name, identification):
        self.name = name
        self.identification = identification

    def solicitar_libro(self, titulo):
        return f"Solicitud de libro '{titulo}' realizada."
    
class Studen(User):
    def __init__(self, name, identification, carrear):
        super().__init__(name,identification, identification)
        self.carrear = carrear 
        self.limit_books = 3
        self.amount_books = []

    def solicitar_libro(self, title):
        if len(self.amount_books) < self.limit_books:
            self.amount_books.append(title)
            return f"Préstamo del libro '{title}' autorizado."
        else:
            return f"No puedes prestar más libros. Límite alcanzado: {self.limit_books}."

class Professor():
    def __init__(self, name, identification):
        super().__init__(name, identification)
        self.limit_books = None

    def solicitar_libro(self, title):
        self.libros_prestados.append(title)
        return f"Préstamo del libro '{title}' autorizado."
