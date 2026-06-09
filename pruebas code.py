# CLASE 1: El auto que se va a modificar
class VehiculoProyecto:
    def __init__(self, id_vehiculo, marca_modelo, año, hp_stock, angulo_giro):
        self.id_vehiculo = id_vehiculo
        self.marca_modelo = marca_modelo
        self.año = año
        self.hp_stock = hp_stock
        self.__hp_actuales = hp_stock  # Al principio llega con los mismos HP de fábrica
        self.angulo_giro = angulo_giro
        self.estado_proyecto = "Stock"  # Estado inicial por defecto

    def actualizar_estado(self, nuevo_estado):
        # Cambia el texto del estado por uno nuevo
        self.estado_proyecto = nuevo_estado
        print(f"-> El auto {self.marca_modelo} cambió a estado: {nuevo_estado}")

    def incrementar_rendimiento(self, hp_ganados, extra_angulo):
        # Suma los nuevos HP y ángulo a los que ya tenía el auto
        self.__hp_actuales = self.__hp_actuales + hp_ganados
        self.angulo_giro = self.angulo_giro + extra_angulo
        print(f" ¡Auto Potenciado! Ahora tiene {self.__hp_actuales} HP y {self.angulo_giro}° de giro.")

    def generar_ficha_tecnica(self):
        # Muestra un resumen simple del auto en la pantalla
        print(f"--- FICHA DE {self.marca_modelo} ---")
        print(f"Estado: {self.estado_proyecto}")
        print(f"HP Actuales: {self.__hp_actuales} (Llegó con: {self.hp_stock})")
        print(f"Ángulo de Giro: {self.angulo_giro}°")
        print("---------------------------------")

    def obtener_hp(self):
        return self.__hp_actuales

from abc import ABC, abstractmethod

# Clase abstracta
class Persona(ABC):

    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def mostrar_tipo(self):
        pass

# CLASE 2: El dueño del auto (Piloto)
class PilotoCliente(Persona):

    def __init__(self, id_cliente, nombre, presupuesto_maximo):
        super().__init__(nombre)

        self.id_cliente = id_cliente
        self.presupuesto_maximo = presupuesto_maximo
        self.dinero_invertido = 0.0

    def mostrar_tipo(self):
        print("Soy un cliente")

    def verificar_presupuesto(self, monto_a_gastar):

        if monto_a_gastar <= self.presupuesto_maximo:
            return True
        else:
            return False

    def actualizar_inversion(self, monto):

        self.dinero_invertido = self.dinero_invertido + monto
        print(f"{self.nombre} ha gastado un total de: ${self.dinero_invertido}")


# CLASE 3: Las piezas tuning (Componentes)
class ComponentePerformance:
    def __init__(self, id_componente, nombre_pieza, precio, aporte_hp, aporte_angulo, stock):
        self.id_componente = id_componente
        self.nombre_pieza = nombre_pieza
        self.precio = precio
        self.aporte_hp = aporte_hp
        self.aporte_angulo = aporte_angulo
        self.stock_disponible = stock

    def reducir_stock(self, cantidad):
        # Resta las piezas usadas del inventario
        self.stock_disponible = self.stock_disponible - cantidad
        print(f" Quedan {self.stock_disponible} unidades de {self.nombre_pieza} en stock.")

# CLASE 4: El mecánico del taller
class TunerMecanico(Persona):

    def __init__(self, id_mecanico, nombre, especialidad):
        super().__init__(nombre)

        self.id_mecanico = id_mecanico
        self.especialidad = especialidad
        self.proyectos_asignados = 0

    def mostrar_tipo(self):
        print("Soy un mecanico")

    def asignar_proyecto(self):

        self.proyectos_asignados = self.proyectos_asignados + 1
        print(f"Mecánico {self.nombre} tomó un nuevo trabajo. Total a cargo: {self.proyectos_asignados}")

    def liberar_mecanico(self):

        self.proyectos_asignados = self.proyectos_asignados - 1
        print(f"Mecánico {self.nombre} terminó un trabajo. Total a cargo: {self.proyectos_asignados}")


# CLASE 5: La Orden de Trabajo (Une a todas las clases anteriores)
class OrdenModificacion:
    def __init__(self, id_orden, vehiculo_objeto, piloto_objeto, mecanico_objeto, costo_mano_obra):
        self.id_orden = id_orden
        self.vehiculo = vehiculo_objeto  # Recibe un objeto de la clase VehiculoProyecto
        self.piloto = piloto_objeto      # Recibe un objeto de la clase PilotoCliente
        self.mecanico = mecanico_objeto  # Recibe un objeto de la clase TunerMecanico
        self.costo_mano_obra = costo_mano_obra
        self.lista_componentes = []      # Lista vacía para ir guardando las piezas
        self.estado_orden = "Abierta"

        # Al crear la orden, le asignamos automáticamente el trabajo al mecánico
        self.mecanico.asignar_proyecto()

    def agregar_componente(self, componente_objeto):
        # 1. Validar que haya stock de la pieza
        if componente_objeto.stock_disponible <= 0:
            print(f"No se puede agregar {componente_objeto.nombre_pieza}. ¡No hay stock!")
            return

        # 2. Calcular cuánto costaría sumando esta pieza
        costo_temporal = self.costo_mano_obra + componente_objeto.precio
        
        # 3. Validar si al piloto le alcanza el dinero
        if self.piloto.verificar_presupuesto(costo_temporal) == True:
            # Si pasa las pruebas, agregamos la pieza a la lista y bajamos el stock
            self.lista_componentes.append(componente_objeto)
            componente_objeto.reducir_stock(1)
            print(f"{componente_objeto.nombre_pieza} agregada con éxito a la orden.")
        else:
            print(f"{self.piloto.nombre} no tiene presupuesto suficiente para esta pieza.")

    def finalizar_trabajo(self):

    if self.estado_orden == "Entregado":
        print("La orden ya fue finalizada.")
        return

    print(f"\n--- FINALIZANDO ORDEN N° {self.id_orden} ---")

    total_piezas = 0

    for pieza in self.lista_componentes:

        self.vehiculo.incrementar_rendimiento(
            pieza.aporte_hp,
            pieza.aporte_angulo
        )

        total_piezas = total_piezas + pieza.precio

    costo_total_final = total_piezas + self.costo_mano_obra

    self.piloto.actualizar_inversion(costo_total_final)
    self.vehiculo.actualizar_estado("Listo para Pista")
    self.mecanico.liberar_mecanico()

    self.estado_orden = "Entregado"

    print("-----------------------------------------\n")


# SIMULACIÓN / PRUEBA DE FUNCIONAMIENTO (Para ver cómo interactúan)
# Creamos las entidades básicas
auto1 = VehiculoProyecto(101, "Nissan Silvia S15", 2002, 250, 45)
piloto1 = PilotoCliente("11.111.111-1", "Diego Drift", 5000) # Presupuesto de 5000 dólares
mecanico1 = TunerMecanico(1, "Don Carlos", "Motores JDM")

# Creamos un par de piezas en el inventario del taller
turbo_garrett = ComponentePerformance("C-01", "Turbo Garrett G30", 2500, 150, 0, 3) # Aporta 150 HP
kit_giro = ComponentePerformance("C-02", "Kit de Ángulo Wisefab", 1200, 0, 20, 2)    # Aporta 20° de giro

# Ver cómo está el auto antes de entrar al taller
auto1.generar_ficha_tecnica()

# Creamos la orden de trabajo (Mano de obra cuesta 500 dólares)
orden1 = OrdenModificacion(1, auto1, piloto1, mecanico1, 500)

# Agregamos las piezas a la orden
orden1.agregar_componente(turbo_garrett)
orden1.agregar_componente(kit_giro)

# Finalizamos el trabajo para aplicar los cambios al auto
orden1.finalizar_trabajo()

# Ver cómo quedó el auto después del taller
auto1.generar_ficha_tecnica()
while True:

    print("\nTaller de Tuning y Performance - Menú Principal")
    print("1. Registrar vehiculo")
    print("2. Mostrar vehiculos")
    print("3. Ver tipos de personas")
    print("4. Finalizar trabajo")
    print("5. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":

        id_auto = input("Ingrese ID: ")
        modelo = input("Ingrese modelo: ")
        año = int(input("Ingrese año: "))
        hp = int(input("Ingrese HP: "))
        giro = int(input("Ingrese angulo de giro: "))

        nuevo_auto = VehiculoProyecto(
            id_auto,
            modelo,
            año,
            hp,
            giro
        )

        lista_autos.append(nuevo_auto)

        print("Vehiculo registrado correctamente.")

    elif opcion == "2":

        for auto in lista_autos:
            auto.generar_ficha_tecnica()

    elif opcion == "3":

        personas = [piloto1, mecanico1]

        for persona in personas:
            persona.mostrar_tipo()

    elif opcion == "4":

        orden1.finalizar_trabajo()

    elif opcion == "5":

        print("Programa terminado.")
        break

    else:
        print("Opcion no valida.")