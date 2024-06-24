import uuid
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
        def __init__(self, direccion="", localidad="", pais="", rut="", nombre= ""):
            self.direccion = direccion
            self.localidad = localidad
            self.pais = pais
            self.rut = rut
            self.nombre = nombre
            
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
        def get_rut(self):
            return self.rut
        def set_rut(self, value):
            self.rut = value
        def get_pais(self):
            return self.pais
        def set_pais(self, value):
            self.pais = value

class Paquete():
    def __init__(self):
        self.estado = ""
        self.fecha_envio = ""
        self.fecha_entrega = ""
        self.peso = 0
        self.despachador = ""
        self.receptor = Persona()
        self.remitente = Persona()
        self.repartidor = Repartidor()
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
                f"Remitente: {self.remitente.rut}, {self.remitente.nombre}, {self.remitente.direccion}, {self.remitente.pais}, {self.remitente.localidad}\n"
                f"Receptor: {self.receptor.rut}, {self.receptor.nombre}, {self.receptor.direccion}, {self.receptor.pais}, {self.receptor.localidad}\n"
                f"Fecha de Envío: {self.fecha_envio}\n"
                f"Fecha Entrega: {self.fecha_entrega}\n"
                f"Peso del Paquete: {self.peso}kg\n"
                f"Estado del Envío: {self.estado}\n"
                f"Encargado de Despacho: {self.despachador}\n"
                f"Repartidor: {self.repartidor.nombre}")

menu = ""
repartidoreslista = []
paqueteslista = []

while menu != "5":
    entregado = ""
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
        rutrepartidorverif = "no"
        while rutrepartidorverif != "si":
            rut_repartidor = input("Ingrese el RUT del repartidor: ")
            if rut_repartidor.split("-"):
                rutrepartidorverif = "si"  
            else:
                print("Ingrese rut válido porfavor")
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
            # crear paquete
            paquete = Paquete()
            
            # obtener datos del Paquete
            estadopaqueteverificar = "no"
            while estadopaqueteverificar != "si":
                estado_paquete = input("Ingrese el estado del Paquete (En tránsito, No entregado, Entregado, Sin registro): ").lower()
                if estado_paquete == "en tránsito" or estado_paquete == "no entregado" or estado_paquete == "en transito" or estado_paquete == "sin registro":
                    estadopaqueteverificar = "si"
                elif estado_paquete == "entregado":
                    estadopaqueteverificar = "si"
                    entregado = "si"
                else:
                    print("Ingrese un estado de paquete válido : ")
            envio_verificar = "no"
            while envio_verificar != "si":
                fecha_envio_paquete = input("Ingrese la fecha de envío del Paquete (Año-Mes-Día): ")
                if fecha_envio_paquete.split("-") == False:
                    print("Ingrese fecha válida")
                else:
                    if len(fecha_envio_paquete) != 10:
                        print("Ingrese fecha válida")
                    else:
                        envio_verificar = "si"

            entrega_verificar = "no"
            while entrega_verificar != "si":
                if entregado == "si":
                    fecha_entrega_paquete = input("Ingrese la fecha de entrega del Paquete (Año-Mes-Día): ")
                    if fecha_entrega_paquete.split("-") == False:
                        print("Ingrese fecha válida")
                    elif len(fecha_entrega_paquete) != 10:
                            print("Ingrese fecha válida")
                    else:
                        entrega_verificar = "si"
                else:
                    fecha_entrega_paquete = "No entregado aún"
                    entrega_verificar = "si"
            paquete_verificar = "no"
            while paquete_verificar != "si":
                peso_paquete = (input("Ingrese el peso del Paquete (Kg): "))
                if peso_paquete.isdigit() == False:
                    print("Ingrese un número válido")
                else:
                    if float(peso_paquete)<0:
                        print("Ingrese un número válido")
                    else:
                        peso_paquete = float(peso_paquete)
                        paquete_verificar = "si"

                
            paquete.set_estado(estado_paquete)
            paquete.set_fecha_envio(fecha_envio_paquete)
            paquete.set_fecha_entrega(fecha_entrega_paquete)
            paquete.set_peso(peso_paquete)
            
            # obtener datos del remitente
            rutremitenteverif = "no"
            while rutremitenteverif != "si":
                rut_remitente = input("Ingrese el RUT del remitente: ")
                if rut_remitente.split("-"):
                    rutremitenteverif = "si"
                else:
                    print("Ingrese RUT válido porfavor")
            nombre_remitente = input("Ingrese el nombre del remitente: ")
            direccion_remitente = input("Ingrese la dirección del remitente: ")
            localidad_remitente = input("Ingrese la localidad del remitente: ")
            pais_remitente = input("Ingrese el país del remitente: ")
            remitente = Persona(direccion_remitente, localidad_remitente, pais_remitente, rut_remitente, nombre_remitente)
            paquete.set_remitente(remitente)
            
            # obtener datos del receptor            
            rutreceptorverif = "no"
            while rutreceptorverif != "si":
                rut_receptor = input("Ingrese el RUT del receptor: ")
                if rut_receptor.split("-"):
                    rutreceptorverif = "si"
                else:
                    print("Ingrese rut válido porfavor")
            nombre_receptor = input("Ingrese el nombre del receptor: ")
            direccion_receptor = input("Ingrese la dirección del receptor: ")
            localidad_receptor = input("Ingrese la localidad del receptor: ")
            pais_receptor = input("Ingrese el país del receptor: ")
            receptor = Persona(direccion_receptor, localidad_receptor, pais_receptor, rut_receptor, nombre_receptor)
            paquete.set_receptor(receptor)
            #obtener nombre del despachador
            despachadorinput = input("Ingrese el Despachador: ")
            paquete.set_despachador(despachadorinput)
            # seleccionar repartidor
            print("Seleccione un repartidor a cargo del envío:")
            print("Seleccione un repartidor:")
            for iteraciones in range(len(repartidoreslista)):
                print(f"{iteraciones + 1}. {repartidoreslista[iteraciones].get_nombre()}")
            repartidorverificar = "no"
            while repartidorverificar != "si":
                indice_repartidor = (input("Ingrese el número del repartidor al que desee encargarle el pedido: "))
                if indice_repartidor.isdigit() == True:
                    indice_repartidor = int(indice_repartidor) -1
                    if 0 <= indice_repartidor < len(repartidoreslista):
                        paquete.set_repartidor(repartidoreslista[indice_repartidor])
                        paqueteslista.append(paquete)
                        print(f"Paquete guardado correctamente con el código {paquete.codigo}")
                        repartidorverificar = "si"
                    else:
                        print("Elija un repartidor por favor")
                else:
                    print("Elija un repartidor por favor")
            

    elif menu == "3":
        if paqueteslista == []:
            print("No se encontró ningún envío registrado\n")
        else:
            codigo_paquete = input("Ingrese el código del envío que desea modificar: ")
            paquete = "no"
            for codigos in paqueteslista:
                if codigos.codigo == codigo_paquete:
                    paquete = codigos
                    break

            if paquete != "no":
                if paquete.get_estado() == "entregado":
                    nuevoenvio_verificar = "no"
                    while nuevoenvio_verificar != "si":
                        nuevo_estado = input(f"Estado actual ({paquete.get_estado()}), ingrese nuevo estado del envío: ").lower()
                        if nuevo_estado == "en transito" or nuevo_estado == "no entregado" or nuevo_estado == "en tránsito":
                            paquete.set_estado(nuevo_estado)
                            nuevoenvio_verificar = "si"
                        else:
                            print("Ingrese nuevo estado válido")
                    nuevafecha_verificar = "no"
                    while nuevafecha_verificar != "si":
                        nueva_fecha = input(f"Fecha actual ({paquete.get_fecha_entrega()}), ingrese una nueva fecha de entrega: ").lower()
                        if nueva_fecha.split("-") == False:
                            print("Ingrese fecha válida")
                        elif len(fecha_envio_paquete) != 10:
                            print("Ingrese fecha válida")
                        else:
                            paquete.set_fecha_entrega(nueva_fecha)
                            print("Paquete actualizado correctamente")
                            nuevafecha_verificar = "si"
                else:
                    print("El paquete no fué entregado aún")
            else:
                print("Paquete no encontrado")

    elif menu == "4":
        # listar todos los envios
        if paqueteslista == []:
           print("No se encontró ningún envío registrado\n")
        else:
            for paquetes in paqueteslista:
                print(paquetes)
            print()
print("Adiós!")