# Este código viola los principios SOLID, especialmente el Principio de Responsabilidad Única (SRP),
# ya que el método create_order hace demasiadas cosas: calcula totales, aplica descuentos,
# procesa pagos, calcula envíos, crea órdenes y envía notificaciones. Además, tiene valores
# hardcodeados y no separa las responsabilidades en clases diferentes.

import random

class OrderSystem:
    def __init__(self):
        # Inicializa la lista de órdenes
        self.orders = []

    def create_order(self, user, items, payment_type):
        # Calcula el total inicial sumando precio * cantidad de cada item
        total = 0
        for item in items:
            total += item["price"] * item["quantity"]

        # Aplica descuentos según el tipo de usuario
        if user["type"] == "regular":
            total -= total * 0.05
        elif user["type"] == "premium":
            total -= total * 0.10
        elif user["type"] == "vip":
            total -= total * 0.20

        # Aplica descuento adicional si el total supera 500
        if total > 500:
            total -= total * 0.05
        # Agrega IVA del 19%
        total += total * 0.19

        # Procesa el método de pago
        if payment_type == "card":
            print("Procesando tarjeta...")
        elif payment_type == "paypal":
            print("Procesando PayPal...")
        elif payment_type == "cash":
            print("Pago en efectivo...")
        else:
            raise Exception("Método de pago inválido")

        # Agrega costo de envío según el país del usuario
        if user["country"] == "CO":
            total += 20000
        else:
            total += 50000

        # Crea el diccionario de la orden con id aleatorio, usuario, items, total y estado
        order = {
            "id": random.random(),
            "user": user,
            "items": items,
            "total": total,
            "status": "created"
        }

        # Agrega la orden a la lista de órdenes
        self.orders.append(order)

        # Envía notificación por email si el usuario tiene email
        if "email" in user:
            print(f"Enviando correo a {user['email']}")
        return order    