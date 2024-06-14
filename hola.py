import uuid
menu = ""
repartidoreslista = []
paqueteslista = []
class Repartidor():
    def __init__(self, rut="", nombre="", direccion="", localidad="", pais=""):
        self.rut = rut
        self.nombre = nombre
        self.direccion = direccion
        self.localidad = localidad
        self.pais = pais
    def get_rut(self):
        return self.rut

    def set_rut(self, value):
        self.rut = value

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, value):
        self.nombre = value

    def get_direccion(self):
        return self.direccion

    def set_direccion(self, value):
        self.direccion = value 

    def get_localidad(self):
        return self.localidad

    def set_localidad(self, value):
        self.localidad = value

    def get_pais(self):
        return self.pais

    def set_pais(self, value):
        self.pais = value

class Persona():
        def __init__(self, direccion="", localidad="", pais=""):
            self.direccion = direccion
            self.localidad = localidad
            self.pais = pais
            
        def set_direccion(self, value):
            self.direccion = value
        def get_direccion(self):
            return self.direccion
        def get_localidad(self):
            return self.set_localidad
        def set_localidad(self, value):
            self.localidad = value
        def get_pais(self):
            return self.pais
        def set_pais(self, value):
            self.pais = value
            pass

class Paquete():
    def __init__(self):
        self.estado = ""
        self.fecha_envio = ""
        self.fecha_entrega = ""
        self.peso = 0
        self.despachador = ""
        self.receptor = Persona("", "", "")
        self.remitente = Persona("", "", "")
        self.repartidor = Repartidor("", "", "")
        self.codigo = str(uuid.uuid4())

    def get_estado(self):
        return self.estado

    def set_estado(self, value):
        self.estado = value

    def get_fecha_envio(self):
        return self.fecha_envio

    def set_fecha_envio(self, value):
        self.fecha_envio = value

    def get_fecha_entrega(self):
        return self.fecha_entrega

    def set_fecha_entrega(self, value):
        self.fecha_entrega = value

    def get_costo(self):
        return self.costo
    
    def get_peso(self):
        return self.peso
    
    def set_peso(self, value):
        self.peso = value
        if self.peso > 1:
            precio_base = 1800
            costo_extra = (self.peso - 1) * 1000
            self.costo = precio_base + costo_extra
        else:
            self.costo = 1800

        if self.peso % 10 == 0:
            descuento = self.costo * 0.05
            self.costo = self.costo - descuento

    def get_despachador(self):
        return self.despachador
    def set_despachador(self, value):
        self.despachador = value

    def get_receptor(self):
        return self.receptor

    def set_receptor(self, value):
        self.receptor = value

    def get_remitente(self):
        return self.remitente

    def set_remitente(self, value):
        self.remitente = value

    def get_repartidor(self):
        return self.repartidor

    def set_repartidor(self, value):
        self.repartidor = value

    def __str__(self):
        return (f"Código {self.codigo}:\n"
                f"Remitente: {self.remitente.direccion}\n"
                f"Receptor: {self.receptor.direccion}\n"
                f"Fecha de Envío: {self.fecha_envio}\n"
                f"Fecha Entrega: {self.fecha_entrega}\n"
                f"Peso del Paquete: {self.peso}kg\n"
                f"Costo del Envío: {self.get_costo()}\n"
                f"Estado del Envío: {self.estado}\n"
                f"Encargado de Despacho: {self.despachador}\n"
                f"Repartidor: {self.repartidor.nombre}")


while menu != "5":
    print("******** Bienvenido a la aplicación de Envíos Instantáneos ********")
    print("1.- Ingrese un repartidor")
    print("2.- Ingrese un envío")
    print("3.- Modifique un envío")
    print("4.- Listar todos los envíos")
    print("5.- Salir")
    print("********************************************************************************")
    menu = input("Seleccione una opción: ")
    if menu == "1":
        # Obtener datos del repartidor
        rut_repartidor = input("Ingrese el RUT del repartidor: ")
        nombre_repartidor = input("Ingrese el nombre del repartidor: ")
        direccion_repartidor = input("Ingrese la dirección del repartidor: ")
        pais_repartidor = input("Ingrese el país del repartidor: ")
        repartidor = Repartidor(rut_repartidor, nombre_repartidor, direccion_repartidor, pais_repartidor)
        repartidoreslista.append(repartidor)
        print("Repartidor añadido correctamente")

    elif menu == "2":
        if repartidoreslista == []:
            print("No hay repartidores disponibles, por favor ingrese uno\n")
        else:
            # Crear un nuevo paquete
            paquete = Paquete()
            
            # Obtener datos del Paquete
            estado_paquete = input("Ingrese el estado del Paquete: ")
            envio_verificar = "no"
            while envio_verificar != "si":
                fecha_envio_paquete = input("Ingrese la fecha de envío del Paquete (Año-Mes-Día): ")
                if fecha_envio_paquete.isdigit() == False:
                    print("Ingrese fecha válida")
                else:
                    if len(fecha_envio_paquete) != 8:
                        print("Ingrese fecha válida")
                    else:
                        envio_verificar = "si"

            entrega_verificar = "no"
            while entrega_verificar != "si":
                fecha_entrega_paquete = input("Ingrese la fecha de entrega del Paquete (Año-Mes-Día): ")
                if fecha_entrega_paquete.isdigit() == False:
                    print("Ingrese fecha válida")
                else:
                    if len(fecha_entrega_paquete) != 8:
                        print("Ingrese fecha válida")
                    else:
                        entrega_verificar = "si"
                    entrega_verificar = "si"
            paquete_verificar = "no"
            while paquete_verificar != "si":
                peso_paquete = (input("Ingrese el peso del Paquete (Kg): "))
                if peso_paquete.isdigit() == False:
                    print("Ingrese un número válido")
                else:
                    peso_paquete = float(peso_paquete)
                    paquete_verificar = "si"

                
            paquete.set_estado(estado_paquete)
            paquete.set_fecha_envio(fecha_envio_paquete)
            paquete.set_fecha_entrega(fecha_entrega_paquete)
            paquete.set_peso(peso_paquete)
            
            # Obtener datos del remitente
            direccion_remitente = input("Ingrese la dirección del remitente: ")
            localidad_remitente = input("Ingrese la localidad del remitente: ")
            pais_remitente = input("Ingrese el país del remitente: ")
            remitente = Persona(direccion_remitente, localidad_remitente, pais_remitente)
            paquete.set_remitente(remitente)
            
            # Obtener datos del receptor
            direccion_receptor = input("Ingrese la dirección del receptor: ")
            localidad_receptor = input("Ingrese la localidad del receptor: ")
            pais_receptor = input("Ingrese el país del receptor: ")
            receptor = Persona(direccion_receptor, localidad_receptor, pais_receptor)
            paquete.set_receptor(receptor)
            #Obtener nombre del despachador
            despachadorinput = input("Ingrese el Despachador: ")
            paquete.set_despachador(despachadorinput)
            # Seleccionar repartidor
            print("Seleccione un repartidor a cargo del envío:")
            print("Seleccione un repartidor:")
            for iteraciones in range(len(repartidoreslista)):
                print(f"{iteraciones + 1}. {repartidoreslista[iteraciones].get_nombre()}")
            indice_repartidor = int(input("Ingrese el número del repartidor al que desee encargarle el pedido: ")) - 1
            paquete.set_repartidor(repartidoreslista[indice_repartidor])

            # Guardar el paquete
            paqueteslista.append(paquete)
            print(f"Paquete guardado correctamente con el código {paquete.codigo}")

    elif menu == "3":
        if paqueteslista == []:
            print("No se encontró ningún paquete registrado\n")
        else:
            codigo_paquete = input("Ingrese el código del envío que desea modificar: ")
            paquete = "no"
            for iteraciones in paqueteslista:
                if iteraciones.codigo == codigo_paquete:
                    paquete = iteraciones
                    break

            if paquete != "no":
                nuevo_estado = input(f"Estado actual ({paquete.get_estado()}), ingrese nuevo estado: ")
                paquete.set_estado(nuevo_estado)
                print("Estado del paquete actualizado correctamente")
            else:
                print("Paquete no encontrado")

    elif menu == "4":
        # Listar todos los envíos
        if paqueteslista == []:
           print("No se encontró ningún paquete registrado\n")
        else:
            for paquetes in paqueteslista:
                print(paquetes)
            print()
print("Adiós!")