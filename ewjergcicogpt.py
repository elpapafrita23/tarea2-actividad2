usuarioslista = []
libroslista = []
librosnombres = []
class Usuario():
    def __init__(self, nombre="", idusuario=""):
        self.nombre = nombre
        self.idusuario = idusuario
    def set_nombre(self, value):
        self.nombre = value
    def get_nombre(self):
        return self.nombre
    
    def set_idusuario(self, value):
        self.idusuario = value
    def get_idusuario(self):
        return self.idusuario
    def __str__(self):
        return (f"hola {self.nombre}, id {self.idusuario}")
    
class Libro():
    def __init__(self, titulo="", autor="", isbn="", estado=False):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.estado = estado
    def set_titulo(self, value):
        self.titulo = value
    def get_titulo(self):
        return self.titulo
    
    def set_autor(self, value):
        self.autor = value
    def get_autor(self):
        return self.autor
    
    def set_isbn(self, value):
        self.isbn = value
    def get_isbn(self):
        return self.isbn
    def set_estado(self, value):
        self.estado = value
    def get_estado(self):
        return self.estado
    def __str__(self):
        return f"Ha guardado {self.titulo}, del autor {self.autor} con el ibsn {self.isbn}"
def menu():
    menu = ""
    while menu != "si":
        print("1)Registrar usuario")
        print("2)Ingresar como usuario")
        print("3)Registrar un libro")
        print("4)Listar libros")
        print("5)Tomar libro prestado")
        print("6)Devolver libro")
        print("7)Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            nombreusu = input("Ingrese el nombre de usuario: ")
            idusu = input("Ingrese el id de usuario: ")
            usuarioslista.append(Usuario(nombreusu, idusu))
            print(f"Usuario '{nombreusu}' registrado con ID '{idusu}'.")
        elif opcion == "2":
            ingresousu = input("Ingrese el nombre de usuario: ")
            ingresoidusu = input("Ingrese el id de usuario: ")
            for usuarios in usuarioslista:
                if usuarios.nombre == ingresousu and usuarios.idusuario == ingresoidusu:
                    print("Ingreso exitoso")
                else:
                    print("Las creedenciales son invalidas")
        elif opcion == "3":
            libro = Libro()
            tituloingreso = input("Ingrese el título del libro: ")
            autoringreso = input("Ingrese el autor del libro: ")
            isbningreso = input("Ingrese el IBSN del libro: ")
            libro.set_titulo(tituloingreso)
            librosnombres.append(libro)
            libro.set_autor(autoringreso)
            libro.set_isbn(isbningreso)
            libroslista.append(libro)
            print(libro)
        elif opcion == "4":
            for libros in libroslista:
                print(libros)
        elif opcion == "5":
            for libros in libroslista:
                if libros.estado == False:
                    for iteraciones in range(len(librosnombres)):
                        print("Libros disponibles")
                        print(f"{iteraciones + 1}. {libroslista[iteraciones].get_titulo()}")
                        input("Seleccione el libro que desee elegir: ")
                        libro.set_estado(True)
        elif opcion == "6":
            libro = Libro()
            for libros in libroslista:
                if libros.estado == True:
                    for iteraciones in range(len(librosnombres)):
                        print("Libros a devolver")
                        print(f"{iteraciones + 1}. {libroslista[iteraciones].get_titulo()}")
                        opcion = int(input("Ingrese libro: "))- 1
                        libroslista[opcion].set_estado(False)
        elif opcion == "7":
            print("Adiós!")
            menu = "si"
menu()