alumnoslista = []
nombreslista = []
class Estudiante():
    def __init__(self, nombre="", apellido="", edad="", rut="", materia="", nota="", estado=""):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.rut = rut
        self.materia = materia
        self.nota = nota
        self.estado = estado

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, value):
        self.nombre = value

    def get_apellido(self):
        return self.apellido

    def set_apellido(self, value):
        self.apellido = value

    def get_edad(self):
        return self.edad

    def set_edad(self, value):
        self.edad = value

    def get_rut(self):
        return self.rut

    def set_rut(self, value):
        self.rut = value

    def get_materia(self):
        return self.materia

    def set_materia(self, value):
        self.materia = value

    def set_nota(self, value):
        self.nota = value

    def get_nota(self):
        return self.nota
    
    def set_estado(self, value):
        self.estado = value
    
    def get_estado(self):
        return self.estado
    
    def __str__(self):
        return  (f"******** Notas Estudiantes ********\n"
                f"Estudiante:\n"
                f"Rut: {self.rut}\n"
                f"Nombre: {self.nombre}\n"
                f"Edad: {self.edad}\n"
                f"Nota: {self.nota}\n"
                f"Estado: {self.estado}\n"
                f"Materia: {self.materia}\n")

def menu():
    menu = ""
    while menu != "si":
        print("******** Bienvenido a la aplicación de Sistema de Notas ********")
        print("1.- Ingrese un Alumno.")
        print("2.- Ingresar notas de Alumno.")
        print("3.- Listar Notas de Alumnos.")
        print("4.- Salir")
        print("******************************************************************")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            estudiante = Estudiante()
            nombrealumno = input("Ingrese el nombre del alumno: ")
            apellidolumno = input("Ingrese el apellido del alumno: ")
            edadalumno = input("Ingrese la edad del alumno: ")
            rutalumno = input("Ingrese el rut del alumno: ")
            materiaalumno = input("Ingrese la materia del alumno: ")
            estudiante.set_nombre(nombrealumno)
            estudiante.set_apellido(apellidolumno)
            estudiante.set_edad(edadalumno)
            estudiante.set_rut(rutalumno)
            estudiante.set_materia(materiaalumno)
            alumnoslista.append(estudiante)
            nombreslista.append(nombrealumno)
            print("Datos guardados")
        elif opcion == "2":
            for nombres in range(len(nombreslista)):
                print(f"{nombres+1}. {nombreslista[nombres]}")
            seleccion = int(input("Ingrese un alumno: "))-1
            estudiante = alumnoslista[seleccion]
            nota1 = float(input("Ingrese la nota 1 (40%): "))
            nota2 = float(input("Ingrese la nota 2 (40%): "))
            nota3 = float(input("Ingrese la nota 3 (10%): "))
            nota4 = float(input("Ingrese la nota 4 (10%): "))
            promedio = nota1 * 0.4 + nota2 * 0.4 + nota3* 0.1 + nota4 * 0.1
            if promedio >= 4.0:
                estudiante.set_estado("Aprobado")
                estudiante.set_nota(promedio)
            else:
                estudiante.set_estado("Reprobado")
                estudiante.set_nota(promedio)
        elif opcion == "3":
            estudiante = Estudiante()
            for alumnos in alumnoslista:
                print(alumnos)
menu()