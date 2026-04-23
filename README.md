# Order System - TDD y Refactorización con SOLID

## Descripción

Este proyecto consiste en la implementación de pruebas unitarias y la refactorización de un sistema de órdenes defectuoso, aplicando la metodología TDD (Test-Driven Development) y principios SOLID.

---

## 1. Pruebas Unitarias

Se desarrollaron pruebas unitarias utilizando el módulo `unittest` de Python antes de modificar el código original.

### Casos cubiertos

Las pruebas validan los siguientes comportamientos:

* Creación correcta de órdenes
* Cálculo del total
* Descuentos según tipo de usuario (regular, premium, vip)
* Descuento adicional del 5% si el total supera 500
* Aplicación de impuestos (19%)
* Costos de envío (Colombia e internacional)
* Validación de métodos de pago
* Generación de ID de orden
* Comportamiento ante tipo de usuario desconocido
* Verificación de mensajes impresos mediante mock

---

### Resultados iniciales

Al ejecutar las pruebas por primera vez, algunas fallaban debido a inconsistencias en el cálculo del total. Esto permitió identificar errores en la lógica del sistema.

---

### Validación de las pruebas

Para comprobar que las pruebas eran correctas, se introdujo un error intencional en el cálculo del impuesto (cambiando el 19% por 50%). Al ejecutar nuevamente las pruebas, aquellas relacionadas con el cálculo del total fallaron, lo que confirmó que las pruebas detectan errores reales en el sistema.

---

## 2. Problemas del Código Original

El método `create_order` presentaba varios problemas de diseño:

* Múltiples responsabilidades en un solo método
* Uso excesivo de estructuras condicionales
* Lógica de negocio acoplada (descuentos, impuestos, pagos, envío)
* Dificultad para mantenimiento y extensión

---

## 3. Refactorización con SOLID

Se refactorizó el sistema separando las responsabilidades en diferentes clases:

* `DiscountService`: cálculo de descuentos
* `TaxService`: aplicación de impuestos
* `ShippingService`: cálculo de costos de envío
* `PaymentService`: procesamiento de pagos

### Principios aplicados

**Single Responsibility Principle (SRP):**
Cada clase se encarga de una única responsabilidad, lo que facilita el mantenimiento y la comprensión del código.

**Open/Closed Principle (OCP):**
El sistema permite extender funcionalidades (como nuevos tipos de usuario o métodos de pago) sin modificar el código existente.

---

## 4. Validación después del refactor

Después de la refactorización, todas las pruebas unitarias se ejecutaron nuevamente y pasaron correctamente. Esto garantiza que el comportamiento del sistema se mantiene a pesar de los cambios internos.

---

## 5. Estructura del Proyecto

```
src/
 ├── order_system.py
 ├── order_system_original.py
 ├── discount_service.py
 ├── tax_service.py
 ├── shipping_service.py
 └── payment_service.py

tests/
 └── test_order_system.py

README.md
```

---

## 6. Proceso realizado

El desarrollo del proyecto se llevó a cabo de la siguiente manera:

1. Se subió el código original sin modificaciones al repositorio.
2. Se crearon pruebas unitarias para validar el comportamiento del sistema.
3. Se ejecutaron las pruebas, identificando fallos en el cálculo del total.
4. Se introdujo un error controlado en el cálculo del impuesto para verificar que las pruebas detectaban inconsistencias.
5. Se corrigió el error y se verificó que las pruebas volvieran a pasar.
6. Se realizó la refactorización del sistema separando responsabilidades en diferentes clases.
7. Se ejecutaron nuevamente las pruebas para asegurar que el sistema seguía funcionando correctamente después del refactor.

---

## 7. Conclusión

El uso de pruebas unitarias permitió identificar errores en el sistema y validar los cambios realizados durante la refactorización. Al aplicar principios SOLID, el código resultante es más organizado, modular y fácil de mantener, sin alterar su comportamiento original.
