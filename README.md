Sistema de Gestión de Taller de Tuning y Performance

Idea inicial del Proyecto

Este proyecto comenzó con la idea de crear un sistema de gestión integral para un taller de autos especializados en tuning y modificaciones de performance. La visión original era:

Escenario: Un mecánico profesional en un taller de tuning recibe diferentes autos de clientes que necesitan modificaciones y mejoras de rendimiento. 

Flujo principal:
1 Recepción de vehículos - El mecánico recibe autos de diferentes tipos y marcas (Toyota, Honda, Ford, etc.), cada uno con sus características iniciales.
2 Creación de proyectos de trabajo - Para cada cliente se abre un proyecto donde se registra qué mejoras quiere hacer (más potencia, mejor maniobrabilidad, etc.).
3 Personalización y instalación - El mecánico analiza el auto y agrega componentes custom según lo que el cliente necesita y su presupuesto. Puede instalar turbos, suspensiones ajustadas, sistemas de escape personalizado, etc.
4 Validación del proceso - El sistema controla que exista disponibilidad de piezas y que el cliente tenga presupuesto suficiente para cada instalación.
5 Finalización del proyecto - Cuando se terminan todas las modificaciones, el sistema genera un reporte completo mostrando:
    Todos los componentes instalados
    El costo total invertido en el proyecto
    Los cambios conseguidos (HP ganados, mejoras en maniobrabilidad, etc.)
    El auto transformado listo para entregarle al cliente

Nuestro objetivo es simular un taller real donde el mecánico gestiona múltiples proyectos simultáneamente, mantiene control de inventario de piezas, valida presupuestos de clientes, y puede ver en tiempo real cómo evoluciona cada vehículo según las modificaciones que se van aplicando.

Durante el desarrollo, el proyecto se fue adaptando y refinando para aplicar de forma práctica todos los conceptos fundamentales de la Programación Orientada a Objetos, manteniendo siempre esta visión de un taller funcional y realista.

----------------------------------------------------------------------------------------------------------------------------------------

Este es un programa en Python que simula un taller de tuning donde se registran vehículos, clientes, mecánicos y órdenes de trabajo. El sistema permite instalar componentes especiales en los autos para mejorar su rendimiento (aumentar caballos de fuerza y ángulo de giro).

El proyecto demuestra cómo funcionaría un sistema real de gestión de un taller, con control de inventario, validación de presupuestos y modificación de características de vehículos.


Archivos del proyecto

Gestión de Taller de Tuning y Performance.py - Programa principal con todas las clases y el menú (reemplezaremos despues)
pruebas code.py - Pruebas del sistema(luego lo borraremos)

Qué hace el programa

El programa simula las operaciones principales de un taller:

1 Registrar vehículos - Guardar autos con su marca, modelo, año y características iniciales (caballos de fuerza base y ángulo de giro)
2 Registrar clientes y mecánicos - Crear personas que participan en el taller. Los clientes tienen un presupuesto disponible y los mecánicos realizan los trabajos
3 Crear órdenes de trabajo - Asociar un vehículo, un cliente y un mecánico para iniciar un proyecto de tuning
4 Instalar componentes - Agregar piezas de performance (como turbos o suspensiones) al vehículo dentro de una orden
5 Validar automáticamente - El sistema verifica que:
    Existe stock disponible del componente solicitado
    El cliente tiene presupuesto suficiente para comprarlo
6 Aplicar mejoras - Una vez instalados los componentes, se actualiza el vehículo aumentando sus caballos de fuerza y ángulo de giro
7 Ver información - Consultar fichas técnicas con todos los datos actualizados de cada vehículo

aplicamos los 4 pilares de POO

Encapsulamiento

El encapsulamiento protege los datos importantes de un objeto para que no sean modificados de forma incorrecta. En este proyecto:
    El saldo del cliente está protegido y solo se puede modificar a través de métodos específicos (no se puede cambiar directamente)
    Los atributos privados de las clases aseguran que la información se modifique de manera controlada
    Ejemplo: no puedes restar dinero del cliente sin validar que tenga suficiente presupuesto

Herencia

La herencia permite que una clase "herede" características de otra. En este proyecto:
    Existe una clase base llamada `Persona` que tiene atributos comunes como nombre, teléfono y dirección
    Las clases `Cliente` y `Mecánico` heredan de `Persona`, es decir, usan todos sus atributos y métodos
    Esto evita repetir código: ambas personas comparten características, pero cada una tiene sus propias características adicionales

Polimorfismo

El polimorfismo permite que distintas clases respondan de forma diferente al mismo método. En este proyecto:
El método `mostrar_info()` existe en varias clases (Vehículo, Cliente, Mecánico), pero cada uno muestra información diferente
El método `incrementar_rendimiento()` del vehículo modifica los HP y el ángulo de giro de forma específica
Cada clase implementa el mismo concepto de forma diferente según lo que necesita

Abstracción

La abstracción simplifica las cosas complejas mostrando solo lo importante. En este proyecto:
El usuario del programa no necesita saber cómo funciona internamente el cálculo de validaciones
Solo interactúa con métodos simples como "instalar componente" sin preocuparse por los detalles internos
Las clases abstractas definen qué métodos deben tener las clases derivadas (como un contrato)

Ejemplo de uso
aquí está el flujo típico de cómo usar el programa:

1 Ejecuta el programa y se abre un menú interactivo
2 Registra un vehículo nuevo (ejemplo: "Toyota Supra 2020")
    ingresa marca, modelo, año, caballos de fuerza inicial y ángulo de giro
3 Registra un cliente (ejemplo: "Juan García")
    ingresa nombre, teléfono y presupuesto disponible (ej: $50.000)
4 Registra un mecánico que realizará el trabajo
5 Crea una orden de trabajo seleccionando el cliente, vehículo y mecánico
6 Instala componentes al vehículo (ejemplo: Turbo que cuesta $15.000 y suma 200 HP)
    El sistema verifica que el cliente tenga presupuesto
    El sistema verifica que haya stock disponible
    Si todo es correcto, descuenta el dinero y suma los HP
7 Continúa instalando más componentes si lo deseas
8 Finaliza la orden para aplicar todos los cambios al vehículo
9 Consulta la ficha técnica del vehículo para ver los cambios aplicados (HP y ángulo de giro actualizados)

Al terminar, el vehículo tendrá más caballos de fuerza y mejor ángulo de giro de lo que tenía originalmente