class VehiculoProyecto:
    # 1 EL CONSTRUCTOR: Aquí se crean los atributos cuando nace el objeto
    def __init__(self, marca_modelo, año, hp_stock, angulo_giro):
        self.marca_modelo = marca_modelo
        self.año = año
        self.hp_stock = hp_stock
        self.hp_actuales = hp_stock  # Al principio es igual al stock
        self.angulo_giro = angulo_giro
        self.estado_proyecto = "Stock"
        # 2. LOS MÉTODOS: Van abajo, al mismo nivel que el __init__
    def actualizar_estado(self, nuevo_estado):
        """Cambia la fase actual del proyecto de drift"""
        self.estado_proyecto = nuevo_estado
        print(f"-> Estado actualizado: El auto ahora está en: {self.estado_proyecto}")

    def incrementar_rendimiento(self, hp_ganados, extra_angulo):
        """Modifica los HP y el ángulo de giro al instalar piezas tuning"""
        self.hp_actuales += hp_ganados
        self.angulo_giro += extra_angulo
        print(f"Modificación exitosa! +{hp_ganados} HP | +{extra_angulo}° de giro.")

    def generar_ficha_tecnica(self):
        """Retorna un resumen con las specs actuales del auto"""
        return (f"--- FICHA TÉCNICA: {self.marca_modelo} ({self.año}) ---\n"
                f"Status: {self.estado_proyecto}\n"
                f"Potencia: {self.hp_actuales} HP (Stock: {self.hp_stock} HP)\n"
                f"Ángulo de Giro: {self.angulo_giro}°\n"
                f"----------------------------------------")

class PilotoCliente:
    def __init__(self,id_cliente, nombre, telefono, presupuesto_maximo, dinero_invertido, tipo_licencia):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.telefono = telefono
        self.presupuesto_maximo = presupuesto_maximo
        self.dinero_invertido = dinero_invertido
        self.tipo_licencia = tipo_licencia