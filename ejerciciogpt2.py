usuarioslista = []
tareaslista = []
tareasasignadas = []
usuariostareasasignadas = []
class Tarea():
    def __init__(self, titulo="", vencimiento="", estado=False):
        self.titulo = titulo
        self.vencimiento = vencimiento
        self.estado = estado
    def set_titulo(self, value):
        self.titulo = value
    def get_titulo(self):
        return self.titulo
    
    def set_vencimiento(self, value):
        self.vencimiento = value
    def get_vencimiento(self):
        return self.vencimiento
    
    def set_estado(self, value):
        self.estado = value
    def get_estado(self):
        return self.estado
    
class Usuario():
    def __init__(self, nombre=""):
        self.nombre = nombre
    def set_nombre(self, value):
        self.nombre = value
    def get_nombre(self):
        return self.nombre
    def __str__(self):
        return f"Hola {self.nombre}"

def menu():
    menu = "no"
    while menu != "si":
        usuario = Usuario()
        print("1)Registre usuario")
        print("2)Registrar tareas")
        print("3)Asignar tareas")
        print("4)Completar tareas")
        print("5)Consultar tareas")
        print("6)Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            nomusu = input("Ingrese su nombre: ")
            usuario.set_nombre(nomusu)
            usuarioslista.append(usuario)
            print("Guardado!")
        elif opcion == "2":
            tarea = Tarea()
            tareainput = input("Ingrese el titulo de la tarea a registrar: ")
            tarea.set_titulo(tareainput)
            tareaslista.append(tarea)
        elif opcion == "3":
            tarea = Tarea()
            for usuarios in range(len(usuarioslista)):
                print("Usuarios disponibles")
                print(f"{usuarios+1}. {usuarioslista[usuarios].get_nombre()}")
            usuariotarea = int(input("Ingrese el usuario a elegir: "))-1
            usuariostareasasignadas.append(usuarioslista[usuariotarea].get_nombre())
            print("Tareas disponibles")
            for iteraciones in range(len(tareaslista)):
                    print(f"{iteraciones+1}. {tareaslista[iteraciones].get_titulo()}")
            tareaopc = int(input("Ingrese tarea a seleccionar: "))-1
            tareasasignadas.append((tareaslista[tareaopc]).get_titulo())
            tarea.set_estado(True)
menu()